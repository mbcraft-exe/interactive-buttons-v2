# ButtonStyle

`ButtonStyle` defines the visual appearance of buttons: text color,
selection highlight, padding, and prefix/suffix decorators.

Pass a style to [`Component`](component.md) as `global_buttons_style`, or
to an individual [`Button`](button.md) as `local_button_style`.

---

## Class reference

::: interactive_buttons.ButtonStyle
    options:
      show_root_heading: true
      show_source: false
      members:
        - text_color
        - highlight_color
        - spaces_count
        - left_decorator
        - right_decorator

---

## How a button is rendered

```
{index}  {left_decorator}{spaces}{label}{spaces}{right_decorator}
```

When the button is **selected**, `text_color` and `highlight_color` are prepended and a reset sequence is appended.

Example with `CORPORATE_STYLE`:

```text
[ Option A ]   <- unselected (blue text, no background)
[ Option B ]   <- selected   (bold white text, blue background)
```

---

## Using colorama

```python
from colorama import Fore, Back
from interactive_buttons import ButtonStyle

ocean_style = ButtonStyle(
    text_color=Fore.CYAN,
    highlight_color=Back.BLUE,
    spaces_count=4,
    left_decorator="~~",
    right_decorator="~~",
)
```

---

## Using raw ANSI codes

```python
from interactive_buttons import ButtonStyle

ocean_style = ButtonStyle(
    text_color="\033[36m",     # cyan
    highlight_color="\033[44m",  # blue background
    spaces_count=4,
    left_decorator="~~",
    right_decorator="~~",
)
```

!!! note "`spaces_count` minimum"
    The constructor enforces a minimum value of **2** for `spaces_count`.
    Values below 2 are silently raised to 2.

---

---

## MultiSelectStyle

`MultiSelectStyle` enables multi-selection mode on a `Component`. Pass an instance as the `multi_select` argument. The layout methods then return a `list` of values instead of a single value.

::: interactive_buttons.MultiSelectStyle
    options:
      show_root_heading: true
      show_source: false
      members:
        - tick_on
        - tick_off
        - min_selected_amount
        - max_selected_amount
        - display_error
        - select_keys
        - selected

---

## Pre-built presets

Rather than building a `ButtonStyle` from scratch, you can use one of the
[12 built-in presets](presets.md).

```python
from interactive_buttons import ButtonStyle, SUNSET_STYLE

style = ButtonStyle(**SUNSET_STYLE)
```
