from __future__ import annotations

from typing import Any, Protocol, cast

from ..button import Button
from ..button_style import ButtonStyle


class ButtonsKindHost(Protocol):
    _buttons: list[Button]
    _global_buttons_style: ButtonStyle
    _display_index: bool
    _index_begin: int
    _auto_erase: bool
    _size: int
    _render_lines: int

    @staticmethod
    def _visual_lines(text: str) -> int: ...

    @staticmethod
    def _clear_lines(n: int = 1) -> None: ...

    @staticmethod
    def _read_key() -> str: ...

    @staticmethod
    def _try_int(key: str | None) -> int | None: ...

    def _build_button_style(
        self,
        label: str,
        selected: bool = False,
        index: int = 0,
        local_style: ButtonStyle | None = None,
    ) -> str: ...


_REQUIRED_HOST_MEMBERS = (
    "_buttons",
    "_global_buttons_style",
    "_display_index",
    "_index_begin",
    "_auto_erase",
    "_size",
    "_render_lines",
    "_visual_lines",
    "_clear_lines",
    "_read_key",
    "_try_int",
    "_build_button_style",
)


def require_buttons_kind_host(instance: object) -> ButtonsKindHost:
    missing = [name for name in _REQUIRED_HOST_MEMBERS if not hasattr(instance, name)]
    if missing:
        members = ", ".join(sorted(missing))
        raise TypeError(
            "Button kind mixins require a host implementing ButtonsKindHost; "
            f"missing members: {members}."
        )
    return cast(ButtonsKindHost, instance)
