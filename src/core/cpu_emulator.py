class CPUEmulator:
    def __init__(self):
        self.registers = [0] * 32  # Пример 32 регистра
        self.pc = 0  # Программный счетчик

    def execute_instruction(self, instruction):
        """Эмулирует выполнение инструкции."""
        print(f"Executing instruction: {instruction}")

    def reset(self):
        """Сбрасывает состояние процессора."""
        self.registers = [0] * 32
        self.pc = 0
        print("CPU reset complete.")
    