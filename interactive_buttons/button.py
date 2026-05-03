from typing import Any

from .button_style import ButtonStyle
from .exceptions import KeyBindError
from dataclasses import dataclass


@dataclass
class ButtonKeyBind:
    """Key binding configuration for a [`Button`][interactive_buttons.Button].

    :param b_keys: Single ASCII alphanumeric characters that trigger the button.
    :param case_sensitive: Whether matching is case-sensitive. Defaults to ``False``.
    :param press_on_selection: If ``True``, selecting via key immediately confirms the button. Defaults to ``False``.
    :raises KeyBindError: If any key in *b_keys* is not a single ASCII alphanumeric character.
    """

    b_keys: list[str]
    case_sensitive: bool = False
    press_on_selection: bool = False

    def __post_init__(self):
        for key in self.b_keys:
            if not (len(key) == 1 and key.isascii() and (key.isalnum() or key == ' ')):
                raise KeyBindError(f"`{key}` is not a valid entry for keybinding."
                                    "\nAccepted: A-Z, a-z, 0-9, SPACE (' ')")

class Button:
    """A selectable button with an optional key binding and custom style."""

    __slots__ = ("_label", "_value", "_key_bind", "_local_button_style")

    _label: str
    _value: Any
    _key_bind: ButtonKeyBind | None
    _local_button_style: ButtonStyle | None

    def __init__(self, *,
                    label: str,
                    value: Any,
                    key_bind: ButtonKeyBind | None = None,
                    local_button_style: ButtonStyle | None = None) -> None:
        """
        :param label: Text displayed on the button. Newlines and tabs are escaped.
        :param value: Value returned when this button is confirmed.
        :param key_bind: Optional keyboard shortcut configuration.
        :param local_button_style: Per-button style override; ``None`` uses the component's global style.
        """
        self._label = label.replace("\n", "\\n").replace("\r", "\\r").replace("\t", "\\t")
        self._value = value
        self._key_bind = key_bind
        self._local_button_style = local_button_style

    @property
    def label(self) -> str:
        """Display label of the button."""
        return self._label

    @property
    def key_bind_press_on_selection(self) -> list[str] | None:
        if self._key_bind is None:
            return None
        return self._key_bind.press_on_selection # type: ignore

    @property
    def key_bind_case_sensitive(self) -> list[str] | None:
        if self._key_bind is None:
            return None
        return self._key_bind.case_sensitive # type: ignore

    @property
    def key_bind_keys(self) -> list[str] | None:
        if self._key_bind is None:
            return None
        return self._key_bind.b_keys # type: ignore

    @property
    def value(self) -> Any:
        """Value returned when the button is confirmed."""
        return self._value

    @property
    def local_button_style(self) -> ButtonStyle | None:
        """Per-button style override, or ``None`` to use the component's global style."""
        return self._local_button_style
