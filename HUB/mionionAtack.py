import pygame

class ButtonAttackMinion:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.default_color = (0, 128, 0)         # Verde
        self.active_color = (100, 255, 100)      # Verde claro
        self.clicked = False

    def draw(self, surface):
        color = self.active_color if self.clicked else self.default_color
        pygame.draw.circle(surface, color, (self.x, self.y), self.radius)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mx, my = event.pos
            distance = ((mx - self.x) ** 2 + (my - self.y) ** 2) ** 0.5
            if distance <= self.radius:
                self.clicked = True

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_m:  # tecla para activar el botón
                self.clicked = True

        elif event.type == pygame.MOUSEBUTTONUP or \
             (event.type == pygame.KEYUP and event.key == pygame.K_m):
            self.clicked = False

    def is_clicked(self):
        return self.clicked
