# Button & ButtonKeyBind

## Button

A single selectable item. Provide a `label` (displayed text) and a `value`
(returned when the button is confirmed). Optionally attach a
[`ButtonKeyBind`](#interactive_buttons.ButtonKeyBind) and a per-button
[`ButtonStyle`](button-style.md) override.

::: interactive_buttons.Button
    options:
      show_root_heading: true
      show_source: false
      members:
        - label
        - value
        - local_button_style

---

## ButtonKeyBind

Keyboard shortcut configuration for a single `Button`.

::: interactive_buttons.ButtonKeyBind
    options:
      show_root_heading: true
      show_source: false
      members:
        - b_keys
        - case_sensitive
        - press_on_selection

---

## Quick reference

```python
from interactive_buttons import Button, ButtonKeyBind

# Bind keys "y" and "Y"; instant-confirm on press
yes_bind = ButtonKeyBind(
    b_keys=["y"],
    press_on_selection=True,   # confirm without pressing Enter
    case_sensitive=False,      # y and Y both match (default)
)

btn = Button(
    label="Yes",
    value=True,
    key_bind=yes_bind,
)
```

| Rule | Detail |
|------|--------|
| `b_keys` entries | Single ASCII alphanumeric characters only (`A-Z`, `a-z`, `0-9`) |
| Duplicate keys | Not allowed across buttons in the same `Component` |
| `display_index` | Cannot be combined with `key_bind` |
