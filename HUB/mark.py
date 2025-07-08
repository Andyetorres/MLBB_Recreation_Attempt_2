import pygame

class TargetMark:
    def __init__(self):
        self.target = None

    def set_target(self, entity):
        self.target = entity

    def clear_target(self):
        self.target = None

    def draw(self, surface):
        if self.target and hasattr(self.target, "rect"):
            rect = self.target.rect.inflate(10, 10)  # Un poco más grande que el objetivo
            x, y, w, h = rect
            color = (255, 255, 0)  # Amarillo para destacar
            thickness = 2

            # Dibujar las 4 esquinas tipo { } con líneas
            pygame.draw.line(surface, color, (x, y), (x + 15, y), thickness)
            pygame.draw.line(surface, color, (x, y), (x, y + 15), thickness)

            pygame.draw.line(surface, color, (x + w, y), (x + w - 15, y), thickness)
            pygame.draw.line(surface, color, (x + w, y), (x + w, y + 15), thickness)

            pygame.draw.line(surface, color, (x, y + h), (x + 15, y + h), thickness)
            pygame.draw.line(surface, color, (x, y + h), (x, y + h - 15), thickness)

            pygame.draw.line(surface, color, (x + w, y + h), (x + w - 15, y + h), thickness)
            pygame.draw.line(surface, color, (x + w, y + h), (x + w, y + h - 15), thickness)
