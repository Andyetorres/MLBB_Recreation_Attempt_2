import pygame
import time
from Heros import Enemy , BasicHero
from HUB import Joystick, ButtonAtackHero, DamageText
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

    joystick.update()
    hero.move(joystick.get_direction())

    # Lógica de ataque
    if button_attack.is_clicked():
        # Incluye todos los objetivos posibles
        enemies = [enemy_1, enemy_2, red_minion, creep]
        visible_enemies = [e for e in enemies if screen.get_rect().colliderect(e.rect)]
        for enemy in visible_enemies:
            if hero.in_attack_range(enemy):
                damage = hero.attack(enemy)  # Ahora retorna el daño infligido
                if damage > 0:
                    damage_texts.append(DamageText(damage, enemy.rect.center))
                break  # Ataca solo a uno por click

    screen.fill((20, 20, 20))

    hero.draw(screen)
    enemy_1.draw(screen)
    enemy_2.draw(screen)

    blue_minion.draw(screen)
    red_minion.draw(screen)
    creep.draw(screen)

    joystick.draw(screen)
    button_attack.draw(screen)

    # Dibuja los textos de daño
    for dmg in damage_texts:
        dmg.draw(screen)

    # Elimina los textos expirados
    damage_texts = [d for d in damage_texts if not d.is_expired()]

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
