
# from asyncio.tasks import _T1
from os import environ
from pickle import TRUE
import random
# from re import T
from threading import Thread
import threading

import sys
from turtle import Turtle
import gameSprites
import pygame
from  pygame.locals import *


bullet_width = 10
bullet_height = 33
spaceship_width = 50
spaceship_height = 62

pygame.init()

pygame.mouse.set_visible(False)


fr_width =  1000
fr_height = 600
FPS = 60  
FPSCLOCK = pygame.time.Clock()



background = pygame.image.load('./assets/img/background.jpg')
spaceship = pygame.image.load('./assets/img/plane.png')
dummy  = pygame.image.load('./assets/img/star.png')
dummy = pygame.transform.rotate(dummy, 180)


spaceship_velocity = 10
bullets = []
enemies = []
enemybullets = []
# total_score = 0
# score_per_bullet = 0

is_bullet = False
is_enemies = False
is_colorchange = False
explosion = [False,0]

surface = pygame.display.set_mode((fr_width,fr_height))
surface.blit(background,(0,0))

spaceship = gameSprites.Spaceship(surface)
tk = gameSprites.Ticker(50,1)
en_ticker = gameSprites.Ticker(100,1)
event_ticker = gameSprites.Ticker(100,1)
event_is_there = False
exp_frames = []
for i in range(1,6):
    exp_frames.append(pygame.image.load(f'./assets/img/explosion/exp{i}.png'))    
score = gameSprites.Score(surface,fr_width,fr_height)

# score_show = True


def Explode():
    pass
        
def Quit(var):
    '''
    Task: Quits The Game 
    If:
    You Give True
    If:
    You Give False
    It Resumes The Game
    '''
    if (var == True):
        pygame.quit()
        sys.exit()

def GameLoose():
    if spaceship.spaceship_is_alive == False:
        font = pygame.font.SysFont('Comic Sans ms', 50)
        img = font.render('You Lost!', True, (255,255,255))
        surface.blit(img, (fr_width/2-img.get_rect().centerx, fr_height/2-img.get_rect().centery))
        pygame.display.update()
        




gameon = False

some_x_pos = random.randint(10,fr_width-100)
some_y_pos = random.randint(100,500)

    
while True:
    
    if gameon == False:
    
        surface.blit(background,(0,0))
        surface.blit(dummy,(some_x_pos,some_y_pos))
        if en_ticker.isticksOver():
            dummy = pygame.transform.rotate(dummy, 180)
            some_x_pos = random.randint(10,fr_width-100)
            some_y_pos = random.randint(100,500)
            surface.blit(dummy,(some_x_pos,some_y_pos))

        font = pygame.font.SysFont('Comic Sans ms', 50)
        img = font.render('Welcome to', True, (255,255,255))
        surface.blit(img, (fr_width/2-img.get_rect().centerx, fr_height/2-img.get_rect().centery-100))
        pygame.mouse.set_visible(True)
        font = pygame.font.SysFont('Comic Sans ms', 50)
        img = font.render('Space Invaders', True, (255,255,255))
        surface.blit(img, (fr_width/2-img.get_rect().centerx, fr_height/2-img.get_rect().centery))
        # pygame.mouse.set_visible(True)
        font = pygame.font.SysFont('Comic Sans ms', 25)
        img = font.render('Press the Space bar on your keyboard to Play ', True, (232, 92, 49))
        surface.blit(img, (fr_width/2-img.get_rect().centerx, fr_height/2-img.get_rect().centery+100))
        # pygame.mouse.set_visible(True)
    else:
        pygame.mouse.set_visible(False)
        surface.blit(background,(0,0))
        score.ChangeColor((255,255,255))
        spaceship.Move()
        GameLoose()
        if is_colorchange:
            color_ticker.tick()
    
            if color_ticker.isticksOver():
                score.ChangeColor((255,255,255))

        if spaceship.spaceship_is_alive:

            if tk.isticksOver() == True:
                if len(enemies) > 0:
                    for en in enemies:
                        en.Shoot()


            if en_ticker.isticksOver() == True:
                en = gameSprites.Enemy(surface,random.randint(10,fr_width-75),0)
                enemies.append(en)
                en = None
                is_enemies = True  



        if spaceship.spaceship_is_alive == True:
            score.update()

        if is_enemies == True:
            for enemy in enemies:

                enemy.Move()
                enemy.MoveEnemybullets()
               
                #checking spaceship collided with enemy bullets
                enemybullets = spaceship.isCollided(enemy.enemybullets)
                
                if enemy.isBulletsCollided(bullets):
                    is_colorchange = True
                    color_ticker = gameSprites.Ticker(200,1)
                    score.ChangeColor((237, 207, 36))
                    score.add(5)                
                
                #checking enemy and player bullets collided
                if len(bullets) > 0:
                    if enemy.isEnemyCollided(enemies,bullets):
                        is_colorchange = True
                        color_ticker = gameSprites.Ticker(200,1)
                        score.ChangeColor((237, 207, 36))
                        score.add(10)
         
                    
                        
    
        if len(bullets) > 0:
            for bl in bullets:
                bl.Move()



    for event in pygame.event.get():
        if event.type == QUIT:
            Quit()

        elif event.type == MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0] == True:
                if spaceship.spaceship_is_alive:
                    bullet = gameSprites.Bullet(surface)
                    is_bullet = True
                    bullets.append(bullet)
                    bullet = None

        

        elif event.type == KEYDOWN:
            if event.key == K_SPACE:
                if gameon == False:
                    gameon = True
                elif gameon:
                    bullet = gameSprites.Bullet(surface)
                    is_bullet = True
                    bullets.append(bullet)
                    bullet = None
   

    pygame.display.update()
    FPSCLOCK.tick(60)
    tk.tick()
    if event_is_there == True:
        event_ticker.tick()
        print('showing')
        font = pygame.font.SysFont('Comic Sans ms', 25)
        img = font.render('Enemy Smashed ', True, (232, 92, 49))
        surface.blit(img, (fr_width/2-img.get_rect().centerx, 100))
    if event_ticker.isticksOver() == True:
        event_is_there = False


    en_ticker.tick()
    
