# IMPORTACIONES

import pygame
from pygame.locals import *
from raqueta import Raqueta
from pelota import Pelota
from bloque import Bloque

# MEDIDAS

VENTANA_HORI = 800  # Ancho de la ventana
VENTANA_VERT = 600  # Alto de la ventana
FPS = 60  # Fotogramas por segundo

# COLORES

BLANCO = pygame.Color("#ffffff")
AZULOSCURO = pygame.Color("#140F2D")
LIGHTBLUE = pygame.Color("#3F88C5")

# DATOS

puntuacion = 0
vidas = 9999

# INICIAR PYGAME

pygame.init()
ventana = pygame.display.set_mode((VENTANA_HORI, VENTANA_VERT))
pygame.display.set_caption("Juego Breakout")
fuente = pygame.font.Font(None, 34)

# CREAR SPRITES

grupo_sprites = pygame.sprite.Group()  # Aquí irán todos los sprites
grupo_bloques = pygame.sprite.Group()  # Aquí irán sólo los bloques

raqueta = Raqueta(LIGHTBLUE, 100, 10)
raqueta.rect.x = 350
raqueta.rect.y = 560
grupo_sprites.add(raqueta)

pelota = Pelota(BLANCO, 10, 10)
pelota.rect.x = 345
pelota.rect.y = 195
grupo_sprites.add(pelota)

for i in range(7):  # PRIMERA FILA DE LADRILLOS
    bloque = Bloque(80, 30, 3)
    bloque.rect.x = 60 + i * 100
    bloque.rect.y = 60
    grupo_sprites.add(bloque)
    grupo_bloques.add(bloque)
for i in range(7):  # SEGUNDA FILA DE LADRILLOS
    bloque = Bloque(80, 30, 2)
    bloque.rect.x = 60 + i * 100
    bloque.rect.y = 100
    grupo_sprites.add(bloque)
    grupo_bloques.add(bloque)
for i in range(7):  # TERCERA FILA DE LADRILLOS
    bloque = Bloque(80, 30, 1)
    bloque.rect.x = 60 + i * 100
    bloque.rect.y = 140
    grupo_sprites.add(bloque)
    grupo_bloques.add(bloque)

# BUCLE PRINCIPAL

sigueJugando = True
while sigueJugando:

    # EVENTOS

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            sigueJugando = False  # Flag that we are done so we exit this loop

    # Comprobar si presionamos alguna tecla

    teclas_pulsadas = pygame.key.get_pressed()

    if teclas_pulsadas[pygame.K_x]:  # Salir del juego
        sigueJugando = False
    if teclas_pulsadas[pygame.K_LEFT]: # Mover raqueta a la izquierda
        raqueta.mover_izquierda(5)
    if teclas_pulsadas[pygame.K_RIGHT]: # Mover raqueta a la derecha
        raqueta.mover_derecha(5)

    # LOGICA DEL PROGRAMA

    grupo_sprites.update()

    # REBOTE DE LA PELOTA

    if pelota.rect.x >= 790: # Pared derecha
        pelota.velocity[0] = -pelota.velocity[0]
    if pelota.rect.x <= 0: # Pared izquierda
        pelota.velocity[0] = -pelota.velocity[0]  
    if pelota.rect.y < 40: # Pared arriba
        pelota.velocity[1] = -pelota.velocity[1]
    if pelota.rect.y > 590: # Pared abajo (perdemos vida)
        pelota.velocity[1] = -pelota.velocity[1]
        vidas -= 1

        # Partida perdida
        
        if vidas == 0:            
            fuente = pygame.font.Font(None, 74)
            text = fuente.render("GAME OVER", 1, BLANCO)
            ventana.blit(text, (250, 300))
            pygame.display.flip()
            pygame.time.wait(3000)
            # Parar el juego
            sigueJugando = False

    # COLISIONES

    # Colisiones pelota - paredes

    if pygame.sprite.collide_mask(pelota, raqueta):
        pelota.rect.x -= pelota.velocity[0]
        pelota.rect.y -= pelota.velocity[1]
        pelota.rebotar()

    # Colisiones pelota - bloques

    grupo_bloques_golpeados = pygame.sprite.spritecollide(
        pelota, grupo_bloques, False)
    for bloque in grupo_bloques_golpeados:
        pelota.rebotar()
        bloque.golpear()

        # Borrar bloque

        if bloque.vidas == 0:
            puntuacion += bloque.puntos
            bloque.kill()

        # Partida ganada

        if len(grupo_bloques) == 0:
            fuente = pygame.font.Font(None, 74)
            text = fuente.render("NIVEL COMPLETADO", 1, BLANCO)
            ventana.blit(text, (200, 300))
            pygame.display.flip()
            pygame.time.wait(3000)
            
            sigueJugando = False

    # IMAGENES

    # Pintamos el fondo

    ventana.fill(AZULOSCURO)
    pygame.draw.line(ventana, BLANCO, [0, 38], [800, 38], 2)

    # Pintamos el texto

    fuente = pygame.font.Font(None, 34)
    text = fuente.render("Puntos: " + str(puntuacion), 1, BLANCO)
    ventana.blit(text, (20, 10))
    text = fuente.render("IES Ramon LLull ", 1, BLANCO)
    ventana.blit(text, (300, 10))
    text = fuente.render("Vidas: " + str(vidas), 1, BLANCO)
    ventana.blit(text, (650, 10))

    # Pintamos los sprites (pelota,raqueta,ladrillos)

    grupo_sprites.draw(ventana)

    # UPDATE

    pygame.display.update()
    pygame.time.Clock().tick(FPS)

pygame.quit()
