import pygame
from pygame.locals import *
from sys import exit
import random

INWIDTH = 35
INHEIGHT = 25
MAX = 8

class Invader(pygame.sprite.Sprite):
    '''Basic easy invader'''
    def __init__(self,x,y,direction,image):

        pygame.sprite.Sprite.__init__(self)
        image1 = pygame.Surface((INWIDTH,INHEIGHT))
        image1.fill(pygame.Color('green'))
        self.image = image
        self.imageHit = pygame.Surface((INWIDTH,INHEIGHT))
        self.imageHit.fill(pygame.Color('orange'))
        left = x - self.image.get_width()/2
        top = y - self.image.get_height()/2
        self.rect = pygame.Rect(left,top,
                                self.image.get_width(),
                                self.image.get_height())
        self.killed = False
        self.direction = direction
        self.hit = MAX

    def draw(self,screen):
        screen.blit(self.image, self.rect)

    @staticmethod
    def setSpeed(dx):
        Invader.dx = dx

    @staticmethod
    def getSpeed():
        return Invader.dx

    @staticmethod
    def setScore(num):
        Invader.score = num

    @staticmethod
    def getScore():
        return Invader.score

    def update(self,timepassed,ls):
        self.rect = self.rect.move(self.direction*Invader.dx*timepassed,0)
        if self.hit==0:
            self.kill()
            ls.remove(self)
        else:
            if self.hit<MAX:
                self.hit -= 1

    def moveDown(self):
        if self.direction > 0:
            self.rect = self.rect.move(-5,INHEIGHT)
        else:
            self.rect = self.rect.move(5,INHEIGHT)

    def processHit(self,gallery):
        if self.hit==MAX:
            self.image = self.imageHit
            self.hit -= 1
            gallery.points += self.getScore()

    def shoot(self,shotList):
        shot = Shot(self.rect.centerx,self.rect.centery,1,120,'yellow')
        shotList.add(shot)

class Invader2(Invader):

    def __init__(self,x,y,direction):

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((INWIDTH,INHEIGHT))
        self.image.fill(pygame.Color('yellow'))
        self.imageHit1 = pygame.Surface((INWIDTH,INHEIGHT))
        self.imageHit1.fill(pygame.Color('red'))
        self.imageHit2 = pygame.Surface((INWIDTH,INHEIGHT))
        self.imageHit2.fill(pygame.Color('orange'))
        left = x - self.image.get_width()/2
        top = y - self.image.get_height()/2
        self.rect = pygame.Rect(left,top,
                                self.image.get_width(),
                                self.image.get_height())
        self.killed = False
        self.direction = direction
        self.hit = MAX
        self.lives = 1

    def processHit(self,gallery):
        if self.lives > 0:
            self.image = self.imageHit1
            self.lives -= 1
        else:
            if self.hit==MAX:
                self.image = self.imageHit2
                self.hit -= 1
                gallery.points += self.getScore()

    def getScore(self):
        return Invader.getScore() + 5

    def shoot(self,shotList):
        shot = Shot(self.rect.centerx,self.rect.centery,1,150,'green')
        shotList.add(shot)

class Invader3(Invader2):

    def __init__(self,x,y,direction):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((INWIDTH,INHEIGHT))
        self.image.fill(pygame.Color('red'))
        self.imageHit1 = pygame.Surface((INWIDTH,INHEIGHT))
        self.imageHit1.fill(pygame.Color('yellow'))
        self.imageHit2 = pygame.Surface((INWIDTH,INHEIGHT))
        self.imageHit2.fill(pygame.Color('green'))
        self.imageHit3 = pygame.Surface((INWIDTH,INHEIGHT))
        self.imageHit3.fill(pygame.Color('orange'))
        left = x - self.image.get_width()/2
        top = y - self.image.get_height()/2
        self.rect = pygame.Rect(left,top,
                                self.image.get_width(),
                                self.image.get_height())
        self.killed = False
        self.direction = direction
        self.hit = MAX
        self.lives = 2

    def processHit(self,gallery):
        if self.lives >= 2:
            self.image = self.imageHit1
            self.lives -= 1
        elif self.lives ==1:
            self.image = self.imageHit2
            self.lives -= 1
        else:
            if self.hit==MAX:
                self.image = self.imageHit3
                self.hit -= 1
                gallery.points += self.getScore()

    def getScore(self):
        return Invader.getScore() + 10

    def shoot(self,shotList):
        shot = Shot(self.rect.centerx,self.rect.centery,1,170,'red')
        shotList.add(shot)


class Shot(pygame.sprite.Sprite):
    '''the bullets getting shot by the avatar and invaders'''
    def __init__(self,x,y,direction,speed,color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((5,15))
        self.image.fill(pygame.Color(color))
        left = x - self.image.get_width()/2
        top = y - self.image.get_height()/2
        self.rect = pygame.Rect(left, top,
                                self.image.get_width(),
                                self.image.get_height())
        self.speed = speed
        self.direction = direction
        self.color = color


    def draw(self,screen):
        screen.blit(self.image, self.rect)

    def update(self,timePassed):
        self.rect = self.rect.move(0,self.direction*self.speed*timePassed)
        if self.rect.bottom < 0 or self.rect.bottom > screen.get_height():
            self.kill()

class Block(pygame.sprite.Sprite):

    def __init__(self,x,y,lives):
        pygame.sprite.Spite.__init__(self)
        image1 = pygame.Surface((INWIDTH*2.5,INHEIGHT//2.2))
        image1.fill(pygame.Color('white'))
        left = x - self.image.get_width()/2
        top = y - self.image.get_height()/2
        self.rect = pygame.Rect(left, top,
                                self.image.get_width(),
                                self.image.get_height())
        self.lives = lives

    def draw(self,screen):
        screen.blit(self.image, self.rect)

    def update(self):
        if self.lives <= 0:
            self.kill()



class Avatar(pygame.sprite.Sprite):

    def __init__(self,x,y,dx,image):
        pygame.sprite.Sprite.__init__(self)
        image1 = pygame.Surface((INWIDTH+10,INHEIGHT+5))
        image1.fill(pygame.Color('blue'))
        self.image = image
        #self.imageHit = imageHit
        Avatar.setSpeed(dx)
        left = x - self.image.get_width()/2
        top = y - self.image.get_height()/2
        self.rect = pygame.Rect(left, top,
                                self.image.get_width(),
                                self.image.get_height())
        self.initRect = self.rect

    @staticmethod
    def setSpeed(dx):
        Avatar.dx = dx

    @staticmethod
    def getSpeed():
        return Avatar.dx

    def update(self,key,screen):
        if key==K_LEFT:
            rect = self.rect.move(-Avatar.dx,0)
        elif key==K_RIGHT:
            rect = self.rect.move(Avatar.dx,0)
        else:
            rect = self.rect
        if rect.right <= screen.get_width() and rect.left >= 0:
            self.rect = rect

    def draw(self,screen):
        screen.blit(self.image,self.rect)

    def shoot(self,shotList):
        shot = Shot(self.rect.centerx,self.rect.centery,-1,250,'blue')
        shotList.add(shot)
