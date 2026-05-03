# interactive-buttons

**Keyboard-driven interactive button menus for your Python terminal apps.**

<div class="grid cards" markdown>

-   :material-gesture-tap-button:{ .lg .middle } **Three layout modes**

    ---

    Render buttons as a horizontal row, a vertical column, or a square grid, one method call each.

    [:octicons-arrow-right-24: Layout examples](examples/layouts.md)

-   :material-palette-outline:{ .lg .middle } **12 built-in style presets**

    ---

    Plug in `HACKER_STYLE`, `CYBERPUNK_STYLE`, `CORPORATE_STYLE`, and nine others with zero configuration.

    [:octicons-arrow-right-24: Style presets](api/presets.md)

-   :material-keyboard-outline:{ .lg .middle } **Hotkey bindings**

    ---

    Assign one or more keys to any button, with optional instant-confirm on press and case-sensitivity control.

    [:octicons-arrow-right-24: Key binding examples](examples/keybinds.md)

-   :material-code-braces:{ .lg .middle } **Minimal dependencies**

    ---

    Relies only on `colorama` and `readchar`. Works in any real terminal on Linux, macOS, and Windows.

    [:octicons-arrow-right-24: Getting started](getting-started.md)

</div>

---

## Installation

```bash
pip install interactive-buttons-v2
```

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

> Use **up / down** to navigate and **Enter** to confirm.

```text
> Continue      <- highlighted (selected)
  Exit
```
