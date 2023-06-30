import pygame
import sys
from configuraciones import *
from class_personaje import Personaje
from Generar_plataforma import *
from modo import *

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

pygame.init()

def actualizar_pantalla(pantalla, un_personaje, fondo, lados_piso):
    pantalla.blit(fondo, (0, 0))
    un_personaje.update(pantalla, lados_piso)

# Configuración
W, H = 1280, 720
TAMAÑO_PANTALLA = (W, H)
FPS = 20
RELOJ = pygame.time.Clock()
# Pantalla
screen = pygame.display.set_mode(TAMAÑO_PANTALLA)

# Fondo
plataforma = pygame.draw.rect(screen, AZUL, (20,200,300,5))
fondo = pygame.image.load("Parcial-PyGame/Fondo jueguito.png")
fondo = pygame.transform.scale(fondo, TAMAÑO_PANTALLA)

# Personaje
posicion_inicial = (13, 560)
tamaño = (75, 85)

diccionario_animaciones = {}
diccionario_animaciones["quieto"] = personaje_quieto
diccionario_animaciones["salta"] = personaje_salta
diccionario_animaciones["golpear"] = personaje_golpea
diccionario_animaciones["patea"] = personaje_patea
diccionario_animaciones["camina_derecha"] = personaje_moviendose
diccionario_animaciones["camina_izquierda"] = girar_imagenes(personaje_moviendose, True, False)

mi_personaje = Personaje(tamaño, diccionario_animaciones, posicion_inicial, 10)

# Plataforma

plataforma_flotante = Plataformas((480, 550), r"Parcial-PyGame/Plataformas/0.png")
plataforma_flotante2 = Plataformas((700, 550), r"Parcial-PyGame/Plataformas/0.png")

piso = pygame.Rect(0, 0, W, 20)
piso.top = mi_personaje.lados["main"].bottom
lados_piso = obtener_rectangulo(piso)

while True:
    RELOJ.tick(FPS)
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:  # Clic izquierdo del mouse
                posicion_clic = pygame.mouse.get_pos()
                print("Posición del clic: X =", posicion_clic[0], "Y =", posicion_clic[1])
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_TAB:
                cambiar_modo()
    
    screen.blit(fondo, (0, 0))
    
    actualizar_pantalla(screen, mi_personaje, fondo, lados_piso)
    
    for plataforma in [plataforma_flotante, plataforma_flotante2]:
        plataforma.generar_estructura(screen)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        mi_personaje.que_hace = "derecha"
    elif keys[pygame.K_LEFT]:
        mi_personaje.que_hace = "izquierda"
    elif keys[pygame.K_UP]:
        mi_personaje.que_hace = "salta"
    elif keys[pygame.K_j]:
        mi_personaje.que_hace = "golpear"
    elif keys[pygame.K_k]:
        mi_personaje.que_hace = "patea"
    else:
        mi_personaje.que_hace = "quieto"
    
    mi_personaje.aplicar_gravedad(screen, lados_piso)
    
    for plataforma in [plataforma_flotante, plataforma_flotante2]:
        if mi_personaje.lados["bottom"].colliderect(plataforma.hitbox):
            mi_personaje.que_hace = "quieto"  # El personaje se queda quieto en la plataforma
            mi_personaje.lados["main"].bottom = plataforma.hitbox.top - mi_personaje.alto
            
    if get_modo():
        for lado in lados_piso:
            pygame.draw.rect(screen, "Blue", lados_piso[lado], 3)
        for lado in mi_personaje.lados:
            pygame.draw.rect(screen, "Orange", mi_personaje.lados[lado], 3)
        
    pygame.display.flip()
    pygame.display.update()