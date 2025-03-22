import tkinter as tk
from tkinter import filedialog, messagebox

class UIManager:
    def __init__(self, root):
        self.root = root

    def setup_ui(self):
        """Создает интерфейс пользователя."""
        frame = tk.Frame(self.root, padx=10, pady=10)
        frame.pack(expand=True)

        self.load_button = tk.Button(frame, text="Загрузить игру", command=self.load_game)
        self.load_button.pack(pady=5)

        self.start_button = tk.Button(frame, text="Запустить", command=self.start_emulation, state=tk.DISABLED)
        self.start_button.pack(pady=5)

        self.stop_button = tk.Button(frame, text="Остановить", command=self.stop_emulation, state=tk.DISABLED)
        self.stop_button.pack(pady=5)

    def load_game(self):
        """Выбирает игру для загрузки."""
        file_path = filedialog.askopenfilename(title="Выберите ROM-файл",
                                               filetypes=[("ROM Files", "*.bin;*.iso;*.rom")])
        if file_path:
            messagebox.showinfo("Игра загружена", f"Файл {file_path} загружен.")
            self.start_button.config(state=tk.NORMAL)

    def start_emulation(self):
        """Запускает эмуляцию (заглушка)."""
        messagebox.showinfo("Эмуляция", "Эмуляция запущена.")
        self.stop_button.config(state=tk.NORMAL)
        self.start_button.config(state=tk.DISABLED)

    def stop_emulation(self):
        """Останавливает эмуляцию (заглушка)."""
        messagebox.showinfo("Эмуляция", "Эмуляция остановлена.")
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
