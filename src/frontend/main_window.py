import tkinter as tk
from tkinter import filedialog, messagebox
from src.frontend.ui_manager import UIManager
from src.game_loader.rom_loader import ROMLoader


class MainWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("RetroEmuX")
        self.root.geometry("800x600")

        self.ui_manager = UIManager(self.root, self)
        self.rom_loader = ROMLoader()
        self.loaded_rom = None

        self.ui_manager.setup_ui()

    def load_game(self):
        """Открывает диалог выбора файла и загружает игру."""
        file_path = filedialog.askopenfilename(
            title="Выберите ROM-файл",
            filetypes=[("ROM Files", "*.bin;*.iso;*.rom;*.cue")]
        )

        if file_path and self.rom_loader.load_rom(file_path):
            self.loaded_rom = file_path
            messagebox.showinfo("Игра загружена", f"Файл {file_path} успешно загружен.")
            self.ui_manager.enable_start_button()
        else:
            messagebox.showerror("Ошибка", "Не удалось загрузить игру.")

    def start_emulation(self):
        """Имитация запуска эмуляции."""
        if self.loaded_rom:
            messagebox.showinfo("Эмуляция", f"Запуск игры: {self.loaded_rom}")
            self.ui_manager.enable_stop_button()
        else:
            messagebox.showerror("Ошибка", "Сначала загрузите игру.")

    def stop_emulation(self):
        """Имитация остановки эмуляции."""
        messagebox.showinfo("Эмуляция", "Эмуляция остановлена.")
        self.ui_manager.enable_start_button()

    def run(self):
        """Запускает главное окно."""
        self.root.mainloop()


if __name__ == "__main__":
    app = MainWindow()
    app.run()
