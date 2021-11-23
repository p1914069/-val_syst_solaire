import pygame
from pygame.math import Vector2
import core

from Soleil import Soleil

from Mercure import Mercure
from Venus import Venus
from Terre import Terre
from Mars import Mars
from Jupiter import Jupiter
from Saturne import Saturne
from Uranus import Uranus
from Neptune import Neptune

def setup():
    print("Setup START---------")
    core.fps = 60
    core.WINDOW_SIZE = [800, 800]


    # Soleil
    core.memory("Soleil",Soleil())

    # Planètes
    core.memory("Mercure", Mercure())
    core.memory("Venus", Venus())
    core.memory("Terre", Terre())
    core.memory("Mars", Mars())
    core.memory("Jupiter", Jupiter())
    core.memory("Saturne", Saturne())
    core.memory("Uranus", Uranus())
    core.memory("Neptune", Neptune())

    core.memory("TableauDePlanètes", [Mercure(),Venus(),Terre(),Mars(),Jupiter(),Saturne(),Uranus(),Neptune()])

    # Pour calcul
    core.memory("Fg", 0.0)
    core.memory("g", 9.81)

def run ():
    # Dessin du soleil
    core.memory("Soleil").draw(core.screen)

    # Dessins des planètes
    for p in core.memory("TableauDePlanètes"):
        p.draw(core.screen)

    # Déplacement des planètes
    for p in core.memory("TableauDePlanètes"):
        p.Ux = core.memory("Soleil").position - (p.position)
        p.Ux = p.Ux.normalize()

        core.memory("Fg", core.memory("g") * ( (core.memory("Soleil").masse * p.masse)/(core.memory("Soleil").position.distance_to(p.position))))
        p.Ux = p.Ux * core.memory("Fg")
        p.vitesse = p.vitesse + p.Ux
        core.memory("Fg", 0.0)

        p.position = p.position + p.vitesse


core.main(setup, run)
