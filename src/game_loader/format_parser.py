class FormatParser:
    SUPPORTED_FORMATS = [".bin", ".iso", ".rom", ".cue"]

    @staticmethod
    def is_supported_format(file_path):
        """Проверяет, поддерживается ли данный формат файла."""
        return any(file_path.endswith(ext) for ext in FormatParser.SUPPORTED_FORMATS)

    @staticmethod
    def get_file_extension(file_path):
        """Возвращает расширение файла."""
        return file_path.split(".")[-1] if "." in file_path else ""

    @staticmethod
    def parse_file(file_path):
        """Имитация разбора файла (заглушка)."""
        if FormatParser.is_supported_format(file_path):
            print(f"Файл {file_path} успешно распознан.")
            return True
        else:
            print("Неподдерживаемый формат файла.")
            return False
