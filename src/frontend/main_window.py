import tkinter as tk
from .ui_manager import UIManager


class MainWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("RetroEmuX")
        self.root.geometry("800x600")

        self.ui_manager = UIManager(self.root)
        self.ui_manager.setup_ui()

    def run(self):
        """Запускает главное окно."""
        self.root.mainloop()


if __name__ == "__main__":
    app = MainWindow()
    app.run()
