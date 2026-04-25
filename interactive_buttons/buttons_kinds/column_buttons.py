from __future__ import annotations
from typing import Any
import readchar

from .contracts import (  # type: ignore[reportMissingImports]
    ButtonsKindHost,
    require_buttons_kind_host,
)


class ColumnButtons:

    def column_buttons(self: ButtonsKindHost) -> Any:
        """Display buttons in a vertical column and return the selected value.

        Renders all buttons stacked vertically. The user navigates with the
        UP/DOWN arrow keys and confirms with ENTER. When ``display_index`` is
        enabled, pressing the corresponding digit jumps to that button, otherwise
        configured key-bindings can be used (butr not both at the same time).

        :returns: The ``value`` of the button confirmed by the user, this value can be anything.
        :rtype: Any
        """
        host = require_buttons_kind_host(self)
        btn_count = len(host._buttons)
        host._size = btn_count
        y = 0

        def print_column(sel_y: int = 0) -> None:
            out = ""
            for i in range(btn_count):
                btn = host._buttons[i]
                out += host._build_button_style(btn.label, i == sel_y, i, btn.local_button_style) + "\n"
            host._clear_lines(host._render_lines)
            host._render_lines = host._visual_lines(out)
            print(out, end="")

        def move(y: int) -> int:
            if y < 0:
                return btn_count - 1
            if y < btn_count:
                return y
            return 0

        print_column(y)
        selected_value: Any = None

        while True:
            key = host._read_key()

            if key == readchar.key.UP:
                y = move(y - 1)
                print_column(y)
            elif key == readchar.key.DOWN:
                y = move(y + 1)
                print_column(y)
            elif key == readchar.key.ENTER:
                selected_value = host._buttons[y].value
                break
            elif host._display_index:
                key_num = host._try_int(key)
                if key_num is None:
                    continue
                for idx in range(btn_count):
                    if idx + host._index_begin == key_num:
                        y = idx
                        print_column(y)
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
                            y = idx
                            print_column(y)
                            if host._buttons[idx].key_bind_press_on_selection is True:
                                selected_value = host._buttons[y].value
                                if host._auto_erase:
                                    host._clear_lines(host._render_lines)
                                return selected_value
                    except AttributeError:
                        continue

        if host._auto_erase:
            host._clear_lines(host._render_lines)
        return selected_value
