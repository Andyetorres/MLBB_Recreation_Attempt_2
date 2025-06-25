import pygame
from Heros import Hero, Enemy
from HUB import Joystick, ButtonAtackHero
from NPCs import Minion, Creep

pygame.init()

WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("My MOBA Game")

clock = pygame.time.Clock()

hero = Hero(100, 100)
enemy = Enemy(1200, 200)

minion = Minion(600, 200)
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

    joystick.update()
    hero.move(joystick.get_direction())

    screen.fill((20, 20, 20))

    hero.draw(screen)
    enemy.draw(screen)

    minion.draw(screen)
    creep.draw(screen)

    joystick.draw(screen)
    button_attack.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
