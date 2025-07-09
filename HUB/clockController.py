# HUB/clockController.py

import pygame
from Core.timeController import TimeController

class ClockController:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 50
        self.clock = TimeController()

        self.font = pygame.font.SysFont("Arial", 28, bold=True)

    def draw(self, surface):
        # Dibujar fondo del reloj (medio círculo gris)
        pygame.draw.circle(surface, (50, 50, 50), (self.x, self.y), self.radius)

        # Dibujar tiempo
        formatted_time = self.clock.get_formatted_time()
        text_surface = self.font.render(formatted_time, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(self.x, self.y))
        surface.blit(text_surface, text_rect)

    def get_time_controller(self):
        """Retorna la instancia de TimeController (opcional si se requiere manipularla desde fuera)."""
        return self.clock
