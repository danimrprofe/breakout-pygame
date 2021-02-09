import pygame
from random import choice, randint
BLACK = (0,0,0)
 
class Pelota(pygame.sprite.Sprite):
    #This class represents a ball. It derives from the "Sprite" class in Pygame.
    
    def __init__(self, color, ancho, alto, posicion_x, posicion_y):
        # Call the parent class (Sprite) constructor
        super().__init__()
        
        # Pass in the color of the ball, its width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([ancho, alto])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        self.ancho = ancho
        self.alto = alto
 
        # Draw the ball (a rectangle!)
        pygame.draw.rect(self.image, color, [0, 0, ancho, alto])
        
        self.velocity = [randint(4,8),randint(-8,8)]
        
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
        self.rect.x = posicion_x
        self.rect.y = posicion_y

        
    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
    
    def rebotar(self):
        self.velocity[0] = -self.velocity[0]
        
        allowed_values = list(range(-8, 8))
        allowed_values.remove(0)

        self.velocity[1] = choice(allowed_values)
        