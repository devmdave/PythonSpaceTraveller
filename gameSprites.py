# from typing_extensions import Self

from copyreg import constructor
from importlib.metadata import packages_distributions
from operator import truediv
from re import L, T
from sys import displayhook
from tkinter import W
from turtle import width
import pygame

bullet_width = 10
bullet_height = 33
spaceship_width = 50
spaceship_height = 62

class Bullet():
    def __init__(self,surface):
        self.bullet = pygame.image.load('./assets/img/bullet2.png')
        self.surface = surface
        self.bullet_rect = self.bullet.get_rect()
        self.bullet_rect.x = pygame.mouse.get_pos()[0]+spaceship_width/2-bullet_width/2
        self.bullet_rect.y = pygame.mouse.get_pos()[1]-bullet_height
        self.bullet_velocity = 10
        self.bullet_width = 10
        self.bullet_height = 33
    
    def Move(self):
        self.bullet_rect.y -= self.bullet_velocity
        self.surface.blit(self.bullet,(self.bullet_rect.x,self.bullet_rect.y))
    
    def getPos(self):
        return (self.bullet_rect.x,self.bullet_rect.y)

    def getRect(self):
        return self.bullet_rect

class Spaceship():
    def __init__(self,surface):
        self.spaceship = pygame.image.load('./assets/img/plane.png')
        self.spaceship_rect = self.spaceship.get_rect()
        self.spaceship_lives = 3
        self.spaceship_is_alive = True
        self.surface = surface
        self.bullets = []
    
    def Move(self):
        if self.spaceship_is_alive:
            self.spaceship_rect.x = pygame.mouse.get_pos()[0]
            self.spaceship_rect.y = pygame.mouse.get_pos()[1]
            self.surface.blit(self.spaceship,(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]))
        if len(self.bullets) > 0:
            for i in self.bullets:
                i.Move()

    def getRect(self):
        return self.spaceship_rect

    def Shoot(self):
        newbullet = Bullet(self.surface)
        self.bullets.append(newbullet)
        newbullet = None


              
    def isCollided(self,enbullets):
        if len(enbullets) > 0:
            
            for i in enbullets:
                if self.spaceship_rect.colliderect(i.getRect()):
                    self.spaceship_lives -= 1
                    enbullets.remove(i)
                    if self.spaceship_lives == 0:
                        self.spaceship_is_alive = False
                        pygame.mouse.set_visible(True)
                        
        return enbullets
                    

class EnemyBullet():      
    def __init__(self,surface,x,y):
        self.bullet = pygame.image.load('./assets/img/bullet2.png')
        self.bullet_rect = self.bullet.get_rect()
        self.surface = surface
        self.bullet_rect.x = x
        self.bullet_rect.y = y
        self.direction = "upward"
        self.bullet_velocity = 5
        
            
    def setVelocity(self,vel):
        self.bullet_velocity = vel
    
    def setDirection(self,dr):
        self.direction = dr
    
    def getPos(self):
        return (self.bullet_rect.x,self.bullet_rect.y)


    def Move(self):
        self.bullet_rect.y += self.bullet_velocity
        self.surface.blit(self.bullet,(self.bullet_rect.x,self.bullet_rect.y))
    
    def getRect(self):
        return self.bullet_rect

class Enemy():

    def __init__(self,surface,x,y):
        self.enemy = pygame.image.load('./assets/img/enemy.png')
        self.bg = pygame.image.load('./assets/img/background.jpg')
        self.enemy_rect = self.enemy.get_rect()
        self.enemy_rect.x = x
        self.enemy_rect.y = y
        
        self.enemyspaceship_width = 75
        self.enemyspaceship_height = 68
        self.enemy_velocity = 2
        self.surface = surface
        self.enemybullets = []
        self.life_counter = 0
   
    def Move(self):
        self.enemy_rect.y += self.enemy_velocity
        self.surface.blit(self.enemy,(self.enemy_rect.x,self.enemy_rect.y))
        

    def Shoot(self):
        self.bulletimg = pygame.image.load('./assets/img/bullet.png')
        newbullet = EnemyBullet(self.surface,self.enemy_rect.x+self.enemyspaceship_width/2,self.enemy_rect.y+self.enemyspaceship_height)
        self.enemybullets.append(newbullet)
        newbullet = None
        
    def MoveEnemybullets(self):
        if len(self.enemybullets) > 0:
            for bl in self.enemybullets:
                if bl.getPos()[1] >= 600:
                    self.enemybullets.remove(bl)
                else:
                    bl.Move()

    def getAllBullets(self):
        if len(self.enemybullets) > 0:
            return self.enemybullets
            
        else:
            return None

    def isBulletsCollided(self,plbull):
        
        if len(plbull) > 0 and len(self.enemybullets) > 0:
            for i in plbull:
                for j in self.enemybullets:
                    if i.getRect().colliderect(j.getRect()):
                        plbull.remove(i)
                        self.enemybullets.remove(j)
                        return True
 

    def getRect(self):
        return self.enemy_rect
    
    def isEnemyCollided(self,enemies,plbull):
        
        if len(enemies) > 0:
            for i in plbull:
                for j in enemies:
                    if i.getRect().colliderect(j.getRect()):
                        self.life_counter += 1
                        if self.life_counter == 3:
                            self.life_counter = 0
                            enemies.remove(j)
                            plbull.remove(i)
                            return True       
                        plbull.remove(i)
        
                


    
class Ticker():
    def __init__(self,ticks,tickspeed):
        self.total_ticks = ticks
        self.speed_of_tick = tickspeed
        self.timeOver = True
        self.tick_counter = 0
       
    def tick(self):
        if self.isticksOver() != True:
            self.tick_counter = self.tick_counter+self.speed_of_tick
        elif self.isticksOver() == True:
            self.tick_counter = 0
        
    
    def isticksOver(self):
        if self.tick_counter >= self.total_ticks:
            self.tick_counter = 0
            return self.timeOver

    def Reset(self):
        self.tick_counter = 0


    def getAllBullets(self):
        if len(self.enemybullets) > 0:
           return self.enemybullets
        else:
            return None
    
class Score():
    def __init__(self,surface,fr_width,fr_height):
        self.score = 0
        self.surface = surface
        self.fr_width = fr_width
        self.fr_height = fr_height
        self.color = (255,255,255)
        # self.display = True

    def add(self,inc):
        self.score += inc
        
    def ChangeColor(self,c_color):
        self.color = c_color

    def getScore(self):
        return self.score

    def update(self):
        font = pygame.font.SysFont('Comic Sans ms', 50)
        img = font.render(f'Score {self.score} ', True, self.color)
        self.surface.blit(img, (self.fr_width/7-img.get_rect().centerx, 20))
        # pygame.display.update()  
        



    

    
    
    
