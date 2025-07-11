
import pygame

class SimpleTower:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 40, 40)  # Las torres son un poco más grandes
        self.color = (150, 0, 0)  # Color amarillo oscuro
        self.max_health = 4500
        self.health = 4500
        self.tipo = "torre"  # Usar "tipo" y no "type" para evitar conflictos

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        self.draw_health_bar(surface)

    def draw_health_bar(self, surface):
        bar_width = self.rect.width
        bar_height = 5
        x = self.rect.x
        y = self.rect.y - 10
        health_ratio = self.health / self.max_health

        # Fondo de la barra de vida (gris)
        pygame.draw.rect(surface, (100, 100, 100), (x, y, bar_width, bar_height))
        # Vida restante (verde)
        pygame.draw.rect(surface, (0, 200, 0), (x, y, bar_width * health_ratio, bar_height))


"""
import pygame
import time

class Torre:
    def __init__(self, tipo, x, y):
        self.tipo = tipo
        self.rect = pygame.Rect(x, y, 50, 50)
        self.color = (255, 255, 0)

        # Estado de la torre
        self.viva = True
        self.objetivo_actual = None
        self.tiempo_ultimo_ataque = 0
        self.escudo_activado = False
        self.bufo_activo = False
        self.ataques_recientes = []
        self.reduccion_dano_heroe_sin_minions = False

        self.golpes_consecutivos = 0
        self.ultimo_objetivo = None
        self.ultimo_ataque = 0
        self.defensa_barrera = False

        self._inicializar_estadisticas(tipo)
        self.tiempo_ultimo_cambio = 0

    def _inicializar_estadisticas(self, tipo):
        self.escudo_duracion = 300000  # 5 minutos en ms
        self.tiempo_creacion = pygame.time.get_ticks()

        datos = {
            "T1": {
                "hp": 4500,
                "danio_base": 360,
                "danio_incr": 240,
                "danio_max": 4880,
                "vel_ataque": 3820,
                "autocuracion": 0,
                "escudo": True,
                "defensa": 30,
            },
            "T2": {
                "hp": 5700,
                "danio_base": 360,
                "danio_incr": 270,
                "danio_max": 5440,
                "vel_ataque": 3820,
                "autocuracion": 0,
                "escudo": False,
                "defensa": 40,
            },
            "T3": {
                "hp": 7300,
                "danio_base": 520,
                "danio_incr": 390,
                "danio_max": 7930,
                "vel_ataque": 3820,
                "autocuracion": 0,
                "escudo": False,
                "defensa": 50,
            },
            "Principal": {
                "hp": 7900,
                "danio_base": 560,
                "danio_incr": 420,
                "danio_max": 8540,
                "vel_ataque": 3820,
                "autocuracion": 165,
                "escudo": False,
                "defensa": 60,
            }
        }

        stats = datos[tipo]
        self.max_health = stats["hp"]
        self.health = stats["hp"]
        self.danio_base = stats["danio_base"]
        self.danio_incr = stats["danio_incr"]
        self.danio_max = stats["danio_max"]
        self.vel_ataque = stats["vel_ataque"]
        self.autocuracion = stats["autocuracion"]
        self.escudo_activado = stats["escudo"]
        self.defensa_fisica = stats["defensa"]
        self.defensa_magica = stats["defensa"]

        self.rango_ataque = 300

    def calcular_dano(self):
        danio = self.danio_base + self.golpes_consecutivos * self.danio_incr
        return min(danio, self.danio_max)

    def seleccionar_objetivo(self, enemigos_en_rango, atacantes_aliados):
        tiempo_actual = pygame.time.get_ticks()
        if self.objetivo_actual and self.objetivo_actual.health > 0:
            return self.objetivo_actual

        if atacantes_aliados:
            self.objetivo_actual = atacantes_aliados[0]
            return self.objetivo_actual

        for enemigo in enemigos_en_rango:
            if enemigo.tipo == "minion" or enemigo.tipo == "creep":
                self.objetivo_actual = enemigo
                return enemigo

        for enemigo in enemigos_en_rango:
            if enemigo.tipo == "hero":
                self.objetivo_actual = enemigo
                return enemigo

        self.objetivo_actual = None
        return None

    def recibir_dano(self, cantidad, tipo_dano="fisico", buffo=False, sin_minions=False):
        if not self.viva:
            return

        if self.tipo == "T1" and self.escudo_activado:
            if pygame.time.get_ticks() - self.tiempo_creacion < self.escudo_duracion:
                return
            else:
                self.escudo_activado = False

        defensa = 60 if buffo else self.defensa_fisica if tipo_dano == "fisico" else self.defensa_magica
        reduccion = 100 / (100 + defensa)
        danio_final = cantidad * reduccion

        if sin_minions:
            danio_final *= 0.5

        self.health -= danio_final
        if self.health <= 0:
            self.health = 0
            self.viva = False

    def curarse(self):
        if self.tipo == "Principal" and self.health < self.max_health:
            self.health = min(self.max_health, self.health + self.autocuracion)

    def puede_atacar(self):
        return pygame.time.get_ticks() - self.tiempo_ultimo_ataque >= self.vel_ataque

    def actualizar_golpe(self, mismo_objetivo=True):
        if mismo_objetivo:
            self.golpes_consecutivos += 1
        else:
            self.golpes_consecutivos = 0

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        self.draw_health_bar(surface)
        if self.escudo_activado:
            pygame.draw.rect(surface, (100, 200, 255), self.rect, 3)

    def draw_health_bar(self, surface):
        bar_width = self.rect.width
        bar_height = 5
        x = self.rect.x
        y = self.rect.y - 10
        ratio = self.health / self.max_health

        pygame.draw.rect(surface, (100, 100, 100), (x, y, bar_width, bar_height))
        pygame.draw.rect(surface, (0, 255, 0), (x, y, bar_width * ratio, bar_height))
"""