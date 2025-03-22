class IOController:
    def __init__(self):
        self.input_state = {
            "up": False,
            "down": False,
            "left": False,
            "right": False,
            "A": False,
            "B": False,
            "Start": False,
            "Select": False
        }

    def set_button_state(self, button, state):
        """Устанавливает состояние кнопки."""
        if button in self.input_state:
            self.input_state[button] = state
            print(f"Button {button} set to {state}")

    def get_button_state(self, button):
        """Возвращает текущее состояние кнопки."""
        return self.input_state.get(button, False)
