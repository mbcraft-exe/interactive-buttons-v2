# Multi-select Examples

Pass a [`MultiSelectStyle`](../api/button-style.md#interactive_buttons.MultiSelectStyle) to `Component` to turn any layout into a multi-selection picker. The user navigates as usual and presses **Space** (or a custom key) to toggle the ticked state of the highlighted button. Pressing **Enter** confirms the selection and returns a `list` of the ticked values.

---

## Basic multi-select

```python
from interactive_buttons import Button, Component, MultiSelectStyle

toppings = [
    Button(label="Cheese",    value="cheese"),
    Button(label="Mushrooms", value="mushrooms"),
    Button(label="Peppers",   value="peppers"),
    Button(label="Olives",    value="olives"),
]

ms = MultiSelectStyle()   # default: SPACE toggles, no bounds

comp    = Component(toppings, multi_select=ms)
choices = comp.column_buttons()   # list[Any]

print(f"You chose: {choices}")
```

![Basic multi-select example](https://github.com/mbcraft-exe/interactive-buttons-v2/blob/main/images/basic_multiselect_buttons.png?raw=true)

---

## Enforcing selection bounds

Use `min_selected_amount` and `max_selected_amount` to constrain how many buttons the user must tick before Enter is accepted. Pair with `display_error` to show inline feedback.

```python
from interactive_buttons import Button, Component, MultiSelectStyle

options = [
    Button(label="Python",     value="python"),
    Button(label="JavaScript", value="js"),
    Button(label="Rust",       value="rust"),
    Button(label="Go",         value="go"),
    Button(label="C++",        value="cpp"),
]

ms = MultiSelectStyle(
    min_selected_amount=1,
    max_selected_amount=3,
    display_error="Please select between 1 and 3 languages.",
)

comp    = Component(options, multi_select=ms)
choices = comp.column_buttons()
```

If the user presses Enter without satisfying the bounds, `display_error` is printed below the buttons and input continues.

---

## Custom tick markers

Override the default `[x]` / `[ ]` prefixes with any string:

```python
ms = MultiSelectStyle(
    tick_on="✔ ",
    tick_off="  ",
)
```

```text
✔ Option A
  Option B
✔ Option C
```

---

## Custom selection key

By default `Space` toggles selection. Change it via `select_keys`:

```python
ms = MultiSelectStyle(
    select_keys=["x"],   # press "x" to tick/untick
)
```

`select_keys` accepts the same characters as [`ButtonKeyBind.b_keys`](../api/button.md#interactive_buttons.ButtonKeyBind): single ASCII alphanumeric characters or space.

---

## Multi-select with linear layout

Multi-select works with all three layout methods:

```python
from interactive_buttons import Button, Component, MultiSelectStyle, ButtonStyle, CORPORATE_STYLE

days = [
    Button(label="Mon", value="mon"),
    Button(label="Tue", value="tue"),
    Button(label="Wed", value="wed"),
    Button(label="Thu", value="thu"),
    Button(label="Fri", value="fri"),
]

ms   = MultiSelectStyle(min_selected_amount=1, display_error="Pick at least one day.")
comp = Component(days, global_buttons_style=ButtonStyle(**CORPORATE_STYLE), multi_select=ms)
selected_days = comp.linear_buttons()
```

---

## Return value

When `multi_select` is active the layout methods always return `list[Any]`, even if the user ticked only one button. An empty list is returned if no buttons were ticked (and `min_selected_amount` is 0).

```python
choices = comp.column_buttons()
# Output example : ["cheese", "peppers"]
```

---

## MultiSelectStyle reference

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `tick_on` | `str` | `"[x] "` | Prefix on a ticked button |
| `tick_off` | `str` | `"[ ] "` | Prefix on an unticked button |
| `min_selected_amount` | `int` | `0` | Minimum ticked count before Enter is accepted |
| `max_selected_amount` | `int` | `-1` | Maximum ticked count (`-1` = no limit) |
| `display_error` | `str \| None` | `None` | Inline message shown when bounds are not met |
| `select_keys` | `list[str]` | `[SPACE]` | Keys that toggle the highlighted button |

See the full API reference at [`MultiSelectStyle`](../api/button-style.md#interactive_buttons.MultiSelectStyle).

!!! warning "Error conditions"
    [`MultiSelectError`](../api/exceptions.md#interactive_buttons.MultiSelectError) is raised at `Component` construction time if `max_selected_amount` or `min_selected_amount` is greater than the number of buttons.
