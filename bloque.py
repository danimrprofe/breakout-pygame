import pygame
BLACK = (0,0,0)
 
class Bloque(pygame.sprite.Sprite):
    #This class represents a brick. It derives from the "Sprite" class in Pygame.
 
    def __init__(self, color, ancho, alto):
         # Llamamos al constructor de la clase Sprite
        super().__init__()
         
        self.image = pygame.Surface([ancho, alto])
        pygame.draw.rect(self.image, color, [0, 0, ancho, alto])
 
        # Cogemos las medidas de la imagen
        self.rect = self.image.get_rect()