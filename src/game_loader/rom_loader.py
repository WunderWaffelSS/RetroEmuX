import os
import hashlib
import json

class ROMLoader:
    SUPPORTED_FORMATS = [".bin", ".iso", ".rom", ".cue"]
    HISTORY_FILE = "rom_history.json"

    def __init__(self):
        self.loaded_rom = None
        self.rom_size = 0
        self.rom_hash = None
        self.load_history()

    def is_supported_format(self, file_path):
        """Проверяет, поддерживается ли данный формат файла."""
        return any(file_path.endswith(ext) for ext in self.SUPPORTED_FORMATS)

    def calculate_hash(self, file_path):
        """Вычисляет SHA-1 хеш загруженного ROM-файла."""
        sha1 = hashlib.sha1()
        try:
            with open(file_path, "rb") as f:
                while chunk := f.read(8192):
                    sha1.update(chunk)
            return sha1.hexdigest()
        except FileNotFoundError:
            return None

    def load_rom(self, file_path):
        """Загружает ROM-файл, проверяет его формат и вычисляет хеш."""
        if not os.path.exists(file_path):
            print("Ошибка: Файл не найден.")
            return False

        if not self.is_supported_format(file_path):
            print("Ошибка: Неподдерживаемый формат файла.")
            return False

        self.loaded_rom = file_path
        self.rom_size = os.path.getsize(file_path)
        self.rom_hash = self.calculate_hash(file_path)

        print(f"ROM {file_path} загружен. Размер: {self.rom_size} байт.")
        print(f"SHA-1 Хеш: {self.rom_hash}")

        self.add_to_history(file_path)

        return True

    def add_to_history(self, file_path):
        """Добавляет загруженный ROM в историю."""
        history = self.get_history()
        if file_path not in history:
            history.append(file_path)

        with open(self.HISTORY_FILE, "w") as file:
            json.dump(history[-5:], file, indent=4)  # Храним последние 5 игр

    def load_history(self):
        """Создаёт файл истории, если он отсутствует."""
        if not os.path.exists(self.HISTORY_FILE):
            with open(self.HISTORY_FILE, "w") as file:
                json.dump([], file)

    def get_history(self):
        """Возвращает список последних загруженных ROM-файлов."""
        try:
            with open(self.HISTORY_FILE, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def get_loaded_rom_info(self):
        """Возвращает информацию о загруженном ROM."""
        return {
            "path": self.loaded_rom,
            "size": self.rom_size,
            "hash": self.rom_hash
        } if self.loaded_rom else None
