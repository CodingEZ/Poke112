

import pygame
from pygame.locals import *
import time
import random


# probably will take out all the framework stuff 
pygame.init()

width = 800
height = 600

gameDisplay = pygame.display.set_mode((800, 600)) # must put in a tuple, kinda like setting up a canvas its the 'surface'
pygame.display.set_caption('move test')
pygame.draw.rect(gameDisplay, (0,0,255), (0,0,800,600))
pygame.mixer.music.load('champion.mp3')
pygame.mixer.music.play(-1)



### SUPERCLASS ###

class Move(pygame.sprite.Sprite):
    def damage(self, attacker, defender):
        attackerType = attacker.type
        defenderType = defender.type
        attack = attacker.attack
        defense = defender.defense
        movePower = self.power
        moveType = self.type
        STAB = 1
        typeAdv = typeAdvCalc(attackerType, defenderType)
        if attackerType == moveType:
            STAB = 1.5
        damage = .44 * movePower * (attack/defense) * typeAdv * STAB
        return damage
            
    def typeAdvCalc(self, defenderType):
        moveType = self.type
        if moveType == "water" and defenderType == "water":
            typeAdv = .5
        if moveType == "water" and defenderType == "grass":
            typeAdv = .5
        if moveType == "water" and defenderType == "fire":
            typeAdv = 2
        if moveType == "grass" and defenderType == "water":
            typeAdv = 2
        if moveType == "grass" and defenderType == "grass":
            typeAdv = .5
        if moveType == "grass" and defenderType == "fire":
            typeAdv = .5
        if moveType == "fire" and defenderType == "water":
            typeAdv = .5
        if moveType == "fire" and defenderType == "grass":
            typeAdv = 2
        if moveType == "fire" and defenderType == "fire":
            typeAdv = .5
            
### STUDENT MOVES ###
            
class RegradeReq(Move):
    def __init__(self):
        self.power = 42
        self.type = "water"
        self.animation = regradeAnimate()
        
    @staticmethod
    def regradeAnimate():
        def init(data):
            data.hands = pygame.image.load('prayemoji.png').convert()
            data.imgW = 100
            data.imgH = 100
            data.rect = data.hands.get_rect()
            data.counter = 0
            data.regrade = "Player made a regrade request!¡"
        
        def draw(data):
            snd1 = pygame.mixer.Sound('firered_003F.wav')
            snd1.play(2)
            text = pygame.font.Font(None,25)
            data.xt = width/4
            data.yt = height - 50
            while data.counter < 3:
                data.x = random.randint(0, width/2-data.imgW)
                data.y = random.randint(0, height/2-data.imgH)
                data.rect.center = (data.x, data.y)
                gameDisplay.blit(data.hands, (data.x, data.y))
                gameDisplay.blit(text.render(data.regrade,True,(0,0,0)),(data.xt,data.yt))
                pygame.display.flip()
                time.sleep(.25)
                data.counter +=1
            data.counter = 0
    
        class Struct(object): pass
        data = Struct()
        init(data)
        draw(data)
        
class ThreeAMPiazza(Move):
    def __init__(self):
        self.power = 60
        self.type = 'water'
        self.animation = threeAMPiazzaAnimate()
    
    @staticmethod
    def threeAMPiazzaAnimate():
        def init(data):
            data.piazza = "Player posted a question on Piazza at 3AM!"
            data.x = width/4
            data.y = height - 50
            data.counter = 0
        
        def draw(data):
            snd1 = pygame.mixer.Sound('firered_0014.wav')
            snd1.play(2)
            text = pygame.font.Font(None,25)
            while data.counter < 3:
                gameDisplay.blit(text.render(data.piazza,True,(0,0,0)),(data.x,data.y))
                pygame.display.flip()
                time.sleep(.25)
                data.counter += 1
            data.counter = 0
        
        class Struct(object): pass
        data = Struct()
        init(data)
        draw(data)
        
class Sleep(Move):
    def __init__(self):
        self.power = 0
        attacker.health += 30
        self.type = "grass"
        self.animation = sleepAnimate()
        
    @staticmethod
    def sleepAnimate():
        def init(data):
            data.zs = pygame.image.load('zs.png')
            data.imgW = 100
            data.imgH = 100
            data.rect = data.zs.get_rect()
            data.y = height/2
            data.x = width/4
            data.vel = 10
            data.animSize = 50
            data.counter = 0
            data.sleep = "Player has crashed!"
            
        def draw(data):
            snd1 = pygame.mixer.Sound('sparkle.wav')
            snd1.play()
            text = pygame.font.Font(None,25)
            data.xt = width/4
            data.yt = height - 50
            while data.counter <= 1:
                pygame.draw.rect(gameDisplay, (0,0,255), (0,0,800,600))
                gameDisplay.blit(data.zs, (data.x, data.y))
                gameDisplay.blit(text.render(data.sleep,True,(0,0,0)),(data.xt,data.yt))
                pygame.display.flip()
                if data.x+data.vel < width/3:
                    data.x += data.vel
                    data.y -= data.vel
                else:
                    data.y = height/2
                    data.x = width/4
                time.sleep(.2)
                data.counter += .1
            data.counter = 0
        
        class Struct(object): pass
        data = Struct()
        init(data)
        draw(data)
        
class OHQueue(Move):
    def __init__(self):
        self.power = 0
        attacker.attack +=3
        self.type='grass'
        self.animation = ohAnimate()
    
    @staticmethod
    def ohAnimate():
        def init(data):
            data.OH = "Student is back on queue!?"
            data.x = width/4
            data.y = height - 50
            data.counter = 0
        
        def draw(data):
            snd1 = pygame.mixer.Sound('firered_0010.wav')
            snd1.play(2)
            text = pygame.font.Font(None,25)
            while data.counter < 3:
                gameDisplay.blit(text.render(data.OH,True,(0,0,0)),(data.x,data.y))
                pygame.display.flip()
                time.sleep(.25)
                data.counter += 1
            data.counter = 0
        
        class Struct(object): pass
        data = Struct()
        init(data)
        draw(data)
        
### TA MOVES ###
        
class Style(Move):
    def __init__(self):
        defender.health -= 2
        self.animation = styleAnimate()
    
    @staticmethod
    def styleAnimate():
        def init(data):
            data.style = "Line length violation oops"
            data.x = width/4
            data.y = height - 50
            data.counter = 0
        
        def draw(data):
            text = pygame.font.Font(None,25)
            while data.counter < 3:
                gameDisplay.blit(text.render(data.style,True,(0,0,0)),(data.x,data.y))
                pygame.display.flip()
                time.sleep(.25)
                data.counter += 1
            data.counter = 0
        
        class Struct(object): pass
        data = Struct()
        init(data)
        draw(data)

class FixProjector(Move):
    def __init__(self):
        self.power = 30
        self.type = 'grass'
        self.animation = fixAnimate()
    
    @staticmethod
    def fixAnimate():
        def init(data):
            data.projector = "TA failed to work projector"
            data.x = width/4
            data.y = height - 50
            data.counter = 0
        
        def draw(data):
            text = pygame.font.Font(None,25)
            while data.counter < 3:
                gameDisplay.blit(text.render(data.projector,True,(0,0,0)),(data.x,data.y))
                pygame.display.flip()
                time.sleep(.25)
                data.counter += 1
            data.counter = 0
        
        class Struct(object): pass
        data = Struct()
        init(data)
        draw(data)
        
class VagueAnswers(Move):
    def __init__(self):
        attacker.defense += 3
        self.animation = vagueAnimate()
    
    @staticmethod
    def vagueAnimate():
        def init(data):
            data.vague = "What do you think?¡?"
            data.x = width/4
            data.y = height - 50
            data.counter = 0
        
        def draw(data):
            text = pygame.font.Font(None,25)
            while data.counter < 3:
                gameDisplay.blit(text.render(data.vague,True,(0,0,0)),(data.x,data.y))
                pygame.display.flip()
                time.sleep(.25)
                data.counter += 1
            data.counter = 0
        
        class Struct(object): pass
        data = Struct()
        init(data)
        draw(data)
        
class Clap(Move):
    def __init__(self):
        self.power = 42
        self.type = 'fire'
        self.animation = clapAnimate()
    
    @staticmethod
    def clapAnimate():
        def init(data):
            data.clap = "TA's prevented sleep"
            data.x = width/4
            data.y = height - 50
            data.counter = 0
        
        def draw(data):
            text = pygame.font.Font(None,25)
            while data.counter < 3:
                gameDisplay.blit(text.render(data.clap,True,(0,0,0)),(data.x,data.y))
                pygame.display.flip()
                time.sleep(.25)
                data.counter += 1
            data.counter = 0
        
        class Struct(object): pass
        data = Struct()
        init(data)
        draw(data)
        
### PROFESSOR MOVES ###

class DebugInClass(Move):
    def __init__(self):
        self.power = 30
        self.type = 'grass'
        self.animation = debugAnimate()
    
    @staticmethod
    def debugAnimate():
        def init(data):
            data.debug = "Professor tried to debug... and made more bugs!"
            data.x = width/4
            data.y = height - 50
            data.counter = 0
        
        def draw(data):
            text = pygame.font.Font(None,25)
            while data.counter < 3:
                gameDisplay.blit(text.render(data.debug,True,(0,0,0)),(data.x,data.y))
                pygame.display.flip()
                time.sleep(.25)
                data.counter += 1
            data.counter = 0
        
        class Struct(object): pass
        data = Struct()
        init(data)
        draw(data)
        
class LongLecture(Move):
    def __init__(self):
        attacker.attack += 3
        self.animation = lectureAnimate()
    
    @staticmethod
    def lectureAnimate():
        def init(data):
            data.lecture = "You still have two more minutes!"
            data.x = width/4
            data.y = height - 50
            data.counter = 0
        
        def draw(data):
            text = pygame.font.Font(None,25)
            while data.counter < 3:
                gameDisplay.blit(text.render(data.lecture,True,(0,0,0)),(data.x,data.y))
                pygame.display.flip()
                time.sleep(.25)
                data.counter += 1
            data.counter = 0
        
        class Struct(object): pass
        data = Struct()
        init(data)
        draw(data)

class Recursion(Move):
    def __init__(self):
        self.power = 60
        self.type = 'fire'
        self.animation = recurseAnimate()
    
    @staticmethod
    def recurseAnimate():
        def init(data):
            data.recursion = "45 points recursion question on homework!"
            data.x = width/4
            data.y = height - 50
            data.counter = 0
        
        def draw(data):
            text = pygame.font.Font(None,25)
            while data.counter < 3:
                gameDisplay.blit(text.render(data.recursion,True,(0,0,0)),(data.x,data.y))
                pygame.display.flip()
                time.sleep(.25)
                data.counter += 1
            data.counter = 0
        
        class Struct(object): pass
        data = Struct()
        init(data)
        draw(data)
    
class BypassPiazza(Move):
    def __init__(self):
        self.power = 30
        self.type = 'grass'
        self.animation = bypassAnimate()
        
    @staticmethod
    def bypassAnimate():
        def init(data):
            data.imgW = 200
            data.imgH = 43
            data.notification = pygame.image.load('piazzasmall.png')
            data.rect = data.notification.get_rect()
            data.counter = 0
            data.bypass = "Professor chose to bypass user preferences!"
            
        def draw(data):
            snd1 = pygame.mixer.Sound('firered_001D.wav')
            snd1.play(4)
            text = pygame.font.Font(None,25)
            data.xt = width/4
            data.yt = height - 50
            while data.counter < 5:
                data.x = random.randint((width*3/4)-100, width-data.imgW)
                data.y = random.randint(height/4, height*3/4)
                data.rect.center = (data.x, data.y)
                gameDisplay.blit(data.notification, (data.x, data.y))
                gameDisplay.blit(text.render(data.bypass,True,(0,0,0)),(data.xt,data.yt))
                pygame.display.flip()
                time.sleep(.2)
                data.counter +=1
            data.counter = 0
            
        class Struct(object): pass
        data = Struct()
        init(data)
        draw(data)


pygame.display.update()

gameExit = False

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == KEYDOWN and event.key == pygame.K_SPACE:
            BypassPiazza.bypassAnimate()

pygame.quit()
quit()
