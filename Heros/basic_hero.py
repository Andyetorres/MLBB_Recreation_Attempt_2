import pygame

class Hero:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 40, 40)
        self.color = (0, 200, 255)
        self.speed = 4
        self.health = 100

    def move(self, direction):
        dx, dy = direction
        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
