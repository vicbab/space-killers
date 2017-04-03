import pygame
from pygame.locals import *
from sys import exit
import random
import math
from threading import Timer

        
WIDTH = 750
HEIGHT = 580
INWIDTH = 35
INHEIGHT = 25
MAX = 8
FLASH = 2


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
        shot = Shot(self.rect.centerx,self.rect.centery,1,Invader.getSpeed()*4,'yellow')
        shotList.add(shot)

class Invader2(Invader):

    def __init__(self,x,y,direction,mode):

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((INWIDTH,INHEIGHT))
        self.image.fill(pygame.Color('yellow'))
        self.image = pygame.image.load('{}/invader2.png'.format(mode))
        self.image = self.image.convert()
        self.image.set_colorkey(self.image.get_at((30,20)))
        self.imageHit1 = pygame.Surface((INWIDTH,INHEIGHT))
        self.imageHit1.fill(pygame.Color('red'))
        self.imageHit1 = pygame.image.load('{}/invader2Hit1.png'.format(mode))
        self.imageHit1 = self.imageHit1.convert()
        self.imageHit1.set_colorkey(self.imageHit1.get_at((30,20)))
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
        shot = Shot(self.rect.centerx,self.rect.centery,1,Invader.getSpeed()*5,'green')
        shotList.add(shot)

class Invader3(Invader2):

    def __init__(self,x,y,direction,mode):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((INWIDTH,INHEIGHT))
        self.image.fill(pygame.Color('red'))
        self.image = pygame.image.load('{}/invader3.png'.format(mode))
        self.image = self.image.convert()
        self.image.set_colorkey(self.image.get_at((23,18)))
        self.imageHit1 = pygame.image.load('{}/invader3Hit1.png'.format(mode))
        self.imageHit1 = self.imageHit1.convert()
        self.imageHit1.set_colorkey(self.imageHit1.get_at((25,23)))
        self.imageHit2 = pygame.image.load('{}/invader3Hit2.png'.format(mode))
        self.imageHit2 = self.imageHit2.convert()
        self.imageHit2.set_colorkey(self.imageHit2.get_at((25,23)))
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
        shot = Shot(self.rect.centerx,self.rect.centery,1,Invader.getSpeed()*6,'red')
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
        self.makeImage()

    def makeImage(self):
        image1 = pygame.Surface((INWIDTH*2.5,INHEIGHT//2.2))
        image1.fill(pygame.Color('white'))
        font = pygame.font.Font(None,25)
        text = font.render(str(self.lives),True,(0,0,0))
        image1.blit(text,(self.rect.centerx,4))

    def draw(self,screen):
        screen.blit(self.image, self.rect)

    def update(self):
        if self.lives <= 0:
            self.kill()

    def processHit(self):
        lives -= 1
        self.makeImage()


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
                                self.image.get_width()-10,
                                self.image.get_height()-10)
        self.initRect = self.rect
        self.flashing = False
        self.i = True
        self.count = 0
        self.shielded = False
        self.hasShield = True

    @staticmethod
    def setSpeed(dx):
        Avatar.dx = dx

    @staticmethod
    def getSpeed():
        return Avatar.dx

    def shield(self):
        self.shielded = True
        self.hasShield = False
        self.image.set_alpha(100)
        t1 = Timer(6,self.shieldOff)
        t1.start()

    def shieldOff(self):
        self.flash()
        t2 = Timer(20,self.canShield)
        t2.start()

    def canShield(self):
        self.hasShield = True

    def flash(self):
        self.flashing = True
        t = Timer(4,self.unFlash)
        t.start()

    def unFlash(self):
        self.flashing = False
        self.image.set_alpha(255)
        if self.shield:
            self.shielded = False

    def update(self,key,screen):
        moveLeft = None
        if self.flashing:
            if self.count==FLASH:
                self.modAlpha()
                self.count = 0
            else:
                self.count += 1
        if key==K_LEFT:
            rect = self.rect.move(-Avatar.dx,0)
            moveLeft = True
        elif key==K_RIGHT:
            rect = self.rect.move(Avatar.dx,0)
            moveLeft = False
        else:
            rect = self.rect
        if rect.right <= screen.get_width() and rect.left >= 0:
            self.rect = rect
        return moveLeft

    def modAlpha(self):
        if self.image.get_alpha()<=50:
            self.image.set_alpha(255)
        else:
            self.image.set_alpha(50)

    def draw(self,screen):
        screen.blit(self.image,self.rect)

    def shoot(self,shotList):
        shot = Shot(self.rect.centerx,self.rect.centery,-1,300,'blue')
        shotList.add(shot)


class InvaderRow:

    def __init__(self,screen,y,num,inType,mode):
        start = (screen.get_width()-num*(INWIDTH+5))/2
        inv1 = pygame.image.load('{}/invader.png'.format(mode))
        inv1 = inv1.convert()
        inv1.set_colorkey(inv1.get_at((0,12)))
        self.invaderList = []
        for i in range(num):
            if inType==1:
                invader = Invader(start+i*(INWIDTH+30),y,-1,inv1)
            elif inType==2:
                invader = Invader2(start+i*(INWIDTH+30),y,-1,mode)
            elif inType==3:
                invader = Invader3(start+i*(INWIDTH+30),y,-1,mode)
            self.invaderList.append(invader)
        self.left = self.invaderList[0]
        self.right = self.invaderList[-1]
        self.invaderGroup = pygame.sprite.Group(self.invaderList)
        self.num = num
        self.type = inType

    def update(self,timepassed,shotList,rowList):
        for invader in self.invaderList:
            invader.update(timepassed,self.invaderList)
        if self.left.rect.left < 0 or self.right.rect.right > screen.get_width():
            for row in rowList:
                row.moveDown()
        try:
            self.left = self.invaderList[0]
            self.right = self.invaderList[-1]
        except IndexError:
            pass
    
    def moveDown(self):
        for invader in self.invaderList:
            invader.moveDown()
            invader.direction *= -1

    def draw(self):
        for invader in self.invaderList:
            invader.draw()


class Frame(pygame.Surface):

    def __init__(self, width,height, rows,mode):

        pygame.Surface.__init__(self,(width, height))
        self.shotGroup = pygame.sprite.Group()
        self.invShotGroup = pygame.sprite.Group()
        self.invaders = []
        self.rows = rows
        for i in range(rows):
            if i==2 or i==3:
                invaderRow = InvaderRow(self,INHEIGHT*2+30+(INHEIGHT+20)*i,9,2,mode)
            elif i==0 :
                invaderRow = InvaderRow(self,INHEIGHT*2+30+(INHEIGHT+20)*i,9,3,mode)
            else:
                invaderRow = InvaderRow(self,INHEIGHT*2+30+(INHEIGHT+20)*i,9,1,mode)
            self.invaders.append(invaderRow)
        self.invaderGroup = pygame.sprite.Group()
        for inRow in self.invaders:
            for inv in inRow.invaderList:
                self.invaderGroup.add(inv)
        avatarImage = pygame.image.load('{}/Avatar.png'.format(mode))
        avatarImage = avatarImage.convert()
        avatarImage.set_colorkey(avatarImage.get_at((0,0)))
        self.avatar = Avatar(self.get_width()/2,self.get_height()-INHEIGHT/2,5,avatarImage)
        #self.blocks = [Block(self.get_width()-INWIDTH*1.8,]
            
        self.allSprites = pygame.sprite.Group()
        self.lives = 3
        self.state = 'normal'
        self.points = 0
        self.alpha = 255
        self.change = -2
        self.mode = mode
        #self.image = pygame.image.load('{}/Background.png'.format(mode))
        #self.image.convert()


    def makeImage(self):
        font = pygame.font.Font(None,25)
        font2 = pygame.font.Font(None,35)
        self.fill(pygame.Color('black'))
        #self.blit(self.image,(0,0))
        if self.avatar.hasShield:
            lifeText = font.render('lives : '+str(self.lives)+' You can use shield',True,pygame.Color('yellow'))
        else:
            lifeText = font.render('lives : '+str(self.lives),True,pygame.Color('yellow'))
        self.blit(lifeText, (30,10))
        pointText = font.render('Points : '+str(self.points),True,pygame.Color('yellow'))
        self.blit(pointText, (520,6))
        if self.alpha<=100:
            self.change = 2
        elif self.alpha>=253:
            self.change = -2
        highText = font.render('Highscore: '+Frame.highscore,True,pygame.Color('yellow'))
        self.blit(highText, (520,22))
        if self.lose():
            loseText = font2.render('You lose human!',True,pygame.Color('yellow'))
            self.blit(loseText, (300,9))
        if self.win():
            loseText = font2.render('You win, next level!',True,pygame.Color('yellow'))
            self.blit(loseText, (280,9))
        self.invaderGroup.draw(self)
        self.shotGroup.draw(self)
        self.invShotGroup.draw(self)
        self.avatar.draw(self)
        self.paused = False

    @staticmethod
    def setHigh(high):
        Frame.highscore = high

    @staticmethod
    def getHigh():
        return Frame.high

    def add(num):
        self.points += num

    def win(self):
        if len(self.invaderGroup) <= 0:
            return True
    def lose(self):
        for i in self.invaderGroup:
            if i.rect.bottom > self.get_height():
                return True
        if self.lives <= 0:
            return True

    def clear(self):
        self.shotGroup = pygame.sprite.Group()
        self.invShotGroup = pygame.sprite.Group()
        self.invaderGroup = pygame.sprite.Group()

    def update(self,timepassed):
        self.makeImage()
        if not self.lose() and not self.win() and self.state=='normal':
            self.shotGroup.update(timepassed)
            self.invShotGroup.update(timepassed)
            for invaderRow in self.invaders:
                invaderRow.update(timepassed,self.shotGroup,self.invaders)

    def clearShots(self):
        self.shotGroup = pygame.sprite.Group()
        self.invShotGroup = pygame.sprite.Group()

    def pause(self):
        self.state = 'pause'
        self.paused = True

    def unPause(self):
        self.state = 'normal'
        self.paused = False

    def nextLevel(self):
        if self.mode=='Fast':
            self.nextLevelShort()
        elif self.mode=='Unlimited':
            self.nextLevelLong()
        else:
            self.nextLevelNormal()

    def nextLevelShort(self):
        Invader.setSpeed(Invader.getSpeed()+5)
        if Invader.getSpeed()/5 >Avatar.getSpeed()*1.08:
            Avatar.setSpeed(Avatar.getSpeed()*1.08)
        self.shotGroup = pygame.sprite.Group()
        self.invShotGroup = pygame.sprite.Group()
        self.invaders = []
        for i in range(self.rows):
            if i==2 or i==3:
                invaderRow = InvaderRow(self,INHEIGHT*2+30+(INHEIGHT+20)*i,9,2,self.mode)
            elif i==0:
                invaderRow = InvaderRow(self,INHEIGHT*2+30+(INHEIGHT+20)*i,9,3,self.mode)
            else:
                invaderRow = InvaderRow(self,INHEIGHT*2+30+(INHEIGHT+20)*i,9,1,self.mode)
            self.invaders.append(invaderRow)
        self.invaderGroup = pygame.sprite.Group()
        for inRow in self.invaders:
            for inv in inRow.invaderList:
                self.invaderGroup.add(inv)
        #self.blocks = [Block(self.get_width()-INWIDTH*1.8,]
            
        self.allSprites = pygame.sprite.Group()
        self.lives += 1
        self.makeImage()

    def nextLevelNormal(self):
        Invader.setSpeed(Invader.getSpeed()+1)
        if Invader.getSpeed()/5 >Avatar.getSpeed()*1.08:
            Avatar.setSpeed(Avatar.getSpeed()*1.08)
        self.shotGroup = pygame.sprite.Group()
        self.invShotGroup = pygame.sprite.Group()
        self.invaders = []
        for i in range(self.rows):
            if i==2 or i==3:
                invaderRow = InvaderRow(self,INHEIGHT*2+30+(INHEIGHT+20)*i,9,2,self.mode)
            elif i==0 or i==1:
                invaderRow = InvaderRow(self,INHEIGHT*2+30+(INHEIGHT+20)*i,9,3,self.mode)
            else:
                invaderRow = InvaderRow(self,INHEIGHT*2+30+(INHEIGHT+20)*i,9,1,self.mode)
            self.invaders.append(invaderRow)
        self.invaderGroup = pygame.sprite.Group()
        for inRow in self.invaders:
            for inv in inRow.invaderList:
                self.invaderGroup.add(inv)
        #self.blocks = [Block(self.get_width()-INWIDTH*1.8,]
            
        self.allSprites = pygame.sprite.Group()
        self.lives += 1
        self.makeImage()

    def nextLevelLong(self):
        if Invader.getSpeed()/5 >Avatar.getSpeed()*1.08:
            Avatar.setSpeed(Avatar.getSpeed()*1.08)
        self.shotGroup = pygame.sprite.Group()
        self.invShotGroup = pygame.sprite.Group()
        self.invaders = []
        for i in range(self.rows):
            if i==2 or i==3:
                invaderRow = InvaderRow(self,INHEIGHT*2+30+(INHEIGHT+20)*i,9,2,self.mode)
            elif i==0 or i==1:
                invaderRow = InvaderRow(self,INHEIGHT*2+30+(INHEIGHT+20)*i,9,3,self.mode)
            else:
                invaderRow = InvaderRow(self,INHEIGHT*2+30+(INHEIGHT+20)*i,9,1,self.mode)
            self.invaders.append(invaderRow)
        self.invaderGroup = pygame.sprite.Group()
        for inRow in self.invaders:
            for inv in inRow.invaderList:
                self.invaderGroup.add(inv)
        #self.blocks = [Block(self.get_width()-INWIDTH*1.8,]
            
        self.allSprites = pygame.sprite.Group()
        self.lives += 1
        self.makeImage()


class Choice(pygame.sprite.Sprite):

    def __init__(self,image,left,top,choice):
        pygame.sprite.Sprite.__init__(self)
        self.rect = Rect(left,top,image.get_width(),image.get_height())
        self.image = image
        self.choice = choice
        self.flashing = False
        self.count = 0

    def draw(self):
        screen.blit(self.image,self.rect)

    def flash(self,time=None):
        self.flashing = True
        if time != None:
            t = Timer(time,self.unFlash)

    def unFlash(self):
        self.flashing = False

    def update(self):
        if self.flashing:
            if self.count==FLASH:
                self.modAlpha()
                self.count = 0
            else:
                self.count += 1

    def modAlpha(self):
        if self.image.get_alpha()<=50:
            self.image.set_alpha(255)
        else:
            self.image.set_alpha(50)

    def getVersion(self):
        return self.choice

class Menu(pygame.Surface):
    def __init__(self,width,height,file='versions.txt'):

        pygame.Surface.__init__(self,(width, height))
        versionsFile = open(file,'r')
        versions = []
        version = versionsFile.readline().strip()
        while not version == '':
            versions.append(version)
            version = versionsFile.readline().strip()
        self.versions = versions
        self.verList = []
        image = None
        for i in range(len(self.versions)):
            image = pygame.image.load('versions/{}.png'.format(self.versions[i]))
            image.convert()
            top = (i//2+1)*(image.get_height()+5)
            if i%2==0:
               left = (width-(image.get_width()*2)-10)/2
            else:
                left = (width-image.get_width()*2-10)/2+10+image.get_width()
            choice = Choice(image,left,top,self.versions[i])
            self.verList.append(choice)

    def makeImage(self):
        for choice in self.verList:
            choice.draw()

    def update(self):
        for choice in self.verList:
            choice.update()
            
    def flash(self,i=None):
        if i != None:
            self.verList[i].flash()
        else: #if not flash all of them
            for choice in self.verList:
                choice.flash()

    def processClick(self,x,y):
        for ver in self.verList:
            if ver.rect.left<=x<=ver.rect.right and ver.rect.top<=y<=ver.rect.bottom:
                return (True,ver.getVersion())
        return (False,None)

    

pygame.init()
pygame.display.set_caption('Space Killers')
clock = pygame.time.Clock()

screen = pygame.display.set_mode((WIDTH,HEIGHT))
menu = Menu(WIDTH,HEIGHT)


Invader.setSpeed(30)
Invader.setScore(5)

line = open('/lib/txt/highscore.txt','r')
line = line.readline()
highscore = line.strip()

pygame.event.set_grab(True)

key = None
state = 'menu'

def play():
    global state
    state = 'play'

while True:
    for event in pygame.event.get(): # get all events
        if event.type==QUIT:
            # due to grab, you can't click the close box during the game
            exit()
        if state=='play':
            if event.type==KEYDOWN: # player clicked somewhere
                key = event.key
            elif event.type==KEYUP:
                key = None
            elif event.type==MOUSEBUTTONDOWN:#K_SPACE for spacebar type=keydown
                gallery.avatar.shoot(gallery.shotGroup)
            if key == K_p:
                if gallery.state =='pause':
                    gallery.unPause()
                    pygame.mixer.music.unpause()
                else:
                    gallery.pause()
                    pygame.mixer.music.pause()
            elif key==K_e:
                state = 'wait'
                pygame.mixer.music.fadeout(900)
        elif state=='menu':
            if event.type == MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos()
                ans = menu.processClick(x,y)
                if ans[0]:
                    mode = ans[1]
                    gallery = Frame(WIDTH,HEIGHT,8,mode)
                    gallery.setHigh(highscore)
                    gallery.makeImage()
                    print(len(gallery.invaderGroup))
                    pygame.mixer.music.fadeout(800)
                    pygame.time.wait(800)
                    state = 'play'
        elif state=='wait':
            if event.type==KEYDOWN: # player clicked somewhere
                key = event.key
            elif event.type==KEYUP:
                key = None
            if event.type == KEYDOWN:
                if event.key==K_e:
                    state = 'menu'
                    gallery = None
                if event.key==K_c:
                    state = 'play'
    timePassed = clock.tick(30) # make clock do 50 frames/second
    # timePassed is interval since last clock tick
    timePassed = timePassed / 1000.0 # convert to seconds

    if state=='play':
        if gallery.state == 'pause':
            key = None
        if not gallery.win() or not gallery.lose() and not gallery.paused:
            moveLeft = gallery.avatar.update(key,screen)# update everything in the game
        else:
            gallery.clear()
        if key==K_DOWN and gallery.avatar.hasShield:
            gallery.avatar.shield()
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.load('{}/PlayMusic.ogg'.format(gallery.mode))
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(10)
        for inv in gallery.invaderGroup:
            for shot in gallery.shotGroup:
                if pygame.sprite.collide_rect(inv,shot):
                    inv.processHit(gallery)
                    shot.kill()
        if not gallery.state == 'pause':
            for row in gallery.invaders:
                for inv in row.invaderList:
                    if isinstance(inv,Invader):
                        if gallery.avatar.rect.left-5<inv.rect.centerx<gallery.avatar.rect.right+5:
                            move = True
                        else:
                            if moveLeft==True:
                                move = gallery.avatar.rect.left-50<inv.rect.centerx<gallery.avatar.rect.right-25\
                                       or gallery.avatar.rect.right+10<inv.rect.centerx<gallery.avatar.rect.right+25

                            elif moveLeft==False:
                                move = gallery.avatar.rect.left+25<inv.rect.centerx<gallery.avatar.rect.right+50\
                                       or gallery.avatar.rect.left-25<inv.rect.centerx<gallery.avatar.rect.left-10    
                            else:
                                move = False
                        if move:
                            if (len(gallery.invaderGroup)-5)*2<1:
                                coin = random.randint(1,20)
                            else:
                                coin = random.randint(1,(len(gallery.invaderGroup)-5)*2)
                                if coin==1:
                                    inv.shoot(gallery.invShotGroup)
                    if isinstance(inv,Invader2):
                        if gallery.avatar.rect.left-5<inv.rect.centerx<gallery.avatar.rect.right+5:
                            move = True
                        else:
                            if moveLeft==True:
                                move = gallery.avatar.rect.left-50<inv.rect.centerx<gallery.avatar.rect.right-25\
                                       or gallery.avatar.rect.right+10<inv.rect.centerx<gallery.avatar.rect.right+25

                            elif moveLeft==False:
                                move = gallery.avatar.rect.left+25<inv.rect.centerx<gallery.avatar.rect.right+50\
                                       or gallery.avatar.rect.left-25<inv.rect.centerx<gallery.avatar.rect.left-10
                            else:
                                move = False
                        if move:
                            if (len(gallery.invaderGroup)-10)*3<1:
                                coin = random.randint(1,20)
                            else:
                                coin = random.randint(1,(len(gallery.invaderGroup)-10)*3)
                                if coin==1:
                                    inv.shoot(gallery.invShotGroup)
                    if isinstance(inv,Invader3):
                        if gallery.avatar.rect.left-5<inv.rect.centerx<gallery.avatar.rect.right+5:
                            move = True
                        else:
                            if moveLeft==True:
                                move = gallery.avatar.rect.left-50<inv.rect.centerx<gallery.avatar.rect.right-25\
                                       or gallery.avatar.rect.right+10<inv.rect.centerx<gallery.avatar.rect.right+25
                            elif moveLeft==False:
                                move = gallery.avatar.rect.left+25<inv.rect.centerx<gallery.avatar.rect.right+50\
                                       or gallery.avatar.rect.left-25<inv.rect.centerx<gallery.avatar.rect.left-10
                            else:
                                move = False
                        if move:
                            if (len(gallery.invaderGroup)-5)*3<1:
                                coin = random.randint(1,20)
                            else:
                                coin = random.randint(1,(len(gallery.invaderGroup)-5)*3)
                                if coin==1:
                                    inv.shoot(gallery.invShotGroup)
        for shot in gallery.invShotGroup:
            if pygame.sprite.collide_rect(shot,gallery.avatar) and not gallery.lose() and not gallery.avatar.shielded:
                gallery.lives -= 1
                gallery.avatar.canShield()
                shot.kill()
                gallery.clearShots()
                gallery.makeImage()
                screen.blit(gallery, (0,0)) # draw the whole game
                pygame.display.update()
                gallery.avatar.rect = gallery.avatar.initRect
                gallery.avatar.flash()
                gallery.pause()
                pygame.time.wait(2000)
                clock = pygame.time.Clock()
                gallery.unPause()

        gallery.update(timePassed)
        if gallery.win():
            gallery.makeImage()
            screen.blit(gallery, (0,0)) # draw the whole game
            pygame.display.update() 
            pygame.time.wait(2000)
            clock = pygame.time.Clock()
            gallery.nextLevelLong()
            gallery.avatar.hasShield = True
        elif gallery.lose():
            gallery.makeImage()
            screen.blit(gallery, (0,0)) # draw the whole game
            pygame.display.update()
            if gallery.points > int(highscore):
                file = open('/lib/txt/highscore.txt','w')
                file.write(str(gallery.points)+'\n')
                file.close()
            pygame.time.wait(3000)
            state = 'menu'
            gallery = None
            pygame.mixer.music.fadeout(500)
        if state == 'play':
            gallery.makeImage()
            screen.blit(gallery, (0,0)) # draw the whole game

    elif state=='menu':
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.load('lib/music/MenuMusic.ogg')
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(10)
        menu.update()
        menu.makeImage()
        screen.blit(menu, (0,0))
        for choice in menu.verList:
            choice.draw()

    elif state=='wait':
        screen.fill((0,0,0))
        font = pygame.font.SysFont('arial', 45)
        text = font.render("Press 'c' to continue game."\
                           , True, pygame.Color('yellow'))
        screen.blit(text,(90,150))
        text2 = font.render("Press 'e' to go to the menu.",True,pygame.Color('yellow'))
        screen.blit(text2,(90,200))
        text3 = font.render("Returning to the menu will erase progress",True,pygame.Color('yellow'))
        screen.blit(text3,(10,250))
        if state != 'wait':
            text = None

    pygame.display.update()














            
        


