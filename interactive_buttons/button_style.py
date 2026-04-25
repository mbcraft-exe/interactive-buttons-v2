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
