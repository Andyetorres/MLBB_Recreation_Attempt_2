import pygame

class Hero:
    def __init__(self, x, y):
        # Initialize hero position, color, speed, health, and attack stats
        self.rect = pygame.Rect(x, y, 40, 40)
        self.color = (0, 200, 255)
        self.speed = 4
        self.max_health = 100
        self.health = 100
        self.range = 18
        self.attack_range = (self.range / 10) * 50  # in pixels
        self.attack_damage = 200  # Base attack damage
        self.last_attack_time = 0
        self.attack_cooldown_ms = 1000  # 1 second cooldown

    def move(self, direction):
        # Move hero by direction vector (dx, dy)
        dx, dy = direction
        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed

    def draw(self, surface):
        # Draw hero, health bar, and attack range
        pygame.draw.rect(surface, self.color, self.rect)
        self.draw_health_bar(surface)
        self.draw_attack_range(surface)

    def draw_health_bar(self, surface):
        # Draw health bar above hero
        bar_width = self.rect.width
        bar_height = 5
        x = self.rect.x
        y = self.rect.y - 10
        health_ratio = self.health / self.max_health

        pygame.draw.rect(surface, (200, 200, 200), (x, y, bar_width, bar_height))  # gray background
        pygame.draw.rect(surface, (0, 255, 0), (x, y, bar_width * health_ratio, bar_height))  # green health

    def draw_attack_range(self, surface):
        # Draw light gray circle (1px border) for attack range
        center = self.rect.center
        pygame.draw.circle(surface, (200, 200, 200), center, int(self.attack_range), 1)  # light gray circle

    def in_attack_range(self, enemy):
        # Check if enemy is within attack range
        distance = pygame.Vector2(self.rect.center).distance_to(enemy.rect.center)
        return distance <= self.attack_range

    def attack(self, target):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_attack_time >= self.attack_cooldown_ms:
            if hasattr(target, 'health'):
                target.health -= self.attack_damage
                if target.health < 0:
                    target.health = 0
                self.last_attack_time = current_time
                return True  # Atacó
        return False  # No atacó

    def move_towards(self, enemy):
        # Move hero towards enemy
        direction = pygame.Vector2(enemy.rect.center) - pygame.Vector2(self.rect.center)
        if direction.length() != 0:
            direction = direction.normalize()
            self.rect.x += direction.x * self.speed
            self.rect.y += direction.y * self.speed

