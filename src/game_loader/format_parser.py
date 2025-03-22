import os


class FormatParser:
    SUPPORTED_FORMATS = [".bin", ".iso", ".rom", ".cue"]

    @staticmethod
    def is_supported_format(file_path):
        """Проверяет, поддерживается ли данный формат файла."""
        return any(file_path.endswith(ext) for ext in FormatParser.SUPPORTED_FORMATS)

    @staticmethod
    def get_file_extension(file_path):
        """Возвращает расширение файла."""
        return os.path.splitext(file_path)[-1].lower()

    @staticmethod
    def parse_file(file_path):
        """Анализирует заголовок файла для определения его типа."""
        if not os.path.exists(file_path):
            print("Ошибка: Файл не найден.")
            return None

        ext = FormatParser.get_file_extension(file_path)

        if ext in [".bin", ".iso", ".rom"]:
            return FormatParser.read_binary_header(file_path)
        elif ext == ".cue":
            return FormatParser.parse_cue_file(file_path)
        else:
            print("Ошибка: Неподдерживаемый формат файла.")
            return None

    @staticmethod
    def read_binary_header(file_path):
        """Читает заголовок бинарного ROM-файла и определяет его тип."""
        try:
            with open(file_path, "rb") as file:
                header = file.read(16)  # Читаем первые 16 байт для анализа

                # Проверяем заголовок на соответствие известным форматам
                if header[:4] == b"SEGA":
                    print("Обнаружен ROM Sega Mega Drive / Genesis.")
                    return "Sega Mega Drive"
                elif header[:4] == b"PS-X":
                    print("Обнаружен ROM Sony PlayStation.")
                    return "Sony PlayStation"
                elif header[:4] == b"CD00":
                    print("Обнаружен диск Dreamcast.")
                    return "Sega Dreamcast"
                else:
                    print("Неизвестный формат ROM.")
                    return "Unknown"
        except Exception as e:
            print(f"Ошибка при чтении заголовка: {e}")
            return None

    @staticmethod
    def parse_cue_file(file_path):
        """Парсит CUE-файл и извлекает список связанных BIN-файлов."""
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                lines = file.readlines()

            bin_files = [line.split('"')[1] for line in lines if "FILE" in line and '"' in line]

            if bin_files:
                print(f"CUE-файл {file_path} содержит BIN-файлы: {bin_files}")
                return {"cue_file": file_path, "bin_files": bin_files}
            else:
                print(f"CUE-файл {file_path} не содержит ссылок на BIN-файлы.")
                return None
        except Exception as e:
            print(f"Ошибка при разборе CUE-файла: {e}")
            return None
