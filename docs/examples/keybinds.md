# Key Binding Examples

[`ButtonKeyBind`](../api/button.md#interactive_buttons.ButtonKeyBind) lets you assign one or more hotkeys to a button. When the user presses a bound key the cursor jumps to that button, or immediately confirms it if `press_on_selection=True`.

!!! warning "Mutually exclusive with `display_index`"
    Key bindings and `display_index=True` cannot be used at the same time on the same `Component`. Combining them raises [`KeyBindError`](../api/exceptions.md#interactive_buttons.KeyBindError).

---

## Basic key binding

```python
from interactive_buttons import Button, ButtonKeyBind, Component, ButtonStyle, HACKER_STYLE

save_bind = ButtonKeyBind(b_keys=["s", "1"])
quit_bind = ButtonKeyBind(b_keys=["q", "2"])

buttons = [
    Button(label="Save",  value="save",  key_bind=save_bind),
    Button(label="Quit",  value="quit",  key_bind=quit_bind),
]

comp   = Component(buttons, global_buttons_style=ButtonStyle(**HACKER_STYLE))
choice = comp.column_buttons()
```

Pressing `s`, `S` or `1` jumps the cursor to **Save** or `q`, `Q` or `2` jumps to **Quit**.  The user still needs to press **Enter** to confirm.

---

## Instant-confirm on key press

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

!!! tip
    This pattern is ideal for quick `Y/N` prompts where you want single-key responses.

---

## Case-sensitive keys

By default, key matching is not **case-sensitive**, both `a` and `A` trigger the same binding.

Set `case_sensitive=True` to distinguish between them:

```python
lower_bind = ButtonKeyBind(b_keys=["a"], case_sensitive=True)
upper_bind = ButtonKeyBind(b_keys=["A"], case_sensitive=True)

buttons = [
    Button(label="Option a (lowercase only)", value="a_lower", key_bind=lower_bind),
    Button(label="Option A (uppercase only)", value="a_upper", key_bind=upper_bind),
]

comp   = Component(buttons)
choice = comp.column_buttons()
```

---

## Multiple keys per button

`b_keys` is a list, so a single button can respond to several hotkeys:

```python
nav_bind = ButtonKeyBind(b_keys=["h", "b", "1"])  # h, b, or 1 all jump here

buttons = [
    Button(label="Home", value="home", key_bind=nav_bind),
    Button(label="Exit", value="exit"),
]
```

---

## Accepted key characters

Each entry in `b_keys` must be a **single ASCII alphanumeric character** (`A-Z`, `a-z`, `0-9`) or a **space** (`' '`). Anything else raises [`KeyBindError`](../api/exceptions.md#interactive_buttons.KeyBindError) at construction time.

```python
# [v] Valid
ButtonKeyBind(b_keys=["a", "1", "Z"])

# [v] Valid — space is an accepted character
ButtonKeyBind(b_keys=[" "])

# [x] Raises KeyBindError, multi-character string
ButtonKeyBind(b_keys=["ab"])

# [x] Raises KeyBindError, non-ASCII character
ButtonKeyBind(b_keys=["é"])
```

---

## No duplicate keys across buttons

Each bound key must be unique across all buttons in a `Component`.  Assigning
the same key to two different buttons raises [`KeyBindError`](../api/exceptions.md#interactive_buttons.KeyBindError) when the `Component` is constructed:

```python
bind_a = ButtonKeyBind(b_keys=["a"])
bind_b = ButtonKeyBind(b_keys=["a"])   # duplicate!

buttons = [
    Button(label="Alpha", value="alpha", key_bind=bind_a),
    Button(label="Beta",  value="beta",  key_bind=bind_b),
]

# Raises: KeyBindError: Duplicate key accross two differents buttons.
comp = Component(buttons)
```
