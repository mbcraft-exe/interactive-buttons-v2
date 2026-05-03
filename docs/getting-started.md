# Getting Started

## Installation

```bash
pip install interactive-buttons-v2
```

The library requires Python **3.10+** and two lightweight dependencies:

| Package | Purpose |
|---------|---------|
| `colorama` | Cross-platform ANSI color codes |
| `readchar` | Raw single-keystroke input |

---

## Your first button menu

### 1. Import the building blocks

```python
from interactive_buttons import Button, Component, ButtonStyle, HACKER_STYLE
```

### 2. Create your buttons

Each [`Button`](api/button.md#interactive_buttons.Button) has a **label** (what the user sees) and a **value** (what your code receives).

```python
buttons = [
    Button(label="Start game",  value="start"),
    Button(label="Load save",   value="load"),
    Button(label="Settings",    value="settings"),
    Button(label="Quit",        value="quit"),
]
```

### 3. Wrap them in a Component

[`Component`](api/component.md) is the renderer and input handler. Pass a style preset or your own [`ButtonStyle`](api/button-style.md).

```python
comp = Component(
    buttons,
    global_buttons_style=ButtonStyle(**HACKER_STYLE),
)
```

### 4. Display and wait for a selection

Pick a layout : `column_buttons`, `linear_buttons`, or `matrix_buttons`, and call it. The call **blocks** until the user confirms a choice and returns that button's `value`.

```python
choice = comp.column_buttons()
print(f"Selected: {choice}")
```

![Getting started example](https://github.com/mbcraft-exe/interactive-buttons-v2/blob/main/images/matrix_style_buttons_column.png?raw=true)

---

## Component options at a glance

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `buttons` | list[[Button](/api/button/#interactive_buttons.Button)] | - | Ordered list of buttons |
| `global_buttons_style` | [`ButtonStyle`](/api/button-style/?h=buttonst) | [`DEFAULT_STYLE`](/api/presets/?h=default#interactive_buttons.button_styles_presets.DEFAULT_STYLE) | Style applied to buttons without a local override |
| `multi_select` | [`MultiSelectStyle`](/api/button-style/#interactive_buttons.MultiSelectStyle) \| `None` | `None` | Enable multi-selection; layout methods return `list[Any]` |
| `display_index` | `bool` | `False` | Auto-prefix each button with a digit shortcut (`1`, `2`, ...) |
| `index_begin` | `int` | `1` | Starting digit when `display_index` is active |
| `auto_erase` | `bool` | `False` | Erase the rendered buttons automatically after selection |

---

## Navigation keys

| Layout | Keys |
|--------|------|
| `column_buttons` | up / down * Enter |
| `linear_buttons` | left / right * Enter |
| `matrix_buttons` | left / right / up / down * Enter |

In all layouts, digit shortcuts (when `display_index=True`) or custom key bindings jump directly to a button.

---

## What's next?

<div class="grid cards" markdown>

-   :material-view-list:{ .lg .middle } **Layout examples**

    ---
    See all three layouts with full working code.

    [:octicons-arrow-right-24: Layouts](examples/layouts.md)

-   :material-palette:{ .lg .middle } **Style customisation**

    ---
    Browse presets or build your own `ButtonStyle`.

    [:octicons-arrow-right-24: Styles](examples/styles.md)

-   :material-keyboard:{ .lg .middle } **Key bindings**

    ---
    Assign hotkeys, control case sensitivity, and use instant-confirm.

    [:octicons-arrow-right-24: Key bindings](examples/keybinds.md)

-   :material-checkbox-multiple-marked:{ .lg .middle } **Multi-select**

    ---
    Let the user tick several buttons at once before confirming. Configure min/max bounds and a custom error message.

    [:octicons-arrow-right-24: Multi-select](examples/multi-select.md)

</div>
