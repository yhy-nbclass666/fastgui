"""
Core module:
    Windows class.
"""

from .imports import _Core, _Wid
import sys

class Window:
    """
    Main window for GUI applications.

    Example:
        >>> from fastgui import Window
        >>> window = Window()
        >>> window.run()
        >>> # Then you can see a window!
    """

    def __init__(self) -> None:
        """Initialize the main window."""
        self.app = _Wid.QApplication(sys.argv)

        self.window = _Wid.QWidget()

    def run(self) -> None:
        """Show the main window and enter the main loop."""
        self.window.show()
        sys.exit(self.app.exec())