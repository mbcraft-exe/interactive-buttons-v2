from __future__ import annotations
from typing import Any
import readchar

from .contracts import (  # type: ignore[reportMissingImports]
    ButtonsKindHost,
    require_buttons_kind_host,
)


class MatrixButtons:

    def matrix_buttons(self: ButtonsKindHost) -> Any:
        """Display buttons in a square grid and return the selected value.

        Arranges buttons in a square grid of side length. The user navigates
        with arrow keys and confirms with ENTER. When ``display_index`` is
        enabled, pressing the corresponding digit jumps to that button, otherwise
        configured key-bindings can be used (butr not both at the same time).

        :returns: The ``value`` of the button confirmed by the user, this value can be anything.
        :rtype: Any
        """
        host = require_buttons_kind_host(self)
        btn_count = len(host._buttons)
        import math
        grid_size = math.ceil(math.sqrt(btn_count))
        host._size = grid_size
        x, y = 0, 0

        def print_matrix(sel_x: int = 0, sel_y: int = 0) -> None:
            max_len = max(len(b.label) for b in host._buttons)
            col_width = max_len + host._global_buttons_style.spaces_count
            out = ""
            for j in range(grid_size):
                for i in range(grid_size):
                    idx = j * grid_size + i
                    if idx >= btn_count:
                        break
                    btn = host._buttons[idx]
                    out += host._build_button_style(
                        btn.label, (i, j) == (sel_x, sel_y),
                        idx,
                        btn.local_button_style
                    )
                    style = btn.local_button_style or host._global_buttons_style
                    dec_len = len(style.left_decorator) + len(style.right_decorator)
                    out += " " * max(0, col_width - len(btn.label) - dec_len)
                out += "\n"
            host._clear_lines(host._render_lines)
            host._render_lines = host._visual_lines(out)
            print(out, end="")

        def move(x: int, y: int, dx: int, dy: int) -> tuple[int, int]:
            x = (x + dx) % grid_size
            y = (y + dy) % grid_size
            idx = y * grid_size + x
            if idx < btn_count:
                return x, y
            return 0, 0

        print_matrix(x, y)
        selected_value: Any = None

        while True:
            key = host._read_key()

            if key == readchar.key.RIGHT:
                x, y = move(x, y, 1, 0)
                print_matrix(x, y)
            elif key == readchar.key.LEFT:
                x, y = move(x, y, -1, 0)
                print_matrix(x, y)
            elif key == readchar.key.UP:
                x, y = move(x, y, 0, -1)
                print_matrix(x, y)
            elif key == readchar.key.DOWN:
                x, y = move(x, y, 0, 1)
                print_matrix(x, y)
            elif key == readchar.key.ENTER:
                selected_value = host._buttons[y * grid_size + x].value
                break
            elif host._display_index:
                key_num = host._try_int(key)
                if key_num is None:
                    continue
                for j in range(grid_size):
                    for i in range(grid_size):
                        idx = j * grid_size + i
                        if idx < btn_count and idx + host._index_begin == key_num:
                            x, y = i, j
                            print_matrix(x, y)
            else:
                for j in range(grid_size):
                    for i in range(grid_size):
                        idx = j * grid_size + i
                        try:
                            if host._buttons[idx].key_bind_case_sensitive is True:
                                ks = host._buttons[idx].key_bind_keys
                                k = key
                            else:
                                k = key.upper()
                                ks = [s.upper() for s in host._buttons[idx].key_bind_keys] # type: ignore
                            if k in ks: # type: ignore
                                x, y = i, j
                                print_matrix(x, y)
                                if host._buttons[idx].key_bind_press_on_selection is True:
                                    selected_value = host._buttons[y * grid_size + x].value
                                    if host._auto_erase:
                                        host._clear_lines(host._render_lines)
                                    return selected_value
                        except AttributeError:
                            continue

        if host._auto_erase:
            host._clear_lines(host._render_lines)
        return selected_value
