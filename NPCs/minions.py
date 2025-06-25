import pygame

class Minion:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 30, 30)
        self.color = (0, 0, 128)  # Blue color for minions
        self.health = 20

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
