import pygame

class BasicHero:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 40, 40)
        self.color = (0, 200, 255)

        # Posición y movimiento
        self.speed = 7
        self.move_direction = pygame.Vector2(0, 0)

        # Estadísticas base
        self.max_health = 5000
        self.health = 5000
        self.health_regen = 1.0

        self.physical_attack = 20
        self.magical_power = 0
        self.true_damage = 0

        self.physical_defense = 10
        self.magical_defense = 5
        self.crit_chance = 0.1
        self.crit_damage = 2.0

        self.life_steal = 0.0
        self.spell_vamp = 0.0
        self.resilience = 0.0

        self.physical_penetration = 0.0
        self.magical_penetration = 0.0
        self.damage_reduction = 0.0
        self.critical_damage_reduction = 0.0
        self.healing_effect = 1.0
        self.healing_received = 1.0

        # Recursos
        self.max_mana = 100
        self.mana = 100
        self.mana_regen = 2.0
        self.cooldown_reduction = 0.0

        # Rango
        self.attack_range = 90                         # alcance de ataque básico (en píxeles)
        self.vision_range = self.attack_range * 2      # campo visual = doble del ataque

        # Ataque
        self.attack_cooldown_ms = 1110
        self.last_attack_time = 0

    def move(self, direction):
        dx, dy = direction
        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed

    def move_towards(self, enemy):
        direction = pygame.Vector2(enemy.rect.center) - pygame.Vector2(self.rect.center)
        if direction.length() != 0:
            direction = direction.normalize()
            self.rect.x += direction.x * self.speed
            self.rect.y += direction.y * self.speed

    def in_attack_range(self, enemy):
        distance = pygame.Vector2(self.rect.center).distance_to(enemy.rect.center)
        return distance <= self.attack_range

    def in_vision_range(self, enemy):
        distance = pygame.Vector2(self.rect.center).distance_to(enemy.rect.center)
        return distance <= self.vision_range

    def can_see(self, enemy):
        return self.in_vision_range(enemy)

    def can_attack(self):
        return pygame.time.get_ticks() - self.last_attack_time >= self.attack_cooldown_ms

    def attack(self, target, damage_type='physical'):
        if self.can_attack() and hasattr(target, 'health'):
            damage = self.get_attack_damage(damage_type)
            target.health -= damage
            target.health = max(target.health, 0)
            self.last_attack_time = pygame.time.get_ticks()
            return damage
        return 0

    def get_attack_damage(self, damage_type='physical'):
        if damage_type == 'physical':
            return self.physical_attack
        elif damage_type == 'magical':
            return self.magical_power
        elif damage_type == 'true':
            return self.true_damage
        return 0

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        self.draw_health_bar(surface)
        self.draw_attack_range(surface)
        # self.draw_vision_range(surface)  # Descomenta para depuración visual

    def draw_health_bar(self, surface):
        bar_width = self.rect.width
        bar_height = 5
        x = self.rect.x
        y = self.rect.y - 10
        health_ratio = self.health / self.max_health

        pygame.draw.rect(surface, (200, 200, 200), (x, y, bar_width, bar_height))
        pygame.draw.rect(surface, (0, 255, 0), (x, y, bar_width * health_ratio, bar_height))

    def draw_attack_range(self, surface):
        pygame.draw.circle(surface, (200, 200, 200), self.rect.center, int(self.attack_range), 1)

    def draw_vision_range(self, surface):
        pygame.draw.circle(surface, (100, 100, 100), self.rect.center, int(self.vision_range), 1)
