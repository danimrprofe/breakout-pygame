import pygame
from colores import Colores
from random import choice, randint
 
class Pelota(pygame.sprite.Sprite):
    # Esta clase representa una pelota. Deriva de la clase "Sprite" en Pygame.
    
    def __init__(self, color, ancho, alto, posicion_x, posicion_y):
        # Call the parent class (Sprite) constructor
        super().__init__()     

        # Atributos de la pelota
        self.ancho = ancho
        self.alto = alto
        self.velocidad = 2
        self.image = pygame.Surface([ancho, alto])
        self.image.fill(Colores.NEGRO)
        self.image.set_colorkey(Colores.NEGRO)
         
        # La pelota será un cuadrado, lo creamos
        pygame.draw.rect(self.image, color, [0, 0, ancho, alto])
        
        # Creamos 8 direcciones posibles con el mismo recorrido
        dir_posibles ={1: [  1,2], 2: [ 1,-2],
                       3: [  2,1], 4: [ 2,-1],
                       5: [ -1,2], 6: [-1,-2],
                       7: [ -2,1], 8: [-2,-1]}
        
        sorteo = randint(1,8)
        dir_elegida = dir_posibles[sorteo]
        
        # Multiplicando el vector direccion por velocidad, calcularemos la direccion
        self.direccion_x = dir_elegida[0]*self.velocidad
        self.direccion_y = dir_elegida[1]*self.velocidad

        # Cogemos las medidas de la imagen        
        self.rect = self.image.get_rect()
        self.rect.x = posicion_x
        self.rect.y = posicion_y

        
    def update(self):
        self.rect.x += self.direccion_x
        self.rect.y += self.direccion_y
    
    def rebotar(self):
        self.direccion_x = -self.direccion_x        
    
    def reiniciar(self):
        self.rect.x = 400   
        self.rect.y = 300
        