import pygame

class Enemy:
    def __init__(self, x, y):
        # Initialize enemy position, color, health, and attack range
        self.rect = pygame.Rect(x, y, 40, 40)
        self.color = (255, 0, 0)  # Red color for enemies
        self.max_health = 10_000
        self.health = 10_000
        self.range = 18
        self.attack_range = (self.range/10)*50  # in pixels
        self.tipo = "hero"

    def draw(self, surface):
        # Draw enemy, health bar, and attack range
        pygame.draw.rect(surface, self.color, self.rect)
        self.draw_health_bar(surface)
        self.draw_attack_range(surface)

    def draw_health_bar(self, surface):
        # Draw health bar above enemy
        bar_width = self.rect.width
        bar_height = 5
        x = self.rect.x 
        y = self.rect.y - 10
        health_ratio = self.health / self.max_health

        pygame.draw.rect(surface, (200, 200, 200), (x, y, bar_width, bar_height))  # gray background
        pygame.draw.rect(surface, (255, 0, 0), (x, y, bar_width * health_ratio, bar_height))  # red health

    def draw_attack_range(self, surface):
        # Draw light gray circle (1px border) for attack range
        center = self.rect.center
        pygame.draw.circle(surface, (200, 200, 200), center, self.attack_range, 1)  # light gray circle
