from colores import Colores
import pygame

class Ventana:
    def __init__(self, ancho=800, alto=600, color_fondo=Colores.AZULOSCURO, fuente_tipo="None", fuente_tamaño=35, reloj_tick=60):
        self.ancho = ancho
        self.alto = alto
        self.color_fondo = color_fondo
        self.ventana = pygame.display.set_mode([ancho,alto])
        pygame.display.set_caption("Juego Breakout")
        self.fuente = pygame.font.SysFont(fuente_tipo,fuente_tamaño)
        self.reloj = pygame.time.Clock()
        self.reloj_tick = reloj_tick

    def refresca_fondo(self):
        self.ventana.fill(self.color_fondo)
        pygame.draw.line(self.ventana, Colores.BLANCO, [0, 38], [800, 38], 2)

    def pinta_objetos(self, grupo_sprites):                             
        grupo_sprites.draw(self.ventana)  

    def actualiza_pantalla(self,grupo_sprites,puntuacion, vidas):
        self.refresca_fondo()
        self.pinta_objetos(grupo_sprites) 
        self.pinta_puntuacion(puntuacion,vidas)  

        self.reloj.tick(self.reloj_tick)
        pygame.display.update()

    def pinta_puntuacion(self, puntuacion, vidas ):
                 #Display the score and the number of lives at the top of the screen
        
        text = self.fuente.render("Puntos: " + str(puntuacion), 1, Colores.BLANCO)
        self.ventana.blit(text, (20,10))
        text = self.fuente.render("IES Ramon LLull ", 1, Colores.BLANCO)
        self.ventana.blit(text, (300,10))
        text = self.fuente.render("Vidas: " + str(vidas), 1, Colores.BLANCO)
        self.ventana.blit(text, (650,10))

    def pinta_nivelcompletado(self):
        font = pygame.font.Font(None, 74)
        text = font.render("NIVEL COMPLETADO", 1, Colores.BLANCO)
        self.ventana.blit(text, (200, 300))
        pygame.display.flip()
        pygame.time.wait(3000)

    def pinta_gameover(self):
        font = pygame.font.Font(None, 74)
        text = font.render("GAME OVER", 1, Colores.BLANCO)
        self.ventana.blit(text, (250, 300))
        pygame.display.flip()
        pygame.time.wait(3000)