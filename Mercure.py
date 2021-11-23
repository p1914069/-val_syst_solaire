import pygame
from pygame import Vector2
import random

class Mercure:
    def __init__(self):
        self.position = Vector2(random.randint(50, 750),random.randint(50, 750))
        self.rayon = 14
        self.couleur = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.masse = 3.285e23
        self.vitesse = Vector2(0,0)

    def draw(self, screen):
        pygame.draw.circle(screen, self.couleur, self.position, self.rayon)

