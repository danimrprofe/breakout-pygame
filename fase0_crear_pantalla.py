# IMPORTACIONES
import pygame

# MEDIDAS

VENTANA_HORI = 800  # Ancho de la ventana
VENTANA_VERT = 600  # Alto de la ventana
FPS = 60  # Fotogramas por segundo

# COLORES

BLANCO = (255,255,255)
AZULOSCURO = (36,90,190)

# DATOS

puntuacion = 0
vidas = 9999

# INICIAR PYGAME

pygame.init()
ventana = pygame.display.set_mode((VENTANA_HORI, VENTANA_VERT))
pygame.display.set_caption("Juego Breakout")
fuente = pygame.font.Font(None, 34)

def main():
 
    # BUCLE PRINCIPAL   

    sigueJugando = True
    while sigueJugando:

        # EVENTOS

        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                    sigueJugando = False 
            elif event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_x: 
                        sigueJugando = False
        
        

        # LOGICA DEL PROGRAMA
        

        # IMAGENES
        
        ventana.fill(AZULOSCURO)
        pygame.draw.line(ventana, BLANCO, [0, 38], [800, 38], 2)
        text = fuente.render("Puntos: " + str(puntuacion), 1, BLANCO)
        ventana.blit(text, (20,10))
        text = fuente.render("IES Ramon LLull ", 1, BLANCO)
        ventana.blit(text, (300,10))
        text = fuente.render("Vidas: " + str(vidas), 1, BLANCO)
        ventana.blit(text, (650,10))

        # UPDATE
            
        pygame.display.update()
        pygame.time.Clock().tick(FPS)
        
    pygame.QUIT
        


if __name__ == "__main__":
    main()
