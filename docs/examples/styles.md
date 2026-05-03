# Style Examples

interactive-buttons ships 12 ready-to-use style presets and lets you build
fully custom styles with [`ButtonStyle`](../api/button-style.md).

---

## Using a built-in preset

Every preset is exported from the top-level package as a plain `dict`.  Unpack
it into `ButtonStyle` with `**`:

```python
from interactive_buttons import ButtonStyle, HACKER_STYLE, Component, Button

buttons = [Button(label="Launch", value="go"), Button(label="Abort", value="no")]
comp    = Component(buttons, global_buttons_style=ButtonStyle(**HACKER_STYLE))
comp.linear_buttons()
```

See the [Style Presets reference](../api/presets.md) for the full catalogue with visual descriptions.

---

## Building a custom style

[`ButtonStyle`](../api/button-style.md) takes five parameters:

| Parameter | Type | Description |
|-----------|------|-------------|
| `text_color` | `str` | ANSI code for the label text color |
| `highlight_color` | `str` | ANSI code applied to the **selected** button background |
| `spaces_count` | `int` | Padding spaces on each side of the label (minimum 2) |
| `left_decorator` | `str` | String prepended to the label |
| `right_decorator` | `str` | String appended to the label |

Use `colorama.Fore` and `colorama.Back` for a readable, cross-platform way to
specify colors:

```python
from colorama import Fore, Back
from interactive_buttons import ButtonStyle, Button, Component

pastel_style = ButtonStyle(
    text_color=Fore.MAGENTA,
    highlight_color=Back.WHITE,
    spaces_count=4,
    left_decorator="* ",
    right_decorator=" *",
)

buttons = [
    Button(label="Profile", value="profile"),
    Button(label="Logout",  value="logout"),
]

comp   = Component(buttons, global_buttons_style=pastel_style)
choice = comp.column_buttons()
```

```text
* Profile *   <- highlighted (magenta text, white background)
* Logout  *
```

---

## Per-button style override

Each `Button` accepts a `local_button_style` that overrides the component-level
style for that button only:

```python
from colorama import Fore, Back
from interactive_buttons import Button, Component, ButtonStyle, SUCCESS_STYLE, DANGER_STYLE

confirm_btn = Button(
    label="Confirm",
    value="confirm",
    local_button_style=ButtonStyle(**SUCCESS_STYLE),
)

cancel_btn = Button(
    label="Cancel",
    value="cancel",
    local_button_style=ButtonStyle(**DANGER_STYLE),
)

comp   = Component([confirm_btn, cancel_btn])
choice = comp.linear_buttons()
```

![Per-button style override example](https://github.com/mbcraft-exe/interactive-buttons-v2/blob/main/images/multi_themes_linear_buttons_example.png?raw=true)

The global style on `Component` is used as a fallback for buttons that have no
`local_button_style`.

---

## Raw ANSI vs colorama

Both approaches are valid:

=== "colorama"

    ```python
    from colorama import Fore, Back
    style = ButtonStyle(
        text_color=Fore.CYAN,
        highlight_color=Back.BLUE,
        spaces_count=4,
        left_decorator="[",
        right_decorator="]",
    )
    ```

=== "Raw ANSI"

    ```python
    style = ButtonStyle(
        text_color="\033[36m",    # cyan
        highlight_color="\033[44m",  # blue background
        spaces_count=4,
        left_decorator="[",
        right_decorator="]",
    )
    ```

`colorama` is recommended because it handles Windows ANSI initialization
automatically.
