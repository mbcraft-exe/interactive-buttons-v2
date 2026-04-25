"""Built-in style presets for [`ButtonStyle`][interactive_buttons.ButtonStyle].

Each constant is a plain ``dict`` whose keys match the parameters of
[`ButtonStyle`][interactive_buttons.ButtonStyle].  Pass them with the ``**``
unpacking operator::

    from interactive_buttons import ButtonStyle, HACKER_STYLE

    style = ButtonStyle(**HACKER_STYLE)
"""

from typing import Any

#: Classic bracketed buttons - dark text on a white background when selected.
DEFAULT_STYLE: dict[str, Any] = dict(
    text_color="\033[30m",
    highlight_color="\033[47m",
    spaces_count=5,
    left_decorator="[",
    right_decorator="]",
)

#: Minimal green-on-black arrow style - no background highlight.
HACKER_STYLE: dict[str, Any] = dict(
    text_color="\033[32m",
    highlight_color="",
    spaces_count=5,
    left_decorator="> ",
    right_decorator="",
)

#: Underline-only highlight - no color, no decorators.
MINIMAL_STYLE: dict[str, Any] = dict(
    text_color="",
    highlight_color="\033[4m",
    spaces_count=3,
    left_decorator="",
    right_decorator="",
)

#: Reversed-video highlight - white text, no decorators.
MONOCHROME_STYLE: dict[str, Any] = dict(
    text_color="\033[37m",
    highlight_color="\033[7m",
    spaces_count=4,
    left_decorator="",
    right_decorator="",
)

#: Blue bracketed buttons - bold white text on a blue background when selected.
CORPORATE_STYLE: dict[str, Any] = dict(
    text_color="\033[34m",
    highlight_color="\033[1;44;97m",
    spaces_count=4,
    left_decorator="[",
    right_decorator="]",
)

#: Amber retro style - yellow text with a diamond ``*`` prefix.
TERMINAL_RETRO_STYLE: dict[str, Any] = dict(
    text_color="\033[33m",
    highlight_color="\033[43;30m",
    spaces_count=4,
    left_decorator="◆ ",
    right_decorator="",
)

#: Bold green on black - square bracket decorators, Matrix-movie aesthetic.
MATRIX_STYLE: dict[str, Any] = dict(
    text_color="\033[32m",
    highlight_color="\033[1;32;40m",
    spaces_count=3,
    left_decorator="[ ",
    right_decorator=" ]",
)

#: Blue text with amber highlight - French guillemet decorators.
CYBERPUNK_STYLE: dict[str, Any] = dict(
    text_color="\033[34m",
    highlight_color="\033[43;30m",
    spaces_count=4,
    left_decorator="« ",
    right_decorator=" »",
)

#: Red alert style - bold white on red background, warning prefix.
DANGER_STYLE: dict[str, Any] = dict(
    text_color="\033[91m",
    highlight_color="\033[1;41;97m",
    spaces_count=3,
    left_decorator="/!\\ ",
    right_decorator=" ",
)

#: Bright green confirmation style - checkmark ``[v]`` prefix.
SUCCESS_STYLE: dict[str, Any] = dict(
    text_color="\033[92m",
    highlight_color="\033[1;42;30m",
    spaces_count=3,
    left_decorator="✓ ",
    right_decorator="",
)

#: Warm amber with magenta highlight - chevron wrap decorators.
SUNSET_STYLE: dict[str, Any] = dict(
    text_color="\033[33m",
    highlight_color="\033[1;45;93m",
    spaces_count=4,
    left_decorator="> ",
    right_decorator=" <",
)

#: Dim white text, bold on selection - invisible until focused.
GHOST_STYLE: dict[str, Any] = dict(
    text_color="\033[2;37m",
    highlight_color="\033[1;37m",
    spaces_count=4,
    left_decorator="",
    right_decorator="",
)
