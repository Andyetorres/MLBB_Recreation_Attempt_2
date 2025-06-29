import pygame
from Heros.basic_hero import BasicHero

class Guinevere_controller(BasicHero):
    def __init__(self, x, y):
        super().__init__(x, y)

        # === Rol y tipo de daño ===
        self.role = "Combatiente"
        self.damage_type = "magical"
        self.difficulty = "Media-Alta"

        # === Estadísticas Base Nivel 0 ===
        self.max_health = 2350
        self.health = self.max_health
        self.health_regen = 7.8

        self.physical_attack = 116.785
        self.physical_defense = 13.5
        self.magical_defense = 12.5

        self.attack_speed = 1.11  # segundos por ataque
        self.attack_cooldown_ms = int(self.attack_speed * 1000)

        self.crit_chance = 0.0
        self.crit_damage = 2.0  # 200%

        self.life_steal = 0.0
        self.range = 1.8  # unidades internas
        self.attack_range = (self.range / 10) * 50  # en píxeles (90px)

        self.movement_speed = 286
        self.speed = self.movement_speed / 100  # adaptado a pygame

        self.cooldown_reduction = 0.0
        self.magical_power = 0
        self.mana = 0
        self.max_mana = 0
        self.mana_regen = 0

        self.physical_penetration = 0.0
        self.magical_penetration = 0.0
        self.spell_vamp = 0.0
        self.resilience = 0.0
        self.damage_reduction = 0.0
        self.critical_damage_reduction = 0.0
        self.healing_effect = 0.0
        self.healing_received = 0.0

        # === Rango de visión ===
        self.vision_range = 200

        # Nivel y escalado (guardado para uso futuro)
        self.level = 0
        self.scaling = {
            "hp": 157,
            "physical_attack": 9.214,
            "physical_defense": 4.5,  # +1.95% implícito
            "magical_defense": 2.5,   # +1.307% implícito
            "attack_speed": 0.03,
            "health_regen": 4.4,
            "magical_power": 28
        }
