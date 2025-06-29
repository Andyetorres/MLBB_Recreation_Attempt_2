import pygame

class ButtonAtackHero:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.default_color = (0, 0, 255)       # Azul
        self.active_color = (100, 100, 255)    # Azul más claro
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
            if event.key == pygame.K_n:
                self.clicked = True

        elif event.type == pygame.MOUSEBUTTONUP:
            self.clicked = False

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_n:
                self.clicked = False

    def is_clicked(self):
        return self.clicked
