import pygame

class Enemy:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 40, 40)
        self.color = (255, 0, 0)  # Red color for enemies
        self.health = 50

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)