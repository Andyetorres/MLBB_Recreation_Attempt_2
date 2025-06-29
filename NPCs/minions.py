import pygame

class Minion:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 30, 30)
        self.color = (0, 0, 128)  # Blue color for minions
        self.max_health = 200
        self.health = 200

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        self.draw_health_bar(surface)

    def draw_health_bar(self, surface):
        # Draw health bar above minion
        bar_width = self.rect.width
        bar_height = 5
        x = self.rect.x
        y = self.rect.y - 10
        health_ratio = self.health / self.max_health

        pygame.draw.rect(surface, (200, 200, 200), (x, y, bar_width, bar_height))  # gray background
        pygame.draw.rect(surface, (255, 0, 0), (x, y, bar_width * health_ratio, bar_height))
