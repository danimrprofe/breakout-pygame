import pygame

class Juego:
    def __init__(self, velocidad, puntuacion, vidas):
        self.velocidad = velocidad
        self.puntuacion = puntuacion
        self.vidas = vidas
        self.finPartida = False

    def pelota_choca_pared(self, pelota,ventana):
        if not (0 <= pelota.rect.x <= ventana.ancho - pelota.ancho):
            pelota.direccion_x = -pelota.direccion_x        
        if not (40 <= pelota.rect.y <= ventana.alto - pelota.ancho):
            pelota.direccion_y = -pelota.direccion_y        

    def pelota_choca_abajo(self, pelota,ventana):
        if (pelota.rect.y > ventana.alto - pelota.ancho):
            return True
        else:
            return False

    def colision_pelota_raqueta(self,pelota,raqueta):
                # Detectar colision entre la pelota y la raqueta
        if pygame.sprite.collide_mask(pelota, raqueta):
            
            pelota.direccion_y = -pelota.direccion_y
            pelota.rect.y += pelota.direccion_y
            

    def perdervida(self):
        self.vidas -= 1
        if self.vidas == 0:  self.finPartida = True