import pygame
from pygame import Vector2

class Soleil:
    def __init__(self):
        self.position = Vector2(400,400)
        self.rayon = 40
        self.couleur = (255,255,0)
        self.masse = 10

    def draw(self, screen):
        pygame.draw.circle(screen, self.couleur, self.position, self.rayon)

