import pygame
from Heros import Hero
from HUB import Joystick

pygame.init()

WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("My MOBA Game")

clock = pygame.time.Clock()

hero = Hero(100, 100)
joystick = Joystick()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            WIDTH, HEIGHT = event.w, event.h
            screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)

    joystick.update()
    hero.move(joystick.get_direction())

    screen.fill((20, 20, 20))
    hero.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
