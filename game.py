import pygame
from pygame.locals import *
from random import randint, choice, uniform
import math, characters

screen = pygame.display.set_mode((800,600))

def render():
    screen.fill((0,0,255))

    characters.plr.update(screen)

