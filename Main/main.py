import pygame
import time
from Heros import Enemy , BasicHero
from HUB import Joystick, ButtonAtackHero, DamageText, TargetMark, ButtonAttackMinion, ClockController
from NPCs import Minion, Creep
from Map import SimpleTower


pygame.init()

WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("My MOBA Game")

clock = pygame.time.Clock()

# El héroe es BasicHero
hero = BasicHero(100, 100)
enemy_1 = Enemy(900, 200)
enemy_2 = Enemy(1100, 350)

damage_texts = []

red_minion = Minion(600, 200)
blue_minion = Minion(600, 350)
creep = Creep(800, 200)

tower = SimpleTower(200,200)

joystick = Joystick()
button_attack = ButtonAtackHero(1200, 600, 50)
button_attack_minion = ButtonAttackMinion(1200, 500, 40)
target_marker = TargetMark()

clock_hud = ClockController(x=WIDTH // 2, y=40)

# Controlador global de objetivo mantenido
current_target = None

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            WIDTH, HEIGHT = event.w, event.h
            screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)

        joystick.handle_event(event)
        button_attack.handle_event(event)
        button_attack_minion.handle_event(event)

    joystick.update()
    hero.move(joystick.get_direction())  # Movimiento manual

    # 🔵 ATAQUE A HÉROES → MINIONS == CREEPS → TORRES (Con cambio dinámico)
    if button_attack.is_clicked():
        all_targets = [enemy_1, enemy_2, red_minion, creep, tower]

        # Primero: filtramos objetivos válidos
        visible_targets = [
            e for e in all_targets
            if screen.get_rect().colliderect(e.rect) and hero.can_see(e)
        ]


        def prioridad(entidad):
            orden = {"hero": 0, "minion": 1, "creep": 1, "torre": 2}
            return orden.get(getattr(entidad, "tipo", ""), 99)

        def hp(entidad):
            return getattr(entidad, "health", float('inf'))

        # Validar si hay que cambiar de objetivo
        if (
            current_target is None
            or current_target.health <= 0
            or not hero.can_see(current_target)
            or any(
                prioridad(e) < prioridad(current_target) or
                (prioridad(e) == prioridad(current_target) and hp(e) < hp(current_target))
                for e in visible_targets
            )
        ):
            # Reasigna nuevo objetivo según prioridad y vida
            current_target = None
            for prioridad_tipo in ["hero", "minion", "creep", "torre"]:
                posibles = [e for e in visible_targets if getattr(e, "tipo", "") == prioridad_tipo]
                if posibles:
                    current_target = min(posibles, key=hp)
                    break

        # Atacar o moverse hacia el objetivo
        if current_target:
            target_marker.set_target(current_target)
            if hero.in_attack_range(current_target):
                damage = hero.attack(current_target)
                if damage > 0:
                    damage_texts.append(DamageText(damage, current_target.rect.center))
            else:
                hero.move_towards(current_target)
        
    else:
        current_target = None
        target_marker.clear_target()

    # 🟡 ATAQUE A MINIONS (Minions o Creeps con menor vida)
    if button_attack_minion.is_clicked():
        minions = [red_minion, creep]

        # Filtra por pantalla y visión
        visible_minions = [
            m for m in minions
            if screen.get_rect().colliderect(m.rect) and hero.can_see(m)
        ]

        # Reasigna siempre al que tenga menor vida visible
        target_minion = None
        lowest_hp = float('inf')
        for m in visible_minions:
            if m.health < lowest_hp:
                lowest_hp = m.health
                target_minion = m

        current_target = target_minion

        if current_target:
            target_marker.set_target(current_target)
            if hero.in_attack_range(current_target):
                damage = hero.attack(current_target)
                if damage > 0:
                    damage_texts.append(DamageText(damage, current_target.rect.center))
            else:
                hero.move_towards(current_target)
    else:
        # Solo limpia si NO se está atacando con el botón principal
        if not button_attack.is_clicked():
            current_target = None
            target_marker.clear_target()

    # -----------------------------
    # DIBUJO
    # -----------------------------
    screen.fill((20, 20, 20))

    hero.draw(screen)
    hero.draw_vision_range(screen)

    enemy_1.draw(screen)
    enemy_2.draw(screen)
    blue_minion.draw(screen)
    red_minion.draw(screen)
    creep.draw(screen)

    tower.draw(screen)

    joystick.draw(screen)
    button_attack.draw(screen)
    button_attack_minion.draw(screen)
    target_marker.draw(screen)

    clock_hud.draw(screen)

    for dmg in damage_texts:
        dmg.draw(screen)
    damage_texts = [d for d in damage_texts if not d.is_expired()]

    pygame.display.flip()
    clock.tick(60)


pygame.quit()
