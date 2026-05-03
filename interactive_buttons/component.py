import math
import re
import shutil
import termios
from typing import Any
import sys

import readchar

from .button import Button
from .button_style import ButtonStyle, MultiSelectStyle, _RESET_COLOR
from .button_styles_presets import DEFAULT_STYLE
from .exceptions import *
from .buttons_kinds import MatrixButtons, LinearButtons, ColumnButtons


_ANSI_ESCAPE = re.compile(r'\033\[[^a-zA-Z]*[a-zA-Z]')

class Component(MatrixButtons, LinearButtons, ColumnButtons):
    """Interactive button component combining all layout modes.

    Use [`column_buttons`][interactive_buttons.Component.column_buttons],
    [`linear_buttons`][interactive_buttons.Component.linear_buttons], or
    [`matrix_buttons`][interactive_buttons.Component.matrix_buttons]
    to render the buttons and get the user's selection.

    :param buttons: Ordered list of [`Button`][interactive_buttons.Button] instances.
    :param global_buttons_style: Style applied to buttons without a local override.
    :param multi_select: Optional [`MultiSelectStyle`][interactive_buttons.MultiSelectStyle] enabling multi-selection mode. Defaults to ``None``.
    :param display_index: Prefix each button with a digit keys shortcut when ``True``.
    :param index_begin: Digit assigned to the first button when *display_index* is active. Defaults to ``1``.
    :param auto_erase: Erase the rendered output automatically after selection. Defaults to ``False``.
    :raises MoreButtonsThanIndexes: When *display_index* is ``True`` and buttons exceed available digits.
    :raises KeyBindError: On key-bind/display-index conflict or duplicate keys across buttons.
    :raises MultiSelectError: When *multi_select* bounds are inconsistent with the number of buttons.
    """

    _buttons: list[Button]
    _global_buttons_style: ButtonStyle
    _multi_select: MultiSelectStyle | None
    _display_index: bool
    _index_begin: int
    _auto_erase: bool
    _binded_keys: list[str]
    _size: int         # grid size for matrix, button count for column, 1 for linear
    _render_lines: int # actual terminal lines the last render occupied

    def __init__(self, buttons: list[Button],
                        global_buttons_style: ButtonStyle = ButtonStyle(**DEFAULT_STYLE),
                        multi_select: MultiSelectStyle | None = None,
                        display_index: bool = False,
                        index_begin: int = 1,
                        auto_erase: bool = False) -> None:
        """See class-level docstring for parameter descriptions."""
        if display_index and 10 - index_begin < len(buttons):
            raise MoreButtonsThanIndexes(
                f"{10 - index_begin} indexes available for {len(buttons)} buttons.")
        self._buttons = buttons
        self._global_buttons_style = global_buttons_style
        self._multi_select = multi_select
        if multi_select is not None:
            if multi_select.max_selected_amount > len(buttons):
                raise MultiSelectError(
                    f"`max_selected_amount` ({multi_select.max_selected_amount}) "
                    f"cannot be superior to the number of buttons ({len(buttons)})."
                )
            if multi_select.min_selected_amount > len(buttons):
                raise MultiSelectError(
                    f"`min_selected_amount` ({multi_select.min_selected_amount}) "
                    f"cannot be superior to the number of buttons ({len(buttons)})."
                )
        self._display_index = display_index
        self._index_begin = index_begin
        self._auto_erase = auto_erase
        self._binded_keys = []
        for button in buttons:
            if button.key_bind_keys is not None:
                if button._key_bind and self._display_index:
                    raise KeyBindError(
                        f"Button `{button.label}` defines a `key_bind` while `display_index` is enabled on the component. "
                        "Both mechanisms compete for keystrokes (digits in particular), so they cannot be used together. "
                        "Either remove `display_index=True` from the Component, or remove the `key_bind` from every Button."
                    )
                self._binded_keys += button.key_bind_keys # type: ignore
        if len(self._binded_keys) != len(set(self._binded_keys)):
            duplicates = sorted({k for k in self._binded_keys if self._binded_keys.count(k) > 1})
            raise KeyBindError(
                f"The following key(s) are bound to more than one button: {duplicates}. "
                "Each key can only be bound to a single button."
            )
        self._size = 0
        self._render_lines = 0

    @staticmethod
    def _visual_lines(text: str) -> int:
        cols = shutil.get_terminal_size((80, 24)).columns
        stripped = _ANSI_ESCAPE.sub('', text)
        segments = stripped.split('\n')
        newlines = len(segments) - 1
        wrap_lines = sum((len(s) - 1) // cols for s in segments if s)
        return newlines + wrap_lines

    @staticmethod
    def _clear_lines(n: int = 1) -> None:
        sys.stdout.write("\033[F\033[2K" * n)
        sys.stdout.flush()

    @staticmethod
    def _read_key() -> str:
        try:
            return readchar.readkey()
        except termios.error:
            raise EmulatedTerminalDetected(
                "Your terminal seems to be emulated, interactive_buttons can't be used that way.\n"
                "Run the programme in a real terminal."
            )

    @staticmethod
    def _try_int(key: str | None) -> int | None:
        try:
            return int(key)  # type: ignore[arg-type]
        except (ValueError, TypeError):
            return None

    def _button_visible_width(self, button: Button, index: int) -> int:
        """Visible width of a fully rendered button, ignoring ANSI escape codes."""
        style = button.local_button_style or self._global_buttons_style
        width = len(style.left_decorator) + len(button.label) + len(style.right_decorator)
        if self._display_index:
            width += len(str(index + self._index_begin)) + 2
        if self._multi_select is not None:
            width += max(len(self._multi_select.tick_on), len(self._multi_select.tick_off))
        return width

    def _build_button_style(self, label: str,
                                highlighted: bool = False,
                                ticked: bool = False,
                                index: int = 0,
                                local_style: ButtonStyle | None = None) -> str:
        style = local_style if local_style is not None else self._global_buttons_style
        if self._multi_select is not None:
            tick = self._multi_select.tick_on if ticked else self._multi_select.tick_off
        else:
            tick = ""
        return (
            f"{f'{index + self._index_begin}. ' if self._display_index else ''}"
            f"{tick}"
            f"{style.text_color if highlighted else ''}"
            f"{style.highlight_color if highlighted else ''}"
            f"{style.left_decorator}{label}{style.right_decorator}"
            f"{_RESET_COLOR}"
        )

    def erase_buttons(self, bypass: bool = False) -> None:
        """Erase the rendered buttons from the terminal.

        No-op when *auto_erase* is enabled, unless *bypass* is ``True``
        which forces erasure and silences the warning.

        :param bypass: Force erasure even when *auto_erase* is enabled. Defaults to ``False``.
        """
        if not self._auto_erase or bypass:
            self._clear_lines(self._render_lines)
        else:
            print(
                f"\033[93mWarning: do not use `erase_buttons` function when `auto_erase` is enabled.\n"
                f"To silent that warning and make the function work anyway, set `bypass=True` on this function."
                f"{_RESET_COLOR}"
            )
