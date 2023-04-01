import pygame
from pygame.locals import *
from random import randint, choice, uniform
import math, characters, cam

screen = pygame.display.set_mode((800,600))

camera = cam.Camera(4, screen)

def render():
    screen.fill((0,0,255))
    
    
    pygame.draw.rect(screen, (255,0,0),pygame.Rect(50 - camera.scroll[0],50 - camera.scroll[1], 200,200))

    characters.plr.update(screen, camera.scroll)
    
    camera.follow(characters.plr, 1, speed= 32,)

