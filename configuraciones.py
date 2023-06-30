import pygame

def girar_imagenes(lista_original, flip_x, flip_y):
    lista_girada = []
    
    for imagen in lista_original:
        lista_girada.append(pygame.transform.flip(imagen, flip_x, flip_y))
    
    return lista_girada

def rescalar_imagenes(lista_imagenes, W, H):
    for i in range(len(lista_imagenes)):
        lista_imagenes[i] = pygame.transform.scale(lista_imagenes[i], (W, H))

def obtener_rectangulo(principal):
    diccionario = {}
    diccionario["main"] = principal
    diccionario["bottom"] = pygame.Rect(principal.left, principal.bottom - 10, principal.width, 10)
    diccionario["right"] = pygame.Rect(principal.right - 2, principal.top, 2, principal.height)
    diccionario["left"] = pygame.Rect(principal.left, principal.top, 2, principal.height)
    diccionario["top"] = pygame.Rect(principal.left, principal.top, principal.width, 10)
    return diccionario

personaje_quieto = [
                    pygame.image.load("Parcial-PyGame\Movimientos\Sprites_quieto/0.png"),
                    pygame.image.load("Parcial-PyGame\Movimientos\Sprites_quieto/1.png"),
                    pygame.image.load("Parcial-PyGame\Movimientos\Sprites_quieto/2.png"),
                    pygame.image.load("Parcial-PyGame\Movimientos\Sprites_quieto/3.png"),
                    pygame.image.load("Parcial-PyGame\Movimientos\Sprites_quieto/4.png"),
                    pygame.image.load("Parcial-PyGame\Movimientos\Sprites_quieto/5.png"),
                    pygame.image.load("Parcial-PyGame\Movimientos\Sprites_quieto/6.png")
                    ]

personaje_moviendose = [
                    pygame.image.load("Parcial-PyGame\Movimientos\Sprites_caminar/0.png"),
                    pygame.image.load("Parcial-PyGame\Movimientos\Sprites_caminar/1.png"),
                    pygame.image.load("Parcial-PyGame\Movimientos\Sprites_caminar/2.png"),
                    pygame.image.load("Parcial-PyGame\Movimientos\Sprites_caminar/3.png"),
                    pygame.image.load("Parcial-PyGame\Movimientos\Sprites_caminar/4.png"),
                    pygame.image.load("Parcial-PyGame\Movimientos\Sprites_caminar/5.png"),
                    pygame.image.load("Parcial-PyGame\Movimientos\Sprites_caminar/6.png")
                    ]

personaje_salta = [
                    pygame.image.load("Parcial-PyGame\Movimientos\Sprites_saltar/0.png"),
                    pygame.image.load("Parcial-PyGame\Movimientos\Sprites_saltar/1.png"),
                    pygame.image.load("Parcial-PyGame\Movimientos\Sprites_saltar/2.png"),
                    pygame.image.load("Parcial-PyGame\Movimientos\Sprites_saltar/3.png"),
                    pygame.image.load("Parcial-PyGame\Movimientos\Sprites_saltar/4.png"),
                    pygame.image.load("Parcial-PyGame\Movimientos\Sprites_saltar/5.png"),
                    pygame.image.load("Parcial-PyGame\Movimientos\Sprites_saltar/6.png"),
                    pygame.image.load("Parcial-PyGame\Movimientos\Sprites_saltar/7.png")
                    ]

personaje_golpea = [
                    pygame.image.load("Parcial-PyGame\Movimientos\Sprite_golpear/0.png"),
                    pygame.image.load("Parcial-PyGame\Movimientos\Sprite_golpear/1.png"),
                    pygame.image.load("Parcial-PyGame\Movimientos\Sprite_golpear/2.png"),
                    pygame.image.load("Parcial-PyGame\Movimientos\Sprite_golpear/3.png"),
                    pygame.image.load("Parcial-PyGame\Movimientos\Sprite_golpear/4.png"),
                    pygame.image.load("Parcial-PyGame\Movimientos\Sprite_golpear/5.png")
                    ]

personaje_patea = [
                    pygame.image.load("Parcial-PyGame\Movimientos\Sprite_patada/0.png"),
                    pygame.image.load("Parcial-PyGame\Movimientos\Sprite_patada/1.png"),
                    pygame.image.load("Parcial-PyGame\Movimientos\Sprite_patada/2.png"),
                    pygame.image.load("Parcial-PyGame\Movimientos\Sprite_patada/3.png"),
                    pygame.image.load("Parcial-PyGame\Movimientos\Sprite_patada/4.png")
                    ]