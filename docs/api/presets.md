# Style Presets

interactive-buttons ships 12 built-in style presets as module-level
dictionaries.  Import the one you want and unpack it into
[`ButtonStyle`](button-style.md):

```python
from interactive_buttons import ButtonStyle, HACKER_STYLE

style = ButtonStyle(**HACKER_STYLE)
```

---

## Preset catalogue

### `DEFAULT_STYLE`

> Classic bracketed buttons - dark text on a white background when selected.

```python
from interactive_buttons import ButtonStyle, DEFAULT_STYLE

style = ButtonStyle(**DEFAULT_STYLE)
```

```text
[ Option A ]   [ Option B ]   <- selected button: black text, white background
```

| Key | Value |
|-----|-------|
| `text_color` | `\033[30m` - black |
| `highlight_color` | `\033[47m` - white background |
| `spaces_count` | 5 |
| `left_decorator` | `[` |
| `right_decorator` | `]` |

---

### `HACKER_STYLE`

> Minimal green-on-black arrow style - no background highlight.

```python
from interactive_buttons import ButtonStyle, HACKER_STYLE
```

```text
> Option A      Option B
```

| Key | Value |
|-----|-------|
| `text_color` | `\033[32m` - green |
| `highlight_color` | *(empty)* |
| `spaces_count` | 5 |
| `left_decorator` | `> ` |
| `right_decorator` | *(empty)* |

---

### `MINIMAL_STYLE`

> Underline-only highlight - no color, no decorators.

```python
from interactive_buttons import ButtonStyle, MINIMAL_STYLE
```

```text
<u>Option A</u>   Option B
```

| Key | Value |
|-----|-------|
| `text_color` | *(empty)* |
| `highlight_color` | `\033[4m` - underline |
| `spaces_count` | 3 |
| `left_decorator` | *(empty)* |
| `right_decorator` | *(empty)* |

---

### `MONOCHROME_STYLE`

> Reversed-video highlight - white text, no decorators.

| Key | Value |
|-----|-------|
| `text_color` | `\033[37m` - white |
| `highlight_color` | `\033[7m` - reverse video |
| `spaces_count` | 4 |
| `left_decorator` | *(empty)* |
| `right_decorator` | *(empty)* |

---

### `CORPORATE_STYLE`

> Blue bracketed buttons - bold white text on a blue background when selected.

| Key | Value |
|-----|-------|
| `text_color` | `\033[34m` - blue |
| `highlight_color` | `\033[1;44;97m` - bold, blue background, bright white text |
| `spaces_count` | 4 |
| `left_decorator` | `[` |
| `right_decorator` | `]` |

---

### `TERMINAL_RETRO_STYLE`

> Amber retro style - yellow text with a diamond `*` prefix.

| Key | Value |
|-----|-------|
| `text_color` | `\033[33m` - yellow |
| `highlight_color` | `\033[43;30m` - yellow background, black text |
| `spaces_count` | 4 |
| `left_decorator` | `* ` |
| `right_decorator` | *(empty)* |

---

### `MATRIX_STYLE`

> Bold green on black - square bracket decorators, Matrix-movie aesthetic.

| Key | Value |
|-----|-------|
| `text_color` | `\033[32m` - green |
| `highlight_color` | `\033[1;32;40m` - bold green, black background |
| `spaces_count` | 3 |
| `left_decorator` | `[ ` |
| `right_decorator` | ` ]` |

---

### `CYBERPUNK_STYLE`

> Blue text with amber highlight - French guillemet decorators.

| Key | Value |
|-----|-------|
| `text_color` | `\033[34m` - blue |
| `highlight_color` | `\033[43;30m` - yellow background, black text |
| `spaces_count` | 4 |
| `left_decorator` | `<< ` |
| `right_decorator` | ` >>` |

---

### `DANGER_STYLE`

> Red alert - bold white on red background, warning `!/!` prefix.

```python
from interactive_buttons import ButtonStyle, DANGER_STYLE
```

```text
/!\ Delete    /!\ Reset
```

| Key | Value |
|-----|-------|
| `text_color` | `\033[91m` - bright red |
| `highlight_color` | `\033[1;41;97m` - bold, red background, bright white |
| `spaces_count` | 3 |
| `left_decorator` | `/!\\ ` |
| `right_decorator` | ` ` |

---

### `SUCCESS_STYLE`

> Bright green confirmation style - checkmark `[v]` prefix.

```text
[v] Save    [v] Continue
```

| Key | Value |
|-----|-------|
| `text_color` | `\033[92m` - bright green |
| `highlight_color` | `\033[1;42;30m` - bold, green background, black text |
| `spaces_count` | 3 |
| `left_decorator` | `[v] ` |
| `right_decorator` | *(empty)* |

---

### `SUNSET_STYLE`

> Warm amber with magenta highlight - chevron wrap decorators.

```text
> Option A <    Option B
```

| Key | Value |
|-----|-------|
| `text_color` | `\033[33m` - yellow |
| `highlight_color` | `\033[1;45;93m` - bold, magenta background, bright yellow |
| `spaces_count` | 4 |
| `left_decorator` | `> ` |
| `right_decorator` | ` <` |

---

### `GHOST_STYLE`

> Dim white text, bold on selection - invisible until focused.

| Key | Value |
|-----|-------|
| `text_color` | `\033[2;37m` - dim white |
| `highlight_color` | `\033[1;37m` - bold bright white |
| `spaces_count` | 4 |
| `left_decorator` | *(empty)* |
| `right_decorator` | *(empty)* |

---

## Module-level autodoc

::: interactive_buttons.button_styles_presets
    options:
      show_root_heading: true
      show_source: false
      members:
        - DEFAULT_STYLE
        - HACKER_STYLE
        - MINIMAL_STYLE
        - MONOCHROME_STYLE
        - CORPORATE_STYLE
        - TERMINAL_RETRO_STYLE
        - MATRIX_STYLE
        - CYBERPUNK_STYLE
        - DANGER_STYLE
        - SUCCESS_STYLE
        - SUNSET_STYLE
        - GHOST_STYLE
