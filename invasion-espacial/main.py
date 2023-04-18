import pygame
import random

#Inicializando Pygame
pygame.init()

#Creando pantalla de juego
pantalla = pygame.display.set_mode((800, 600))

#Titulo e icono
pygame.display.set_caption("Invasion Espacial")
icono = pygame.image.load("ovni.png")
pygame.display.set_icon(icono)
fondo = pygame.image.load("fondo.jpg")

#Variables jugador
img_jugador = pygame.image.load("cohete.png")
pjugador_x = 368
pjugador_y = 536
pjugadorx_cambio = 0

#Variables enemigo
img_enemigo = pygame.image.load("enemigo.png")
penemigo_x = random.randint(0, 736)
penemigo_y = random.randint(50, 200)
penemigox_cambio = 1
penemigoy_cambio = 50


#Funcion jugador
def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))


#Funcion enemigo
def enemigo(x, y):
    pantalla.blit(img_enemigo, (x, y))


#Loop del juego
se_ejecuta = True
while se_ejecuta:

    #RGB (COLORES PANTALLA)
    pantalla.blit(fondo, (0, 0))
    #ITERANDO EVENTOS
    for evento in pygame.event.get():
        #BUCLE PARA CERRAR PROGRAMA
        if evento.type == pygame.QUIT:
            se_ejecuta = False
        #CONDICION PARA MOVER JUGADOR
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                pjugadorx_cambio = -1
            if evento.key == pygame.K_RIGHT:
                pjugadorx_cambio = 1

        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                pjugadorx_cambio = 0

    #MODIFICAR UBICACION DEL JUGADOR
    pjugador_x += pjugadorx_cambio

    # MODIFICAR UBICACION DEL ENEMIGO
    penemigo_x += penemigox_cambio

    # MANTENER ENEMIGO DENTRO DE LA PANTALLA
    if penemigo_x <= 0:
        penemigox_cambio = 0.4
        penemigo_y += penemigoy_cambio
    elif penemigo_x >= 736:
        penemigox_cambio = -0.4
        penemigo_y += penemigoy_cambio

    #MANTENER JUGADOR DENTRO DE LA PANTALLA
    if pjugador_x <= 0:
        pjugador_x = 0
    elif pjugador_x >= 736:
        pjugador_x = 736

    jugador(pjugador_x, pjugador_y)
    enemigo(penemigo_x, penemigo_y)
    #ACTUALIZACION/SIEMPRE VA ULTIMO
    pygame.display.update()
