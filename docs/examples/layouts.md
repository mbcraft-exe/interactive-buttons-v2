# Layout Examples

`Component` exposes three layout methods.  Each one blocks until the user
confirms a selection and then returns that button's `value`.

---

## Column layout

Buttons are stacked vertically. Navigate with **up / down**, confirm with **Enter**.

```python
from interactive_buttons import Button, Component, ButtonStyle, CORPORATE_STYLE

buttons = [
    Button(label="New file",    value="new"),
    Button(label="Open file",   value="open"),
    Button(label="Save",        value="save"),
    Button(label="Quit",        value="quit"),
]

comp   = Component(buttons, global_buttons_style=ButtonStyle(**CORPORATE_STYLE))
choice = comp.column_buttons()
print(f"Action: {choice}")
```

![Column layout example](https://github.com/mbcraft-exe/interactive-buttons-v2/blob/main/images/basic_column_buttons_example.png?raw=true)

---

## Linear (horizontal) layout

Buttons are placed side by side on a single line. Navigate with **<- / ->**, confirm with **Enter**.

```python
from interactive_buttons import Button, Component, ButtonStyle, MINIMAL_STYLE

buttons = [
    Button(label="Yes", value=True),
    Button(label="No",  value=False),
]

comp    = Component(buttons, global_buttons_style=ButtonStyle(**MINIMAL_STYLE))
confirm = comp.linear_buttons()
print(f"Confirmed: {confirm}")
```

![Linear layout example](https://github.com/mbcraft-exe/interactive-buttons-v2/blob/main/images/minimal_style_buttons_linear.png?raw=true)

!!! tip
    Linear mode is ideal for binary confirmations (`Yes / No`, `OK / Cancel`).

---

## Matrix (grid) layout

Buttons are arranged in a square grid. Navigate with all four arrow keys, confirm with **Enter**.

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
print(f"Action: {action}")
```

![Matrix layout example](https://github.com/mbcraft-exe/interactive-buttons-v2/blob/main/images/sunset_style_buttons_matrix.png?raw=true)

The grid side length is `ceil(sqrt(len(buttons)))`, so nine buttons → 3 × 3 grid.

---

## Using `display_index`

When `display_index=True`, each button is prefixed with a digit that the user can press to jump straight to it.

```python
from interactive_buttons import Button, Component, ButtonStyle, DEFAULT_STYLE

buttons = [
    Button(label="Option A", value="a"),
    Button(label="Option B", value="b"),
    Button(label="Option C", value="c"),
]

comp   = Component(
    buttons,
    global_buttons_style=ButtonStyle(**DEFAULT_STYLE),
    display_index=True,
    index_begin=1,        # first button is reachable with key "1"
)
choice = comp.column_buttons()
```

```text
1. [ Option A ]
2. [ Option B ]
3. [ Option C ]
```

Press `2` to jump to **Option B**, then **Enter** to confirm.

!!! warning "Mutually exclusive with key bindings"
    You cannot use `display_index=True` and per-button `ButtonKeyBind` at the same time.
    Doing so raises [`KeyBindError`](../api/exceptions.md).

!!! warning "Boundaries"
	If `display_index` is enabled, the buttons count will be restrained in the range of `1` to `9`. 

---

## Auto-erasing after selection

Pass `auto_erase=True` to automatically clear the rendered buttons from the terminal once the user confirms:

```python
comp = Component(buttons, auto_erase=True)
choice = comp.column_buttons()
# Terminal output above is now gone; cursor is back where it started.
print(f"You chose: {choice}")
```

You can also trigger erasure manually via [`Component.erase_buttons()`](../api/component.md#interactive_buttons.Component.erase_buttons).

!!! warning "Can't be used with `auto_erase=True`"
    You cannot use `Component.erase_buttons()` with `auto_erase` enabled at the same time.
    Doing so will trigger a warning and `Component.erase_buttons()` will not work unless you set `bypass=True`.
	Turning this argument on may delete lines outer the buttons scope!
