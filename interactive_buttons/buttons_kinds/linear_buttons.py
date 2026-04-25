from __future__ import annotations
from typing import Any
import readchar

from .contracts import (  # type: ignore[reportMissingImports]
    ButtonsKindHost,
    require_buttons_kind_host,
)


class LinearButtons:
    def linear_buttons(self: ButtonsKindHost) -> Any:
        """Display buttons in a horizontal row and return the selected value.

        Renders all buttons side by side on a single line. The user navigates with
        LEFT/RIGHT arrow keys and confirms with ENTER. When ``display_index`` is
        enabled, pressing the corresponding digit jumps to that button, otherwise
        configured key-bindings can be used (butr not both at the same time).

        :returns: The ``value`` of the button confirmed by the user, this value can be anything.
        :rtype: Any
        """
        host = require_buttons_kind_host(self)
        btn_count = len(host._buttons)
        host._size = 1
        x = 0

        def print_linear(sel_x: int = 0) -> None:
            max_len = max(len(b.label) for b in host._buttons)
            col_width = max_len + host._global_buttons_style.spaces_count
            out = ""
            for idx in range(btn_count):
                btn = host._buttons[idx]
                out += host._build_button_style(
                    btn.label, idx == sel_x, idx, btn.local_button_style
                )
                style = btn.local_button_style or host._global_buttons_style
                dec_len = len(style.left_decorator) + len(style.right_decorator)
                out += " " * max(0, col_width - len(btn.label) - dec_len)
            out += "\n"
            host._clear_lines(host._render_lines)
            host._render_lines = host._visual_lines(out)
            print(out, end="")

        def move(x: int) -> int:
            if x < 0:
                return btn_count - 1
            if x < btn_count:
                return x
            return 0

        print_linear(x)
        selected_value: Any = None

        while True:
            key = host._read_key()

            if key == readchar.key.RIGHT:
                x = move(x + 1)
                print_linear(x)
            elif key == readchar.key.LEFT:
                x = move(x - 1)
                print_linear(x)
            elif key == readchar.key.ENTER:
                selected_value = host._buttons[x].value
                break
            elif host._display_index:
                key_num = host._try_int(key)
                if key_num is None:
                    continue
                for idx in range(btn_count):
                    if idx + host._index_begin == key_num:
                        x = idx
                        print_linear(x)
            else:
                for idx in range(btn_count):
                    try:
                        if host._buttons[idx].key_bind_case_sensitive is True:
                            ks = host._buttons[idx].key_bind_keys
                            k = key
                        else:
                            k = key.upper()
                            ks = [s.upper() for s in host._buttons[idx].key_bind_keys] # type: ignore
                        if k in ks: # type: ignore
                            x = idx
                            print_linear(x)
                            if host._buttons[idx].key_bind_press_on_selection is True:
                                selected_value = host._buttons[x].value
                                if host._auto_erase:
                                    host._clear_lines(host._render_lines)
                                return selected_value
                    except AttributeError:
                        continue

        if host._auto_erase:
            host._clear_lines(host._render_lines)
        return selected_value
