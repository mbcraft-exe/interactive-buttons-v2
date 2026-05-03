# Component

`Component` is the central class of interactive-buttons.  It wraps a list of
[`Button`](button.md) instances and provides three layout methods that render
the buttons in the terminal, capture keyboard input, and return the selected
value.

---

## Class reference

::: interactive_buttons.Component
    options:
      members:
        - column_buttons
        - linear_buttons
        - matrix_buttons
        - erase_buttons
      show_root_heading: true
      show_source: false
      inherited_members: true

---

## Relationships

```
Component
+-- inherits -> LinearButtons   (provides linear_buttons)
+-- inherits -> ColumnButtons   (provides column_buttons)
+-- inherits -> MatrixButtons   (provides matrix_buttons)
```

All three layout classes share the same [`ButtonsKindHost`](../api/button.md)
protocol - `Component` satisfies it through its `__init__`.

---

## Component options

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `buttons` | `list[Button]` | — | Ordered list of buttons |
| `global_buttons_style` | `ButtonStyle` | `DEFAULT_STYLE` | Style applied to buttons without a local override |
| `multi_select` | `MultiSelectStyle \| None` | `None` | Enable multi-selection mode; layout methods return `list[Any]` |
| `display_index` | `bool` | `False` | Auto-prefix each button with a digit shortcut |
| `index_begin` | `int` | `1` | Starting digit when `display_index` is active |
| `auto_erase` | `bool` | `False` | Erase the rendered buttons automatically after selection |

---

## Error conditions

| Exception | When |
|-----------|------|
| [`MoreButtonsThanIndexes`](exceptions.md#interactive_buttons.MoreButtonsThanIndexes) | `display_index=True` and buttons exceed `10 - index_begin` |
| [`KeyBindError`](exceptions.md#interactive_buttons.KeyBindError) | `key_bind` used together with `display_index`, or duplicate keys |
| [`MultiSelectError`](exceptions.md#interactive_buttons.MultiSelectError) | `max_selected_amount` or `min_selected_amount` exceeds the number of buttons |
| [`EmulatedTerminalDetected`](exceptions.md#interactive_buttons.EmulatedTerminalDetected) | Terminal cannot provide raw keystroke input |
