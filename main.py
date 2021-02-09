# Importamos pygame
import pygame
from colores import Colores
from ventana import Ventana
from juego import Juego

from pygame.locals import *
# Importamos las clases Raqueta, pelota y bloque
from raqueta import Raqueta
from pelota import Pelota
from bloques import Bloques


# Inicialización de Pygame
pygame.init()

# Inicialización de la superficie de dibujo (display surface)
flags = FULLSCREEN | DOUBLEBUF
#screen = pygame.display.set_mode(resolution, flags, bpp)


def main():

    # Vidas y puntos
    puntuacion = 0
    vidas = 3
    velocidad = 10

    ventana = Ventana()

    juego = Juego(velocidad, puntuacion, vidas)

    juego.finPartida = False
    while not juego.finPartida:
        juego = Juego(velocidad, puntuacion, vidas)

        # Creamos la raqueta, la pelota y los bloques
        raqueta = Raqueta(Colores.LIGHTBLUE, 100, 10, 350, 560)
        pelota = Pelota(Colores.BLANCO, 10, 10, 345, 195)
        bloques = Bloques(ventana)

        # GRUPO con todos los sprites del juego
        grupo_sprites = pygame.sprite.Group()

        # Agregamos la pelota y la raqueta al grupo de sprites
        grupo_sprites.add(raqueta)
        grupo_sprites.add(pelota)
        grupo_sprites.add(bloques.grupo)

        # Cremos las filas de ladrillos

        while not juego.finPartida:
            for event in pygame.event.get():  # User did something
                if event.type == pygame.QUIT:  # If user clicked close
                    juego.finPartida = False  # Flag that we are done so we exit this loop
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_x:  # Pressing the x Key will quit the game
                        juego.finPartida = False

            # Comprobar si presionamos alguna tecla
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                raqueta.moveLeft(5)
            if keys[pygame.K_RIGHT]:
                raqueta.moveRight(5)

            grupo_sprites.update()

            # Comprobar el rebote de la pelota con alguna de las paredes

            juego.pelota_choca_pared(pelota, ventana)
            if juego.pelota_choca_abajo(pelota, ventana):
                juego.perdervida()
                if juego.finPartida:
                    ventana.pinta_gameover()

            juego.colision_pelota_raqueta(pelota, raqueta)

            bloques.colisionBloques(pelota)
            if bloques.bloquesDestruidos > 0:
                juego.puntuacion += bloques.bloquesDestruidos
                if not bloques.quedanBloques():
                    ventana.pinta_nivelcompletado()
                    juego.finPartida = False

            # Fondo con color

            ventana.actualiza_pantalla(
                grupo_sprites, juego.puntuacion, juego.vidas)

    pygame.quit()


if __name__ == "__main__":
    main()
