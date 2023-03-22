import pygame 
from pygame.locals import *
from game import render


clock = pygame.time.Clock()
fps = 144 

run = True
while run:
    clock.tick(fps)

    render()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            
            print("quit")
            
            run = False

    pygame.display.flip()