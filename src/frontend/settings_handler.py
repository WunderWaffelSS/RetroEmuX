import json
import os

class SettingsHandler:
    SETTINGS_FILE = "settings.json"

    def __init__(self):
        self.settings = {
            "resolution": "640x480",
            "fullscreen": False,
            "volume": 50
        }
        self.load_settings()

    def load_settings(self):
        """Загружает настройки из файла."""
        if os.path.exists(self.SETTINGS_FILE):
            with open(self.SETTINGS_FILE, "r") as file:
                self.settings.update(json.load(file))

    def save_settings(self):
        """Сохраняет настройки в файл."""
        with open(self.SETTINGS_FILE, "w") as file:
            json.dump(self.settings, file, indent=4)

    def set_setting(self, key, value):
        """Изменяет параметр настройки."""
        if key in self.settings:
            self.settings[key] = value
            self.save_settings()

    def get_setting(self, key):
        """Получает параметр настройки."""
        return self.settings.get(key)
