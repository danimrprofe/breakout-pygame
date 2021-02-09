import pygame

class Juego:
    def __init__(self, velocidad, puntuacion, vidas):
        self.velocidad = velocidad
        self.puntuacion = puntuacion
        self.vidas = vidas
        self.finPartida = False

    def pelota_choca_pared(self, pelota,ventana):

        if pelota.rect.x >= ventana.ancho - pelota.ancho:
            pelota.velocity[0] = -pelota.velocity[0]
        if pelota.rect.x <= 0:
            pelota.velocity[0] = -pelota.velocity[0]
        if pelota.rect.y > ventana.alto - pelota.ancho:
            pelota.velocity[1] = -pelota.velocity[1]
        if pelota.rect.y < 40:
            pelota.velocity[1] = -pelota.velocity[1]

    def pelota_choca_abajo(self, pelota,ventana):
        if (pelota.rect.y > ventana.alto - pelota.ancho):
            return True
        else:
            return False

    def colision_pelota_raqueta(self,pelota,raqueta):
                # Detectar colision entre la pelota y la raqueta
        if pygame.sprite.collide_mask(pelota, raqueta):
            pelota.rect.x -= pelota.velocity[0]
            pelota.rect.y -= pelota.velocity[1]
            pelota.rebotar()

    def perdervida(self):
        self.vidas -= 1
        if self.vidas == 0:
            self.finPartida = True