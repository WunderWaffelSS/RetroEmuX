class GPURenderer:
    def __init__(self):
        self.framebuffer = [[0] * 640 for _ in range(480)]  # 640x480 пустой кадр

    def render_frame(self):
        """Отрисовывает кадр."""
        print("Rendering frame...")

    def clear_screen(self):
        """Очищает экран."""
        self.framebuffer = [[0] * 640 for _ in range(480)]
        print("Screen cleared.")
