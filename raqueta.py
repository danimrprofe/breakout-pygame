import pygame
from colores import Colores

class Raqueta(pygame.sprite.Sprite):
    # This class represents a paddle. It derives from the "Sprite" class in Pygame.

    def __init__(self, color, ancho, alto, posicion_x, posicion_y, ventana):
        # Llamamos al constructor de la clase Sprite
        super().__init__()

       # Atributos de la raqueta
        self.ancho = ancho
        self.alto = alto
        self.image = pygame.Surface([self.ancho, self.alto])
        self.image.fill(Colores.NEGRO)
        self.image.set_colorkey(Colores.NEGRO)
        self.ventana = ventana
        self.pos_inicial_x = posicion_x
        self.pos_inicial_y = posicion_y

        # La raqueta será un rectángulo
        pygame.draw.rect(self.image, color, [0, 0, self.ancho, self.alto])

        # Cogemos las medidas de la imagen        
        self.rect = self.image.get_rect()
        self.rect.x = posicion_x
        self.rect.y = posicion_y

    def mover(self, pixels):
        self.rect.x += pixels
        
        # Movemos la raqueta a izquierda o derecha
        if self.rect.x < 0: self.rect.x = 0            
        if self.rect.x > self.ventana.ancho - self.ancho: self.rect.x = self.ventana.ancho - self.ancho

    def reiniciar(self):
        self.rect.x = self.pos_inicial_x   
        self.rect.y = self.pos_inicial_y
        

