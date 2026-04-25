# interactive-buttons-v2

Keyboard-driven interactive button menus for your Python terminal apps.

Navigate with arrow keys, confirm with Enter. Three layout modes, 12 built-in style presets, and optional hotkey bindings. Works in any real terminal on Linux, Windows and macOS.

---

## Installation

```bash
pip install interactive-buttons-v2
```

Requires Python **3.10+** and two lightweight dependencies:

| Package | Purpose |
|---------|---------|
| `colorama` | Cross-platform ANSI color codes |
| `readchar` | Raw single-keystroke input |

---

## Quick example

```python
from interactive_buttons import Button, Component, ButtonStyle, HACKER_STYLE

buttons = [
    Button(label="Continue", value="continue"),
    Button(label="Exit",     value="exit"),
]

comp   = Component(buttons, global_buttons_style=ButtonStyle(**HACKER_STYLE))
choice = comp.column_buttons()

print(f"You chose: {choice}")
```

```text
> Continue      <- highlighted (selected)
  Exit
```

Use **up / down** to navigate and **Enter** to confirm.

---

## Layout modes

`Component` exposes three layout methods. Each one blocks until the user confirms a selection and returns that button's `value`.

### Column layout

Buttons are stacked vertically. Navigate with **up / down**, confirm with **Enter**.

```python
from interactive_buttons import Button, Component, ButtonStyle, CORPORATE_STYLE

buttons = [
    Button(label="New file",  value="new"),
    Button(label="Open file", value="open"),
    Button(label="Save",      value="save"),
    Button(label="Quit",      value="quit"),
]

comp   = Component(buttons)
choice = comp.column_buttons()
```

```text
[New file]   <- highlighted
[Open file]
[Save]
[Quit]
```

### Linear (horizontal) layout

Buttons are placed side by side on a single line. Navigate with **← / →**, confirm with **Enter**. Ideal for binary confirmations (`Yes / No`, `OK / Cancel`).

```python
from interactive_buttons import Button, Component, ButtonStyle, MINIMAL_STYLE

buttons = [
    Button(label="Yes", value=True),
    Button(label="No",  value=False),
]

comp    = Component(buttons, global_buttons_style=ButtonStyle(**MINIMAL_STYLE))
confirm = comp.linear_buttons()
```

### Matrix (grid) layout

Buttons are arranged in a square grid. Navigate with all four arrow keys, confirm with **Enter**. The grid side length is `ceil(sqrt(len(buttons)))`.

```python
from interactive_buttons import Button, Component, ButtonStyle, MATRIX_STYLE

buttons = [
    Button(label="Attack",  value="attack"),
    Button(label="Magic",   value="magic"),
    Button(label="Item",    value="item"),
    Button(label="Defend",  value="defend"),
    Button(label="Flee",    value="flee"),
    Button(label="Status",  value="status"),
    Button(label="Options", value="options"),
    Button(label="Save",    value="save"),
    Button(label="Quit",    value="quit"),
]

comp   = Component(buttons, global_buttons_style=ButtonStyle(**MATRIX_STYLE))
action = comp.matrix_buttons()
```

```text
[Attack]   [Magic]  [Item]
[Defend]   [Flee]   [Status]
[Options]  [Save]   [Quit]
```

---

## Component options

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `buttons` | `list[Button]` | - | Ordered list of buttons |
| `global_buttons_style` | `ButtonStyle` | `DEFAULT_STYLE` | Style applied to buttons without a local override |
| `display_index` | `bool` | `False` | Auto-prefix each button with a digit shortcut (`1`, `2`, …) |
| `index_begin` | `int` | `1` | Starting digit when `display_index` is active |
| `auto_erase` | `bool` | `False` | Erase the rendered buttons automatically after selection |

> **Note:** `display_index=True` and per-button `ButtonKeyBind` cannot be used at the same time. Doing so raises `KeyBindError`.

---

## Styles

### Built-in presets

12 presets are exported from the top-level package as plain `dict`. Unpack with `**`:

```python
from interactive_buttons import ButtonStyle, HACKER_STYLE

style = ButtonStyle(**HACKER_STYLE)
```

- `DEFAULT_STYLE`
- `HACKER_STYLE`
- `MINIMAL_STYLE`
- `MONOCHROME_STYLE`
- `CORPORATE_STYLE`
- `TERMINAL_RETRO_STYLE`
- `MATRIX_STYLE`
- `CYBERPUNK_STYLE`
- `DANGER_STYLE`
- `SUCCESS_STYLE`
- `SUNSET_STYLE`
- `GHOST_STYLE`

### Custom style

```python
from colorama import Fore, Back
from interactive_buttons import ButtonStyle, Button, Component

my_style = ButtonStyle(
    text_color=Fore.MAGENTA,
    highlight_color=Back.WHITE,
    spaces_count=4,
    left_decorator="* ",
    right_decorator=" *",
)

comp = Component(buttons, global_buttons_style=my_style)
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `text_color` | `str` | ANSI code for the label text color |
| `highlight_color` | `str` | ANSI code applied to the selected button background |
| `spaces_count` | `int` | Padding spaces on each side of the label (minimum 2) |
| `left_decorator` | `str` | String prepended to the label |
| `right_decorator` | `str` | String appended to the label |

### Per-button style override

Each `Button` accepts a `local_button_style` that overrides the component-level style for that button only:

```python
from interactive_buttons import Button, Component, ButtonStyle, SUCCESS_STYLE, DANGER_STYLE

buttons = [
    Button(label="Confirm", value="confirm", local_button_style=ButtonStyle(**SUCCESS_STYLE)),
    Button(label="Cancel",  value="cancel",  local_button_style=ButtonStyle(**DANGER_STYLE)),
]

comp   = Component(buttons)
choice = comp.linear_buttons()
```

---

## Key bindings

`ButtonKeyBind` lets you assign one or more hotkeys to a button. Pressing a bound key moves the cursor to that button, or immediately confirms it if `press_on_selection=True`.

### Basic binding

```python
from interactive_buttons import Button, ButtonKeyBind, Component, ButtonStyle, HACKER_STYLE

save_bind = ButtonKeyBind(b_keys=["s", "1"])
quit_bind = ButtonKeyBind(b_keys=["q", "2"])

buttons = [
    Button(label="Save", value="save", key_bind=save_bind),
    Button(label="Quit", value="quit", key_bind=quit_bind),
]

comp   = Component(buttons, global_buttons_style=ButtonStyle(**HACKER_STYLE))
choice = comp.column_buttons()
```

Pressing `s` or `1` jumps to **Save**. The user still needs **Enter** to confirm.

### Instant-confirm on key press

Set `press_on_selection=True` to confirm the button the moment its key is pressed, no **Enter** needed:

```python
yes_bind = ButtonKeyBind(b_keys=["y"], press_on_selection=True)
no_bind  = ButtonKeyBind(b_keys=["n"], press_on_selection=True)

buttons = [
    Button(label="Yes", value=True,  key_bind=yes_bind),
    Button(label="No",  value=False, key_bind=no_bind),
]

comp    = Component(buttons)
confirm = comp.linear_buttons()
# Pressing "y" immediately returns True; pressing "n" immediately returns False.
```

### Case-sensitive keys

By default, key matching is case-insensitive (`a` and `A` trigger the same binding). Set `case_sensitive=True` to distinguish them:

```python
lower_bind = ButtonKeyBind(b_keys=["a"], case_sensitive=True)
upper_bind = ButtonKeyBind(b_keys=["A"], case_sensitive=True)
```

### Accepted characters

Each entry in `b_keys` must be a **single ASCII alphanumeric character** (`A-Z`, `a-z`, `0-9`). Anything else raises `KeyBindError` at construction time. Each key must also be unique across all buttons in the same `Component`.


## Documentation

Full documentation at **[interactive-buttons.mbinc.tech](https://interactive-buttons.mbinc.tech)**.
