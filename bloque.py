import pygame
BLACK = (0,0,0)

ROJO = pygame.Color("#ff7b54")
NARANJA = pygame.Color("#ffb26b")
AMARILLO = pygame.Color("#ffd56b")
 
class Bloque(pygame.sprite.Sprite):
    #This class represents a brick. It derives from the "Sprite" class in Pygame.
 
    def __init__(self, width, height, vidas):
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        # Pass in the color of the brick, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.vidas = vidas
                
        if self.vidas == 1:
            self.color = AMARILLO
            self.puntos = 1
        if self.vidas == 2:
            self.color = NARANJA
            self.puntos = 2
        if self.vidas == 3:
            self.puntos = 3
            self.color = ROJO
        self.height = height
        self.width = width
        self.image = pygame.Surface([width, height])
        #self.image = pygame.image.load("bloque.png").convert_alpha()
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
 
        # Draw the brick (a rectangle!)
        pygame.draw.rect(self.image, self.color, [0, 0, width, height])
 
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
    def golpear(self):
        if self.vidas > 0:
            self.vidas -= 1
            if self.vidas == 1:
                self.color = AMARILLO
            if self.vidas == 2:
                self.color = NARANJA
            if self.vidas == 3:
                self.color = ROJO
            pygame.draw.rect(self.image, self.color, [0, 0, self.width, self.height])
        else:
            vidas = 0