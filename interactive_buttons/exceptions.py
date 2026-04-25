"""Exceptions raised by the interactive-buttons library."""


class MoreButtonsThanIndexes(Exception):
    """Raised when the number of buttons exceeds the available digit indexes.

    This happens when [`display_index`][interactive_buttons.Component.display_index] is
    ``True`` and the number of buttons is greater than ``10 - index_begin``.
    """


class EmulatedTerminalDetected(Exception):
    """Raised when the terminal cannot support raw keyboard input.

    interactive-buttons relies on `readchar` to capture individual
    keystrokes.  Emulated terminals (e.g. the integrated terminal inside some
    IDEs) may not expose a real TTY and will trigger this exception.  Run your
    programme in a proper terminal emulator (bash, zsh, PowerShell, etc.).
    """


class KeyBindError(Exception):
    """Raised for invalid or conflicting key-binding configuration.

    Possible causes:

    - A key in [`b_keys`][interactive_buttons.ButtonKeyBind.b_keys] is not a
      single ASCII alphanumeric character.
    - Both ``key_bind`` and ``display_index`` are active at the same time.
    - Two different buttons share the same bound key.
    """
