import pygame

class Plataformas:
    def __init__(self, posicion, path):
        self.imagen = pygame.image.load(path)
        self.rect = self.imagen.get_rect()
        self.rect.x = posicion[0]
        self.rect.y = posicion[1]
        self.hitbox = pygame.Rect(posicion[0], posicion[1], self.rect.width, self.rect.height)

    def generar_estructura(self, surface):
        surface.blit(self.imagen, self.rect)