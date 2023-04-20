import pygame
import random
import math
from pygame import mixer
import io

#Inicializando Pygame
pygame.init()

#Creando pantalla de juego
pantalla = pygame.display.set_mode((800, 600))

#agregando musica de fondo
mixer.music.load("MusicaFondo.mp3")
mixer.music.set_volume(0.2)
mixer.music.play(-1)


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
img_enemigo = []
penemigo_x = []
penemigo_y = []
penemigox_cambio = []
penemigoy_cambio = []
cantidad_enemigos = 6

for e in range(cantidad_enemigos):
    img_enemigo.append(pygame.image.load("enemigo.png"))
    penemigo_x.append(random.randint(0, 736))
    penemigo_y.append(random.randint(50, 200))
    penemigox_cambio.append(1)
    penemigoy_cambio.append(15)

#Variables balas
img_bala = pygame.image.load("bala.png")
pbala_x = 0
pbala_y = 500
pbalax_cambio = 0
pbalay_cambio = 1
bala_visible = False

#Variabel puntaje

puntaje = 0
fuente = pygame.font.Font("freesansbold.ttf", 32)
texto_x = 10
texto_y = 10


#funcion textofinal
fuente_final = pygame.font.Font("freesansbold.ttf", 40)


#funcion para convertir fuente a byte
def fuente_byte(fuente):
    with open(fuente, "rb") as f:
        ttf_bytes = f.read()
    return io.BytesIO(ttf_bytes)

#almanecando funcion en una variable
fuente_a_bytte = fuente_byte("FreeSansBold.ttf")


def texto_final():
    mi_fuente_final = fuente_final.render("Fin del juego", True, (255, 255, 255))
    pantalla.blit(mi_fuente_final, (60, 200))


#funcion mostrar puntaje
def mostrar_puntaje(x, y):
    texto = fuente.render(f"Puntaje: {puntaje}", True, (255, 255, 255))
    pantalla.blit(texto, (x, y))


#Funcion jugador
def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))


#Funcion enemigo
def enemigo(x, y, ene):
    pantalla.blit(img_enemigo[ene], (x, y))


#funcion dispara bala
def disparar_bala(x, y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala, (x + 16, y + 10))


#funcion para detectar colisiones
def hay_colision(x1, y1, x2, y2):
    distancia = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
    if distancia < 27:
        return True
    else:
        return False


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
            if evento.key == pygame.K_SPACE:
                sonido_bala = mixer.Sound("disparo.mp3")
                sonido_bala.play()
                if not bala_visible:
                    pbala_x = pjugador_x
                    disparar_bala(pbala_x, pbala_y)

        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                pjugadorx_cambio = 0

    #MODIFICAR UBICACION DEL JUGADOR
    pjugador_x += pjugadorx_cambio

    # MODIFICAR UBICACION DEL ENEMIGO
    for e in range(cantidad_enemigos):
        if penemigo_y[e] > 395:
            for k in range(cantidad_enemigos):
                penemigo_y[k] = 1000
            texto_final()
            break

        penemigo_x[e] += penemigox_cambio[e]

    # MANTENER ENEMIGO DENTRO DE LA PANTALLA
        if penemigo_x[e] <= 0:
            penemigox_cambio[e] = 0.4
            penemigo_y[e] += penemigoy_cambio[e]
        elif penemigo_x[e] >= 736:
            penemigox_cambio[e] = -0.4
            penemigo_y[e] += penemigoy_cambio[e]

            # VERFICIACION COLISION

        colision = hay_colision(penemigo_x[e], penemigo_y[e], pbala_x, pbala_y)
        if colision:
            sonido_colision = mixer.Sound("Golpe.mp3")
            sonido_colision.play()
            pbala_y = 500
            bala_visible = False
            puntaje += 1
            penemigo_x[e] = random.randint(0, 736)
            penemigo_y[e] = random.randint(50, 200)

        enemigo(penemigo_x[e], penemigo_y[e], e)

    #MANTENER JUGADOR DENTRO DE LA PANTALLA
    if pjugador_x <= 0:
        pjugador_x = 0
    elif pjugador_x >= 736:
        pjugador_x = 736

    #MOVIMIENTO DE BALA
    if pbala_y <= -64:
        pbala_y = 500
        bala_visible = False

    if bala_visible:
        disparar_bala(pbala_x, pbala_y)
        pbala_y -= pbalay_cambio


    jugador(pjugador_x, pjugador_y)

    mostrar_puntaje(texto_x, texto_y)

    #ACTUALIZACION/SIEMPRE VA ULTIMO
    pygame.display.update()
