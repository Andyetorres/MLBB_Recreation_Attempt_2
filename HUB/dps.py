import pygame
import time
import random

class DamageText:
    def __init__(self, text, position, duration=0.5, drift_amount=5):
        self.text = str(text)
        self.start_time = time.time()
        self.duration = duration
        self.font = pygame.font.Font(None, 24)
        self.color = (255, 255, 255)  # Blanco

        self.base_x, self.base_y = position
        self.offset_x = random.uniform(-drift_amount, drift_amount)  # izquierda o derecha
        self.rise = random.uniform(3, 6)  # sube unos pixeles
        self.fall = self.rise * 3         # baja el triple

    def draw(self, surface):
        elapsed = time.time() - self.start_time
        if elapsed < self.duration:
            progress = elapsed / self.duration  # entre 0.0 y 1.0

            # Movimiento vertical: sube y luego baja suavemente
            y_movement = -self.rise + self.fall * progress
            x = self.base_x + self.offset_x
            y = self.base_y + y_movement - 20

            damage_surface = self.font.render(self.text, True, self.color)
            rect = damage_surface.get_rect(center=(x, y))
            surface.blit(damage_surface, rect)

    def is_expired(self):
        return (time.time() - self.start_time) >= self.duration
