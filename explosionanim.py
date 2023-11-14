import pygame, sys
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello World!')
clock = pygame.time.Clock()

exp_frames = []



    


ticker = 0
while True: # main game loop

    DISPLAYSURF.fill((0,0,0))
    
    for i in range(1,6):
        exp_frames.append(pygame.image.load(f'./assets/img/explosion/exp{i}.png'))    

    for frames in exp_frames:
        
        if ticker <= 4:
            DISPLAYSURF.blit(frames,(150,200))
            ticker += 1
            clock.tick(10)
            pygame.display.update()
        
    


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    clock.tick(10)
    pygame.display.update()