import pygame
import time
from Heros import Enemy , BasicHero
from HUB import Joystick, ButtonAtackHero, DamageText, TargetMark, ButtonAttackMinion
from NPCs import Minion, Creep


pygame.init()

WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("My MOBA Game")

clock = pygame.time.Clock()

# El héroe es BasicHero
hero = BasicHero(100, 100)
enemy_1 = Enemy(1100, 200)
enemy_2 = Enemy(1100, 350)

damage_texts = []

red_minion = Minion(600, 200)
blue_minion = Minion(600, 350)
creep = Creep(800, 200)

joystick = Joystick()
button_attack = ButtonAtackHero(1200, 600, 50)
button_attack_minion = ButtonAttackMinion(1200, 500, 50)
target_marker = TargetMark()

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
    hero.move(joystick.get_direction())

    # Lógica de ataque
    if button_attack.is_clicked():
        enemies = [enemy_1, enemy_2, red_minion, creep]

        # Filtra enemigos que estén en pantalla y visión
        visible_enemies = [
            e for e in enemies
            if screen.get_rect().colliderect(e.rect) and hero.can_see(e)
        ]

        # Encuentra el enemigo con menos vida dentro de visión (sin importar ataque aún)
        lowest_hp_enemy = None
        lowest_hp = float('inf')

        for enemy in visible_enemies:
            if enemy.health < lowest_hp:
                lowest_hp = enemy.health
                lowest_hp_enemy = enemy

        if lowest_hp_enemy:
            target_marker.set_target(lowest_hp_enemy)  # ✅ Se marca aunque esté fuera de ataque

            # Solo atacamos si está en rango de ataque
            if hero.in_attack_range(lowest_hp_enemy):
                damage = hero.attack(lowest_hp_enemy)
                if damage > 0:
                    damage_texts.append(DamageText(damage, lowest_hp_enemy.rect.center))
        else:
            target_marker.clear_target()
    else:
        target_marker.clear_target()


        # Si se activa el botón de minions
    if button_attack_minion.is_clicked():
        minions = [red_minion]
        visible_minions = [
            m for m in minions if screen.get_rect().colliderect(m.rect) and hero.can_see(m)
        ]

        # Encuentra el minion con menos vida
        target_minion = None
        lowest_hp = float('inf')
        for minion in visible_minions:
            if minion.health < lowest_hp:
                lowest_hp = minion.health
                target_minion = minion

        if target_minion:
            target_marker.set_target(target_minion)
            if hero.in_attack_range(target_minion):
                damage = hero.attack(target_minion)
                if damage > 0:
                    damage_texts.append(DamageText(damage, target_minion.rect.center))
        else:
            target_marker.clear_target()

    screen.fill((20, 20, 20))

    hero.draw(screen)
    hero.draw_vision_range(screen)

    enemy_1.draw(screen)
    enemy_2.draw(screen)

    blue_minion.draw(screen)
    red_minion.draw(screen)
    creep.draw(screen)

    joystick.draw(screen)
    button_attack.draw(screen)
    target_marker.draw(screen)


    # Dibuja los textos de daño
    for dmg in damage_texts:
        dmg.draw(screen)

    # Elimina los textos expirados
    damage_texts = [d for d in damage_texts if not d.is_expired()]

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
