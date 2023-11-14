import pygame, sys
from pygame.locals import *
import random
# from main import FPSCLOCK

fade = 4
fade_in_color = [0,0,0]
fade_out_color = [242, 201, 78]
hide = False
rgb_ticks = 0
# animation_pause = False
FPSCLOCK = pygame.time.Clock()
#Set up pygame
pygame.init()

surface = pygame.display.set_mode((800,600))




font = pygame.font.SysFont('Consolas', 20)
# img = font.render('Enemy Smashed!', True, (255,255,255))








#Run the game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    # for i in range(fade):

    # if animation_pause == False:
    # fade_in_color[0] =  fade_in_color[0]-fade
    # fade_in_color[1] = fade_in_color[1]-fade
    # fade_in_color[2] = fade_in_color[2]-fade

    if fade_in_color[0] < fade_out_color[0]:
      fade_in_color[0] += fade
      
      if fade_in_color[1] < fade_out_color[1]:
        fade_in_color[1] += fade
        
        if fade_in_color[2] < fade_out_color[2]:
          fade_in_color[2] += fade
          
          
    # if rgb_ticks == 3:
    #   hide = True

    print(fade_in_color)
    img = font.render('+1', True, (fade_in_color[0],fade_in_color[1],fade_in_color[2]))
    # if hide != True:
    surface.blit(img, (800/2-img.get_rect().centerx, 100))
    FPSCLOCK.tick(60)
      
    
    pygame.display.update()