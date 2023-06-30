import pygame
class imagen:
    def __init__(self, tamaño, origen, path_imagen):
        self.imagen = pygame.image.load(path_imagen)
        self.imagen = pygame.transform.scale(self.imagen, tamaño)
        self.rect = self.imagen.get_rect()
        self.rect.center = origen
    
    def mover_imagen(self, sentido: str, desplazamiento: int, tamaño_pantalla: tuple):
        if sentido == "horizontal-":
            self.rect.x -= desplazamiento
            if self.rect.right < 0:
                self.rect.left = tamaño_pantalla[0]
        elif sentido == "horizontal":
            self.rect.x += desplazamiento
            if self.rect.left > tamaño_pantalla[0]:
                self.rect.right = 0

    def detectar_colision(self, otra_imagen):
        if self.rect.colliderect(otra_imagen.rect):
            self.imagen.fill(self.color_colision)
            otra_imagen.imagen.fill(otra_imagen.color_colision)
        else:
            self.imagen.fill(self.color)
            otra_imagen.imagen.fill(otra_imagen.color)