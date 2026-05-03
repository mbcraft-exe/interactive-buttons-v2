# Exceptions

All exceptions live in `interactive_buttons.exceptions` and are re-exported
from the top-level `interactive_buttons` package.

```python
from interactive_buttons import (
    EmulatedTerminalDetected,
    MoreButtonsThanIndexes,
    KeyBindError,
    MultiSelectError,
)
```

---

::: interactive_buttons.EmulatedTerminalDetected
    options:
      show_root_heading: true
      show_source: false

---

::: interactive_buttons.MoreButtonsThanIndexes
    options:
      show_root_heading: true
      show_source: false

---

::: interactive_buttons.KeyBindError
    options:
      show_root_heading: true
      show_source: false

---

::: interactive_buttons.MultiSelectError
    options:
      show_root_heading: true
      show_source: false

---

## When each exception is raised

| Exception | Raised by | Condition |
|-----------|-----------|-----------|
| `EmulatedTerminalDetected` | Any layout method | Terminal cannot provide raw keystroke input (e.g. IDE integrated terminal) |
| `MoreButtonsThanIndexes` | `Component.__init__` | `display_index=True` and `len(buttons) > 10 - index_begin` |
| `KeyBindError` | `ButtonKeyBind.__init__`, `Component.__init__` | Invalid key character, `key_bind` + `display_index` conflict, or duplicate keys |
| `MultiSelectError` | `Component.__init__` | `max_selected_amount` or `min_selected_amount` exceeds the number of buttons |

---

## Handling exceptions

```python
from interactive_buttons import (
    Button, Component,
    EmulatedTerminalDetected,
    KeyBindError,
    MultiSelectError,
)

try:
    comp   = Component([Button(label="OK", value=True)])
    result = comp.column_buttons()
except EmulatedTerminalDetected:
    print("Please run this script in a real terminal, not inside an IDE.")
except KeyBindError as exc:
    print(f"Key binding configuration error: {exc}")
except MultiSelectError as exc:
    print(f"Multi-select configuration error: {exc}")
```
