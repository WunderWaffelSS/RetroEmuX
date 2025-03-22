import os

class ROMLoader:
    def __init__(self):
        self.loaded_rom = None

    def load_rom(self, file_path):
        """Загружает ROM-файл."""
        if os.path.exists(file_path) and file_path.endswith((".bin", ".iso", ".rom")):
            self.loaded_rom = file_path
            print(f"ROM {file_path} загружен.")
            return True
        else:
            print("Ошибка загрузки ROM-файла.")
            return False

    def get_loaded_rom(self):
        """Возвращает путь к загруженному ROM-файлу."""
        return self.loaded_rom
