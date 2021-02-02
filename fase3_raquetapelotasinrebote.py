# Importamos pygame
import pygame
from pygame.locals import *
# Importamos las clases Raqueta, pelota y bloque
from raqueta import Raqueta
from pelota import Pelota
from bloque import Bloque

# Inicialización de Pygame
pygame.init()

# Constantes para la inicialización de la superficie de dibujo

VENTANA_HORI = 800  # Ancho de la ventana
VENTANA_VERT = 600  # Alto de la ventana
FPS = 60  # Fotogramas por segundo

BLANCO = (255,255,255)
AZULOSCURO = (36,90,190)
LIGHTBLUE = (0,176,240)
ROJO = (255,0,0)
NARANJA = (255,100,0)
AMARILLO = (255,255,0)


# Inicialización de la superficie de dibujo (display surface)
flags = FULLSCREEN | DOUBLEBUF
#screen = pygame.display.set_mode(resolution, flags, bpp)
ventana = pygame.display.set_mode((VENTANA_HORI, VENTANA_VERT),flags,0)
#ventana = pygame.display.set_mode((VENTANA_HORI, VENTANA_VERT))

def main():

    # Vidas y puntos
    puntuacion = 0
    vidas = 9999

    pygame.display.set_caption("Juego Breakout")

    # Creamos la raqueta
    raqueta = Raqueta(LIGHTBLUE, 100, 10)
    raqueta.rect.x = 350
    raqueta.rect.y = 560

    # Creamos la pelota
    pelota = Pelota(BLANCO,10,10)
    pelota.rect.x = 345
    pelota.rect.y = 195

    # GRUPO con todos los sprites del juego
    grupo_sprites = pygame.sprite.Group()
    
    # Agregamos la pelota y la raqueta al grupo de sprites    
    grupo_sprites.add(raqueta)
    grupo_sprites.add(pelota)    



 
    # Bucle principal
    sigueJugando = True
    
    while sigueJugando:
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                    sigueJugando = False # Flag that we are done so we exit this loop
            elif event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_x: #Pressing the x Key will quit the game
                        sigueJugando = False
    
        # Comprobar si presionamos alguna tecla         
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            raqueta.mover_izquierda(5)
        if keys[pygame.K_RIGHT]:
            raqueta.mover_derecha(5)        
        
        grupo_sprites.update()

        # Comprobar el rebote de la pelota con alguna de las paredes

        if pelota.rect.x>=790:
            pelota.direccion_eje_x[0] = -pelota.direccion_eje_x[0]
        if pelota.rect.x<=0:
            pelota.direccion_eje_x[0] = -pelota.direccion_eje_x[0]
        if pelota.rect.y>590:
            pelota.direccion_eje_x[1] = -pelota.direccion_eje_x[1]
            vidas -= 1
            if vidas == 0:
                # Mostramos el mensaje de fin de juego
                font = pygame.font.Font(None, 74)
                text = font.render("GAME OVER", 1, BLANCO)
                ventana.blit(text, (250,300))
                pygame.display.flip()
                pygame.time.wait(3000)
    
                # Parar el juego
                sigueJugando=False
        if pelota.rect.y<40:
            pelota.direccion_eje_x[1] = -pelota.direccion_eje_x[1]

      
        # Fondo con color
        ventana.fill(AZULOSCURO)
        pygame.draw.line(ventana, BLANCO, [0, 38], [800, 38], 2)

         #Display the score and the number of lives at the top of the screen
        font = pygame.font.Font(None, 34)
        text = font.render("Puntos: " + str(puntuacion), 1, BLANCO)
        ventana.blit(text, (20,10))
        text = font.render("IES Ramon LLull ", 1, BLANCO)
        ventana.blit(text, (300,10))
        text = font.render("Vidas: " + str(vidas), 1, BLANCO)
        ventana.blit(text, (650,10))

         #Now let's draw all the sprites in one go. (For now we only have 2 sprites!)
        grupo_sprites.draw(ventana)    
        
        pygame.display.flip()
        pygame.time.Clock().tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
