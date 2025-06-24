import pygame

class Joystick:
    def __init__(self):
        self.direction = (0, 0)

    def update(self):
        keys = pygame.key.get_pressed()
        dx = dy = 0
        if keys[pygame.K_w]:
            dy -= 1
        if keys[pygame.K_s]:
            dy += 1
        if keys[pygame.K_a]:
            dx -= 1
        if keys[pygame.K_d]:
            dx += 1
        self.direction = (dx, dy)

    def get_direction(self):
        return self.direction
