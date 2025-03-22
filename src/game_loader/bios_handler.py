import os


class BIOSHandler:
    REQUIRED_BIOS = {
        "ps1": "scph1001.bin",
        "ps2": "scph39001.bin",
        "dreamcast": "dc_boot.bin"
    }

    def __init__(self, bios_directory="bios/"):
        self.bios_directory = bios_directory
        self.loaded_bios = {}

    def load_bios(self, system):
        """Загружает BIOS для указанной системы."""
        bios_file = os.path.join(self.bios_directory, self.REQUIRED_BIOS.get(system, ""))

        if os.path.exists(bios_file):
            self.loaded_bios[system] = bios_file
            print(f"BIOS {bios_file} загружен для {system}.")
            return True
        else:
            print(f"BIOS {system} не найден.")
            return False

    def get_loaded_bios(self, system):
        """Возвращает путь к загруженному BIOS-файлу."""
        return self.loaded_bios.get(system)
