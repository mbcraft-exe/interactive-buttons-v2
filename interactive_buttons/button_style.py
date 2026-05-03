import readchar
from .exceptions import KeyBindError
from typing import Any

try:
    from colorama import Back, Fore, Style
    _RESET_COLOR: str = Style.RESET_ALL
except ImportError:
    Fore = None  # type: ignore[assignment]
    Back = None  # type: ignore[assignment]
    _RESET_COLOR = "\033[0m"


class ButtonStyle:
    """Visual style definition for buttons.

    :param text_color: ANSI escape code for the label text color (works with colorama functions).
    :param highlight_color: ANSI escape code applied to the selected button background (works with colorama functions).
    :param spaces_count: Padding spaces around each label (minimum 2).
    :param left_decorator: String prepended to the button label.
    :param right_decorator: String appended to the button label.
    """

    _text_color: str
    _highlight_color: str
    _spaces_count: int      # This variable won't change when ButtonStyle is used on one button
    _left_decorator: str
    _right_decorator: str

    def __init__(self, text_color: str,
                        highlight_color: str,
                        spaces_count: int,
                        left_decorator: str,
                        right_decorator: str) -> None:
        """See class-level docstring for parameter descriptions."""
        self._text_color = text_color
        self._highlight_color = highlight_color
        self._spaces_count = 2 if spaces_count < 2 else spaces_count  # The minimum amout of spaces is 2.
        self._left_decorator = left_decorator
        self._right_decorator = right_decorator

    @property
    def text_color(self) -> str:
        """ANSI escape code for the label text color."""
        return self._text_color

    @property
    def highlight_color(self) -> str:
        """ANSI escape code applied to the selected button background."""
        return self._highlight_color

    @property
    def spaces_count(self) -> int:
        """Padding spaces around each button label (minimum 2)."""
        return self._spaces_count

    @property
    def left_decorator(self) -> str:
        """String prepended to the button label."""
        return self._left_decorator

    @property
    def right_decorator(self) -> str:
        """String appended to the button label."""
        return self._right_decorator

class MultiSelectStyle:
    """Configuration enabling multi-selection on a button component.

    :param tick_on: Marker prepended to a selected button label.
    :param tick_off: Marker prepended to an unselected button label.
    :param min_selected_amount: Minimum number of buttons the user must select before confirming.
    :param max_selected_amount: Maximum number of buttons the user may select. ``-1`` disables the upper limit.
    :param display_error: Optional message displayed when the user tries to confirm an invalid selection.
    :param select_keys: Keys that toggle the selection of the highlighted button. Defaults to ``SPACE``.
    :raises KeyBindError: If any key in *select_keys* is not a single ASCII alphanumeric character or space.
    """

    _tick_on: str
    _tick_off: str
    _min_selected_amount: int
    _max_selected_amount: int
    _display_error: str | None
    _select_keys: list[str]
    _selected: list[Any]

    def __init__(self, tick_on: str = "[x] ",
                        tick_off: str = "[ ] ",
                        min_selected_amount: int = 0,
                        max_selected_amount: int = -1,
                        display_error: str | None = None,
                        select_keys: list[str] | None = None) -> None:
        """See class-level docstring for parameter descriptions."""
        self._tick_on = tick_on
        self._tick_off = tick_off
        self._min_selected_amount = min_selected_amount
        self._max_selected_amount = max_selected_amount
        self._display_error = display_error
        self._select_keys = select_keys if select_keys is not None else [readchar.key.SPACE]

        for key in self._select_keys:
            if not (len(key) == 1 and key.isascii() and (key.isalnum() or key == ' ')):
                raise KeyBindError(f"`{key}` is not a valid entry for keybinding."
                                    "\nAccepted: A-Z, a-z, 0-9, SPACE (' ')")

        self._selected = []

    @property
    def tick_on(self) -> str:
        """Marker prepended to a selected button label."""
        return self._tick_on

    @property
    def tick_off(self) -> str:
        """Marker prepended to an unselected button label."""
        return self._tick_off

    @property
    def min_selected_amount(self) -> int:
        """Minimum number of buttons the user must select."""
        return self._min_selected_amount

    @property
    def max_selected_amount(self) -> int:
        """Maximum number of buttons the user may select. ``-1`` disables the upper limit."""
        return self._max_selected_amount

    @property
    def display_error(self) -> str | None:
        """Optional message displayed on invalid selection."""
        return self._display_error

    @property
    def select_keys(self) -> list[str]:
        """Keys that toggle the selection of the highlighted button."""
        return self._select_keys

    @property
    def selected(self) -> list[Any]:
        """Values of the buttons currently marked as selected."""
        return self._selected

    def add_to_selected(self, value: Any) -> None:
        """Mark *value* as selected."""
        self._selected.append(value)

    def remove_from_selected(self, value: Any) -> None:
        """Unmark *value* from the selected list."""
        self._selected.remove(value)
