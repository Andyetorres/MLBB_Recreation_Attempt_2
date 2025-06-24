import pygame
import math

class Joystick:
    def __init__(self, center=(100, 600), radius=60):
        self.base_pos = pygame.Vector2(center)
        self.stick_pos = pygame.Vector2(center)
        self.base_radius = radius
        self.stick_radius = radius * 0.4
        self.dragging = False
        self.direction = pygame.Vector2(0, 0)

    def update(self):
        keys = pygame.key.get_pressed()
        dir_x = dir_y = 0

        if keys[pygame.K_w]:
            dir_y -= 1
        if keys[pygame.K_s]:
            dir_y += 1
        if keys[pygame.K_a]:
            dir_x -= 1
        if keys[pygame.K_d]:
            dir_x += 1

        keyboard_dir = pygame.Vector2(dir_x, dir_y)

        if keyboard_dir.length() > 0:
            keyboard_dir = keyboard_dir.normalize()
            self.direction = keyboard_dir
            self.stick_pos = self.base_pos + keyboard_dir * (self.base_radius - 10)
        elif not self.dragging:
            self.direction = pygame.Vector2(0, 0)
            self.stick_pos = self.base_pos


    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if (pygame.Vector2(event.pos) - self.base_pos).length() <= self.base_radius:
                self.dragging = True

        elif event.type == pygame.MOUSEBUTTONUP:
            self.dragging = False
            self.stick_pos = self.base_pos
            self.direction = pygame.Vector2(0, 0)

        elif event.type == pygame.MOUSEMOTION and self.dragging:
            mouse_vector = pygame.Vector2(event.pos) - self.base_pos
            if mouse_vector.length() > self.base_radius:
                mouse_vector = mouse_vector.normalize() * self.base_radius
            self.stick_pos = self.base_pos + mouse_vector

            if mouse_vector.length() > 0:
                self.direction = mouse_vector.normalize()
            else:
                self.direction = pygame.Vector2(0, 0)

    def get_direction(self):
        return self.direction.x, self.direction.y

    def draw(self, surface):
        pygame.draw.circle(surface, (50, 50, 50), self.base_pos, self.base_radius)
        pygame.draw.circle(surface, (0, 150, 255), self.stick_pos, self.stick_radius)
