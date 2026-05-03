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
        configured key-bindings can be used (but not both at the same time).

        When ``multi_select`` is enabled on the component, the keys defined by
        [`select_keys`][interactive_buttons.MultiSelectStyle.select_keys] toggle
        the ticked state of the highlighted button, and ENTER returns the list
        of all ticked values once the
        [`min_selected_amount`][interactive_buttons.MultiSelectStyle.min_selected_amount]
        and
        [`max_selected_amount`][interactive_buttons.MultiSelectStyle.max_selected_amount]
        constraints are satisfied.

        :returns: The ``value`` of the button confirmed by the user, or the list
            of all ticked values when multi-select is enabled.
        :rtype: Any
        """
        host = require_buttons_kind_host(self)
        btn_count = len(host._buttons)
        host._size = btn_count
        y = 0
        error_message: str = ""

        def is_ticked(index: int) -> bool:
            if host._multi_select is None:
                return False
            return host._buttons[index].value in host._multi_select.selected

        def print_column(sel_y: int = 0, error: str = "") -> None:
            out = ""
            for i in range(btn_count):
                btn = host._buttons[i]
                out += host._build_button_style(
                    btn.label, i == sel_y, is_ticked(i), i, btn.local_button_style # type: ignore
                ) + "\n"
            if error:
                out += error + "\n"
            host._clear_lines(host._render_lines)
            host._render_lines = host._visual_lines(out)
            print(out, end="")

        def move(y: int) -> int:
            if y < 0:
                return btn_count - 1
            if y < btn_count:
                return y
            return 0

        def toggle(index: int) -> None:
            if host._multi_select is None:
                return
            value = host._buttons[index].value
            if value in host._multi_select.selected:
                host._multi_select.remove_from_selected(value) # type: ignore
                return
            max_amount = host._multi_select.max_selected_amount
            if max_amount == -1 or len(host._multi_select.selected) < max_amount:
                host._multi_select.add_to_selected(value)

        def validate_selection() -> bool:
            if host._multi_select is None:
                return True
            count = len(host._multi_select.selected)
            if count < host._multi_select.min_selected_amount:
                return False
            max_amount = host._multi_select.max_selected_amount
            if max_amount != -1 and count > max_amount:
                return False
            return True

        print_column(y)
        selected_value: Any = None

        while True:
            key = host._read_key()
            if error_message:
                error_message = ""

            if key == readchar.key.UP:
                y = move(y - 1)
                print_column(y)
            elif key == readchar.key.DOWN:
                y = move(y + 1)
                print_column(y)
            elif host._multi_select is not None and key in host._multi_select.select_keys:
                toggle(y)
                print_column(y)
            elif key == readchar.key.ENTER:
                if host._multi_select is not None:
                    if not validate_selection():
                        if host._multi_select.display_error is not None: # type: ignore
                            error_message = host._multi_select.display_error # type: ignore
                            print_column(y, error_message)
                        continue
                    selected_value = list(host._multi_select.selected)
                    break
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
                            if host._buttons[idx].key_bind_press_on_selection is True:
                                if host._multi_select is not None:
                                    toggle(y)
                                    print_column(y)
                                else:
                                    print_column(y)
                                    selected_value = host._buttons[y].value
                                    if host._auto_erase:
                                        host._clear_lines(host._render_lines)
                                    return selected_value
                            else:
                                print_column(y)
                    except AttributeError:
                        continue

        if host._auto_erase:
            host._clear_lines(host._render_lines)
        return selected_value
