import pygame

class Creep:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 30, 30)
        self.color = (128, 0, 128)  # Purple color for creeps
        self.max_health = 2500
        self.health = 2500
        self.tipo = "creep"

    def draw(self, surface):
        # Draw creep, health bar, and attack range
        pygame.draw.rect(surface, self.color, self.rect)
        self.draw_health_bar(surface)
        # Si quieres un rango de ataque, descomenta la siguiente línea y define self.attack_range
        # self.draw_attack_range(surface)

    def draw_health_bar(self, surface):
        # Draw health bar above creep
        bar_width = self.rect.width
        bar_height = 5
        x = self.rect.x 
        y = self.rect.y - 10
        health_ratio = self.health / self.max_health

        pygame.draw.rect(surface, (200, 200, 200), (x, y, bar_width, bar_height))  # gray background
        pygame.draw.rect(surface, (255, 0, 0), (x, y, bar_width * health_ratio, bar_height))  # red health

    # Si quieres que los creeps tengan rango de ataque, agrega este método:
    # def draw_attack_range(self, surface):
    #     center = self.rect.center
    #     pygame.draw.circle(surface, (200, 200, 200), center, int(self.attack_range), 1)

