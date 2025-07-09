# Core/timeController.py

import pygame

class TimeController:
    def __init__(self):
        self.start_ticks = pygame.time.get_ticks()  # Tiempo de inicio en ms
        self.paused = False
        self.pause_time = 0
        self.offset = 0  # Offset acumulado por pausas
        self.time_scale = 1.0  # Escala de tiempo: 1.0 es normal, 2.0 es el doble de rápido

    def get_game_time_ms(self):
        """Retorna el tiempo transcurrido desde el inicio, ajustado por pausas y escala."""
        if self.paused:
            base_time = self.pause_time - self.start_ticks - self.offset
        else:
            base_time = pygame.time.get_ticks() - self.start_ticks - self.offset
        return int(base_time * self.time_scale)

    def get_game_time_sec(self):
        """Tiempo en segundos escalado, redondeado."""
        return self.get_game_time_ms() // 1000

    def get_formatted_time(self):
        """Devuelve el tiempo en formato MM:SS."""
        total_seconds = self.get_game_time_sec()
        minutes = total_seconds // 60
        seconds = total_seconds % 60
        return f"{minutes:02}:{seconds:02}"

    def pause(self):
        if not self.paused:
            self.paused = True
            self.pause_time = pygame.time.get_ticks()

    def resume(self):
        if self.paused:
            self.paused = False
            paused_duration = pygame.time.get_ticks() - self.pause_time
            self.offset += paused_duration

    def set_time_scale(self, scale):
        """Define la velocidad del tiempo (1.0 normal, >1 más rápido, <1 más lento)."""
        if scale > 0:
            self.time_scale = scale
