class MemoryManager:
    def __init__(self, size=1024 * 1024):  # 1MB памяти по умолчанию
        self.memory = bytearray(size)

    def read(self, address, size=1):
        """Читает данные из памяти."""
        return self.memory[address:address + size]

    def write(self, address, data):
        """Записывает данные в память."""
        self.memory[address:address + len(data)] = data

    def reset(self):
        """Очищает всю память."""
        self.memory = bytearray(len(self.memory))
        print("Memory reset complete.")
