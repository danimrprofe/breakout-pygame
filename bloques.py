import pygame
from bloque import Bloque
from colores import Colores

BLACK = (0, 0, 0)

class Bloques():
    ''' Esta clase contiene un grupo de bloques y algunos métodos para trabajar con ellos '''

    def __init__(self, ventana):
        # Call the parent class (Sprite) constructor
        super().__init__()

        self.grupo = pygame.sprite.Group()
        self.bloquesDestruidos = 0
        self.bloqueAncho = 80
        self.bloqueAlto = 30
        self.separacionFilas = 40
        self.separacionColumnas = 100
        self.posicionPrimeraFila = 60
        self.posicionPrimeraColumna = 60
        self.bloquesPorFila = 7

        for i in range(self.bloquesPorFila):
            bloque = Bloque(Colores.ROJO, self.bloqueAncho, self.bloqueAlto)
            bloque.rect.x = self.posicionPrimeraColumna + i * self.separacionColumnas
            bloque.rect.y = self.posicionPrimeraFila
            self.grupo.add(bloque)
        for i in range(self.bloquesPorFila):
            bloque = Bloque(Colores.NARANJA, self.bloqueAncho, self.bloqueAlto)
            bloque.rect.x = self.posicionPrimeraColumna + i * self.separacionColumnas
            bloque.rect.y = self.posicionPrimeraFila + self.separacionFilas
            self.grupo.add(bloque)
        for i in range(self.bloquesPorFila):
            bloque = Bloque(Colores.AMARILLO,
                            self.bloqueAncho, self.bloqueAlto)
            bloque.rect.x = self.posicionPrimeraColumna + i * self.separacionColumnas
            bloque.rect.y = self.posicionPrimeraFila + 2*self.separacionFilas
            self.grupo.add(bloque)

    def quedanBloques(self):
        return len(self.grupo) == 0:
            return False
        else:
            return True

    def colisionBloques(self, pelota):
        bloques_golpeados = pygame.sprite.spritecollide(pelota, self.grupo, False)
        if not bloques_golpeados: self.bloquesDestruidos = 0
        else:
            for bloque in bloques_golpeados:
                self.bloquesDestruidos += 1
                pelota.rebotar()
                bloque.kill()
