import pygame

class Creep:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 30, 30)
        self.color = (128, 0, 128)  # Purple color for creeps
        self.health = 30

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
