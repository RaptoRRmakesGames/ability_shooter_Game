import pygame
from pygame.locals import *
from random import randint, choice, uniform
import math, characters, cam

screen = pygame.display.set_mode((800,600))

test_block = characters.Block((100,200), (400,80), (255,255,255))
test_block2 = characters.Block((100,150), (400,80), (255,0,255))

camera = cam.Camera(4, screen)

def checkcollide(it1, it2, tolerance=115):
    
    if it1.rect.colliderect(it2.rect):
        if abs(it2.rect.top - it1.rect.bottom) < tolerance:
            return {"bottom" : True, "left" : False,"right" : False,"top" : False,}
        
        elif abs(it2.rect.bottom - it1.rect.top) < tolerance:
            return {"bottom" : False, "left" : False,"right" : False,"top" : True,}
        
        elif abs(it2.rect.right - it1.rect.left) < tolerance:
            return {"bottom" : False, "left" : True,"right" : False,"top" : False,}
        
        elif abs(it2.rect.left - it1.rect.right) < tolerance:
            return {"bottom" : False, "left" : False,"right" : True,"top" : False,}
        
        return {"bottom" : False, "left" : False,"right" : False,"top" : False,}
        

        

def render():
    screen.fill((0,0,255))
    
    test_block.update(screen, camera.scroll)
    test_block2.update(screen, camera.scroll)

    characters.plr.update(screen, camera.scroll)
    pygame.draw.rect(screen, (25,25,25), characters.plr.rect)
    
    
    
    camera.follow(characters.plr, 1, speed= 1,)


def collisions():
    
    if characters.plr.rect.colliderect(test_block.rect):
        if abs(test_block.rect.bottom - characters.plr.rect.top) > 5:
            characters.plr.position.y -= characters.plr.velocity.y + 0.5
            characters.plr.velocity.y = 0
            print("yes2")
        if abs(test_block.rect.top - characters.plr.rect.bottom) > 5:
            characters.plr.position.y += characters.plr.velocity.y + 0.5
            characters.plr.velocity.y = 0
            print("yes2") 
        print("YEs")
