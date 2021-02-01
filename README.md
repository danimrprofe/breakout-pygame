# breakout-pygame
Juego breakout hecho con pygame. 

Podemos encontrar las instrucciones originales aquí: https://atariage.com/manual_html_page.php?SoftwareID=889

# Objetos

En primer lugar, como vamos a utilizar programación orientada a objetos, vamos a ver qué objetos tenemos en nuestro juego:

- La pelota
- La raqueta
- Los bloques (todos son "iguales")

Para ello, crearemos una clase que definirá cada objeto. De esta forma, cada clase será una archivo diferente y lo podremos modificar sin cambiar el archivo principal, además de poder reutilizarlos.

- raqueta.py
- pelota.py
- bloque.py

# El archivo principal

Crearemos también un archivo main.py que va a contener la lógica principal del juego.

# El objeto raqueta

El objeto raqueta deberá ser un rectángulo que:

- Se mueve de derecha a izquierda 
- Actualiza su posición cada vez
- Obedece al teclado para desplazarse
- No hace nada si toca algún objeto

# El objeto pelota

El objeto pelota será un cuadrado que:

- Se mueve alrededor de la pantalla en todas direcciones, por lo que necesita actualizar su posición constantemente
- Rebota contra la pared o contra la raqueta, por lo que se tiene que calcular una nueva dirección

# El objeto bloque

El objeto bloque es el más sencillo puesto que es un rectángulo que:

- Se posiciona en un lugar concreto y no se mueve
- Desaparece si choca una pelota contra él

# Lógica del juego

## Setup (una vez al comenzar)

1. Crear pelota
2. Crear raqueta
3. Crear bloques
4. Agregarlos todos a un gruop
5. Agregar los bloques a un grupo solo con los bloques

## Bucle principal

6. Detectar teclado y mover raquete si es necesario
7. Comprobar rebote de la pelota con las paredes
8. Comprobar si la pelota colisiona con la raqueta
9. Comprobar si la pelota colisiona con algún bloque
10. Eliminar los bloques que han sido tocados y en consecuencia, actualizar el marcador y comprobar si hemos ganado o perdido

# Colisiones

Es importante comprobar si dos objetos chocan (colisionan) para saber si:

- Tienen que rebotar
- Tiene que desaparecer o cambiar

Para comprobar si la pelota choca con algún bloque, utilizaremos la función "spritecollide".

- Encuentra sprites en un grupo (grupo bloques) que colisionan con otro sprite (pelota).
- Devuelve una lista que contiene todos los Sprites de un grupo que han colisionado con otro Sprite. 
- La intersección se determina comparando el atributo Sprite.rect de cada Sprite. Todos los sprites deben tener un valor "rect", que es un rectángulo del área del sprite, que se utilizará para calcular la colisión.
- El argumento de dokill es una booleano. Si se establece en Verdadero, todos los Sprites que colisionen se eliminarán del Grupo.


