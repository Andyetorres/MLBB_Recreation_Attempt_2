class Guinevere:
    def __init__(self):
        UNIDAD = 90  # 1 unidad de distancia MLBB ≈ 90 píxeles (resolución base)

        # ────────────── 🔘 FÍSICO Y COLISIONES ──────────────

        # Radio del cuerpo de Guinevere (hitbox circular)
        self.hitbox_radius_px = 40                     # px
        self.hitbox_radius_units = self.hitbox_radius_px / UNIDAD  # ≈ 0.44 unidades

        # Diámetro total del cuerpo: 80 px
        # El centro del personaje debe usarse como referencia para habilidades


        # ────────────── 🗡️ ATAQUES BÁSICOS ──────────────

        # Ataque básico estándar: corto alcance
        self.attack_range_basic_px = 162               # ≈ 1.8 unidades
        self.attack_range_basic_units = 162 / UNIDAD

        # Ataque básico cargado: mayor alcance tras un retardo
        self.attack_range_charged_px = 368             # ≈ 4.1 unidades
        self.attack_range_charged_units = 368 / UNIDAD


        # ────────────── ✨ SKILL 1 – ORBE MÁGICO ──────────────

        # Proyectil en forma de orbe circular
        self.skill1_range_px = 518                     # Alcance desde Guinevere hasta punto final
        self.skill1_range_units = 518 / UNIDAD         # ≈ 5.76 unidades

        self.skill1_projectile_diameter_px = 75        # Tamaño del orbe (visual y colisión)
        self.skill1_projectile_radius_px = 37.5        # Para colisión
        self.skill1_projectile_radius_units = 37.5 / UNIDAD  # ≈ 0.42 unidades

        # El orbe impacta al primer enemigo dentro de su radio de colisión


        # ────────────── 🌀 SKILL 2 – SALTO Y GOLPE ──────────────

        # Fase 1 – Salto hacia un punto: solo el CENTRO de Guinevere puede llegar hasta 448 px
        self.jump_range_px = 448
        self.jump_range_units = 448 / UNIDAD           # ≈ 4.98 unidades

        # Fase 2 – Golpe de aterrizaje: área circular donde los enemigos son levantados
        self.stun_area_radius_px = 151
        self.stun_area_radius_units = 151 / UNIDAD     # ≈ 1.68 unidades
        self.stun_area_diameter_px = 302               # Área visible total

        # Nota: El impacto se lanza tras caer. Todo enemigo cuya hitbox entre en este rango es suspendido.

        # Fase 3 – Dash posterior (parpadeo direccionado): Guinevere puede moverse hasta 286 px en la dirección elegida
        self.post_skill2_dash_radius_px = 286
        self.post_skill2_dash_radius_units = 286 / UNIDAD  # ≈ 3.18 unidades

        # El dash se activa justo después del aterrizaje, sirve como reposicionamiento. Instantáneo.


        # ────────────── 🌪️ SKILL 3 – ULTIMATE ──────────────

        # Habilidad canalizada: múltiples golpes mientras el enemigo principal está suspendido
        self.ulti_radius_px = 273                      # Radio del círculo de daño
        self.ulti_radius_units = 273 / UNIDAD          # ≈ 3.03 unidades

        # Se lanza tras conectar Skill 2 y suspender al enemigo (normalmente automática)
        # Inflige daño por segundo a todos dentro del rango circular


        # ────────────── 📌 INFO DE REFERENCIA GENERAL ──────────────

        self.unit_px = UNIDAD                          # Escala general para conversión
