import pygame
import random

# Inicializar paygame
pygame.init()

#crear la pantalla
pantalla = pygame.display.set_mode((800,600))

# Titulo e icono
pygame.display.set_caption("Invasion Espacial")
icono = pygame.image.load("135. ovni.png")
pygame.display.set_icon(icono)

# Variables Jugador

img_jugador = pygame.image.load("136. cohete.png")
jugador_x=368
jugador_y=500
jugador_x_cambio=0

# Variables Enemigo

img_enemigo = pygame.image.load("140. enemigo.png")
enemigo_x=random.randint(0,736)
enemigo_y=random.randint(50,200)
enemigo_x_cambio=0.3
enemigo_y_cambio=50


#Funcion jugador
def jugador(x,y):
    pantalla.blit(img_jugador,(x,y))

#Funcion enemigo
def enemigo(x,y):
    pantalla.blit(img_enemigo,(x,y))

#Loop del juego
se_ejecuta=True
while se_ejecuta:

#RGB pantalla
    pantalla.fill((0, 144, 228))

#Iterar eventos
    for evento in pygame.event.get():

#Evento cerrar juego
        if evento.type == pygame.QUIT:
            se_ejecuta = False

#Evento presionar teclas
        if evento.type==pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio = -0.3
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0.3

#Evento soltar teclas
        if evento.type==pygame.KEYUP:
            if evento.key==pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0

#Modificar ubicacion jugador
    jugador_x+=jugador_x_cambio

#Mantener dentro de bordes al jugador

    if jugador_x <=0:
        jugador_x=0
    elif jugador_x >=736:
        jugador_x=736

#Modificar ubicacion del enemigo
    enemigo_x += enemigo_x_cambio

#Mantener dentro de bordes al enemigo

    if enemigo_x <=0:
        enemigo_x_cambio=0.3
        enemigo_y += enemigo_y_cambio
    elif enemigo_x >=736:
        enemigo_x_cambio=-0.3
        enemigo_y += enemigo_y_cambio



    jugador(jugador_x,jugador_y)
    enemigo(enemigo_x,enemigo_y)

#Actuaizar pantalla
    pygame.display.update()


