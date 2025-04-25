import pygame
import sys

# Inicialización de Pygame
pygame.init()

# Configuración de la ventana
ANCHO = 600
ALTO = 800
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Evita los obstáculos")

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
CIAN = (0, 255, 255)
GRIS = (128, 128, 128)
AMARILLO = (255, 255, 0)

# Obstáculos
autos1 = 0
autos2 = 600
autos3 = 0
autos4 = 600
derecha = 2
izquierda = -2
derecha2 = 4
izquierda2 = -4
autos5 = 700
autos6 = 700
autos7 = 700
autos8 = 700

# Jugador
jugador_ancho = 40
jugador_alto = 40
jugador_x = 290
jugador_y = 750
jugador_velocidad = 5
jugador_rect = pygame.Rect(jugador_x, jugador_y, jugador_ancho, jugador_alto)

# Reloj
clock = pygame.time.Clock()
FPS = 60

# Bucle del juego
jugando = True
while jugando:
    clock.tick(FPS)
    ventana.fill(VERDE)

    # Movimiento de los obstáculos
    autos1 += derecha
    autos2 += izquierda
    autos3 += derecha
    autos4 += izquierda2
    autos5 += izquierda2
    autos6 += izquierda2
    autos7 += derecha2
    autos8 += izquierda2

    # Reiniciar la posición de los obstáculos al salir de la pantalla
    if autos1 >= ANCHO + 50:
        autos1 = -50
    if autos2 <= -50:
        autos2 = ANCHO + 50
    if autos3 >= ANCHO + 50:
        autos3 = -50
    if autos4 <= -50:
        autos4 = ANCHO + 50
    if autos5 <= -50:
        autos5 = ANCHO + 50
    if autos6 <= -50:
        autos6 = ANCHO + 50
    if autos7 >= ANCHO + 50:
        autos7 = -50
    if autos8 <= -50:
        autos8 = ANCHO + 50

    # Dibujar las carreteras
    pygame.draw.rect(ventana, GRIS, (0, 400, ANCHO, 100))
    pygame.draw.rect(ventana, GRIS, (0, 560, ANCHO, 100))
    pygame.draw.rect(ventana, NEGRO, (0, 500, ANCHO, 75))
    for x in range(50, ANCHO, 100):
        pygame.draw.rect(ventana, BLANCO, (x, 300, 80, 80))
        pygame.draw.polygon(ventana, ROJO, [(x, 300), (x + 40, 260), (x + 80, 300)])
        pygame.draw.rect(ventana, BLANCO, (x + 20, 330, 20, 20))

    # Movimiento del jugador
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        jugador_y -= jugador_velocidad
    if keys[pygame.K_s]:
        jugador_y += jugador_velocidad
    if keys[pygame.K_a]:
        jugador_x -= jugador_velocidad
    if keys[pygame.K_d]:
        jugador_x += jugador_velocidad
    if keys[pygame.K_LEFT]:
        jugador_x -= jugador_velocidad
    if keys[pygame.K_RIGHT]:
        jugador_x += jugador_velocidad
    if keys[pygame.K_UP]:
        jugador_y -= jugador_velocidad
    if keys[pygame.K_DOWN]:
        jugador_y += jugador_velocidad

    # Mantener al jugador dentro de los límites
    if jugador_x < 0:
        jugador_x = 0
    elif jugador_x > ANCHO - jugador_ancho:
        jugador_x = ANCHO - jugador_ancho
    if jugador_y < 0:
        jugador_y = 0
    elif jugador_y > ALTO - jugador_alto:
        jugador_y = ALTO - jugador_alto

    # Actualizar la posición del rectángulo del jugador
    jugador_rect.topleft = (jugador_x, jugador_y)

    # Crear rectángulos para los obstáculos
    auto1_rect = pygame.Rect(autos1, 420, 50, 50)
    auto2_rect = pygame.Rect(autos2, 420, 50, 50)
    auto3_rect = pygame.Rect(autos3, 420, 40, 40)
    auto4_rect = pygame.Rect(autos4, 420, 50, 50)
    auto5_rect = pygame.Rect(autos5, 600, 50, 50)
    auto6_rect = pygame.Rect(autos6, 600, 50, 50)
    auto7_rect = pygame.Rect(autos7, 600, 50, 50)
    auto8_rect = pygame.Rect(autos8, 600, 50, 50)

    obstaculos = [auto1_rect, auto2_rect, auto3_rect, auto4_rect,
                   auto5_rect, auto6_rect, auto7_rect, auto8_rect]

    # Detección de colisiones
    for obstaculo in obstaculos:
        if jugador_rect.colliderect(obstaculo):
            print("¡Colisión! Cerrando el juego.")
            jugando = False
            break

    # Dibujar todos los elementos
    pygame.draw.rect(ventana, AMARILLO, jugador_rect)
    pygame.draw.rect(ventana, AZUL, auto1_rect)
    pygame.draw.rect(ventana, ROJO, auto2_rect)
    pygame.draw.rect(ventana, CIAN, auto3_rect)
    pygame.draw.rect(ventana, ROJO, auto4_rect)
    pygame.draw.rect(ventana, ROJO, auto5_rect)
    pygame.draw.rect(ventana, AZUL, auto6_rect)
    pygame.draw.rect(ventana, ROJO, auto7_rect)
    pygame.draw.rect(ventana, CIAN, auto8_rect)

    # Manejo de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jugando = False

    # Actualizar ventana
    pygame.display.flip()

# Salir de Pygame
pygame.quit()
sys.exit()