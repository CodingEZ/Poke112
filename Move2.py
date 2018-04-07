import pygame
from pygame.locals import *
import time
import random

width = 800
height = 600

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
    def __init__(self, screen):
        self.power = 42
        self.type = "water"
        
    def animate(self, screen):
        def init(data):
            data.hands = pygame.image.load('prayemoji.png').convert()
            data.imgW = 100
            data.imgH = 100
            data.rect = data.hands.get_rect()
            data.counter = 0
            data.regrade = "Player made a regrade request!¡"
        
        def draw(data, screen):
            #snd1 = pygame.mixer.Sound('firered_003F.wav')
            #snd1.play(2)
            text = pygame.font.Font(None,25)
            data.xt = width/4
            data.yt = height - 50
            while data.counter < 3:
                data.x = random.randint(0, width/2-data.imgW)
                data.y = random.randint(0, height/2-data.imgH)
                data.rect.center = (data.x, data.y)
                screen.blit(data.hands, (data.x, data.y))
                screen.blit(text.render(data.regrade,True,(0,0,0)),(data.xt,data.yt))
                pygame.display.flip()
                time.sleep(.25)
                data.counter +=1
            data.counter = 0
    
        class Struct(object): pass
        data = Struct()
        init(data)
        draw(data, screen)
        
class ThreeAMPiazza(Move):
    def __init__(self, screen):
        self.power = 60
        self.type = 'water'
    
    def animate(self, screen):
        def init(data):
            data.piazza = "Player posted a question on Piazza at 3AM!"
            data.x = width/4
            data.y = height - 50
            data.counter = 0
        
        def draw(data, screen):
            #snd1 = pygame.mixer.Sound('firered_0014.wav')
            #snd1.play(2)
            text = pygame.font.Font(None,25)
            while data.counter < 3:
                screen.blit(text.render(data.piazza,True,(0,0,0)),(data.x,data.y))
                pygame.display.flip()
                time.sleep(.25)
                data.counter += 1
            data.counter = 0
        
        class Struct(object): pass
        data = Struct()
        init(data)
        draw(data, screen)
        
class Sleep(Move):
    def __init__(self, attacker, screen):
        self.power = 0
        attacker.health += 30
        self.type = "grass"
        
    def animate(self, screen):
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
            
        def draw(data, screen):
            #snd1 = pygame.mixer.Sound('sparkle.wav')
            #snd1.play()
            text = pygame.font.Font(None,25)
            data.xt = width/4
            data.yt = height - 50
            while data.counter <= 1:
                pygame.draw.rect(screen, (0,0,255), (0,0,800,600))
                screen.blit(data.zs, (data.x, data.y))
                screen.blit(text.render(data.sleep,True,(0,0,0)),(data.xt,data.yt))
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
        draw(data, screen)
        
class OHQueue(Move):
    def __init__(self, attacker, screen):
        self.power = 0
        attacker.attack +=3
        self.type='grass'
    
    def animate(self, screen):
        def init(data):
            data.OH = "Student is back on queue!?"
            data.x = width/4
            data.y = height - 50
            data.counter = 0
        
        def draw(data, screen):
            #snd1 = pygame.mixer.Sound('firered_0010.wav')
            #snd1.play(2)
            text = pygame.font.Font(None,25)
            while data.counter < 3:
                screen.blit(text.render(data.OH,True,(0,0,0)),(data.x,data.y))
                pygame.display.flip()
                time.sleep(.25)
                data.counter += 1
            data.counter = 0
        
        class Struct(object): pass
        data = Struct()
        init(data)
        draw(data, screen)
        
### TA MOVES ###
        
class Style(Move):
    def __init__(self, defender, screen):
        defender.health -= 2
    
    def animate(self, screen):
        def init(data):
            data.style = "Line length violation oops"
            data.x = width/4
            data.y = height - 50
            data.counter = 0
        
        def draw(data, screen):
            text = pygame.font.Font(None,25)
            while data.counter < 3:
                screen.blit(text.render(data.style,True,(0,0,0)),(data.x,data.y))
                pygame.display.flip()
                time.sleep(.25)
                data.counter += 1
            data.counter = 0
        
        class Struct(object): pass
        data = Struct()
        init(data)
        draw(data, screen)

class FixProjector(Move):
    def __init__(self, screen):
        self.power = 30
        self.type = 'grass'
    
    def animate(self, screen):
        def init(data):
            data.projector = "TA failed to work projector"
            data.x = width/4
            data.y = height - 50
            data.counter = 0
        
        def draw(data, screen):
            text = pygame.font.Font(None,25)
            while data.counter < 3:
                screen.blit(text.render(data.projector,True,(0,0,0)),(data.x,data.y))
                pygame.display.flip()
                time.sleep(.25)
                data.counter += 1
            data.counter = 0
        
        class Struct(object): pass
        data = Struct()
        init(data)
        draw(data, screen)
        
class VagueAnswers(Move):
    def __init__(self, attacker, screen):
        attacker.defense += 3
    
    def animate(self, screen):
        def init(data):
            data.vague = "What do you think?¡?"
            data.x = width/4
            data.y = height - 50
            data.counter = 0
        
        def draw(data, screen):
            text = pygame.font.Font(None,25)
            while data.counter < 3:
                screen.blit(text.render(data.vague,True,(0,0,0)),(data.x,data.y))
                pygame.display.flip()
                time.sleep(.25)
                data.counter += 1
            data.counter = 0
        
        class Struct(object): pass
        data = Struct()
        init(data)
        draw(data, screen)
        
class Clap(Move):
    def __init__(self, screen):
        self.power = 42
        self.type = 'fire'
    
    def animate(self, screen):
        def init(data):
            data.clap = "TA's prevented sleep"
            data.x = width/4
            data.y = height - 50
            data.counter = 0
        
        def draw(data, screen):
            text = pygame.font.Font(None,25)
            while data.counter < 3:
                screen.blit(text.render(data.clap,True,(0,0,0)),(data.x,data.y))
                pygame.display.flip()
                time.sleep(.25)
                data.counter += 1
            data.counter = 0
        
        class Struct(object): pass
        data = Struct()
        init(data)
        draw(data, screen)
        
### PROFESSOR MOVES ###

class DebugInClass(Move):
    def __init__(self, screen):
        self.power = 30
        self.type = 'grass'
    
    def animate(self, screen):
        def init(data):
            data.debug = "Professor tried to debug... and made more bugs!"
            data.x = width/4
            data.y = height - 50
            data.counter = 0
        
        def draw(data, screen):
            text = pygame.font.Font(None,25)
            while data.counter < 3:
                screen.blit(text.render(data.debug,True,(0,0,0)),(data.x,data.y))
                pygame.display.flip()
                time.sleep(.25)
                data.counter += 1
            data.counter = 0
        
        class Struct(object): pass
        data = Struct()
        init(data)
        draw(data, screen)
        
class LongLecture(Move):
    def __init__(self, attacker, screen):
        attacker.attack += 3
    
    def animate(self, screen):
        def init(data):
            data.lecture = "You still have two more minutes!"
            data.x = width/4
            data.y = height - 50
            data.counter = 0
        
        def draw(data, screen):
            text = pygame.font.Font(None,25)
            while data.counter < 3:
                screen.blit(text.render(data.lecture,True,(0,0,0)),(data.x,data.y))
                pygame.display.flip()
                time.sleep(.25)
                data.counter += 1
            data.counter = 0
        
        class Struct(object): pass
        data = Struct()
        init(data)
        draw(data, screen)

class Recursion(Move):
    def __init__(self):
        self.power = 60
        self.type = 'fire'
    
    def recurseanimate(self, screen):
        def init(data):
            data.recursion = "45 points recursion question on homework!"
            data.x = width/4
            data.y = height - 50
            data.counter = 0
        
        def draw(data, screen):
            text = pygame.font.Font(None,25)
            while data.counter < 3:
                screen.blit(text.render(data.recursion,True,(0,0,0)),(data.x,data.y))
                pygame.display.flip()
                time.sleep(.25)
                data.counter += 1
            data.counter = 0
        
        class Struct(object): pass
        data = Struct()
        init(data)
        draw(data, screen)
    
class BypassPiazza(Move):
    def __init__(self):
        self.power = 30
        self.type = 'grass'
        
    def animate(self, screen):
        def init(data):
            data.imgW = 200
            data.imgH = 43
            data.notification = pygame.image.load('piazzasmall.png')
            data.rect = data.notification.get_rect()
            data.counter = 0
            data.bypass = "Professor chose to bypass user preferences!"
            
        def draw(data, screen):
            snd1 = pygame.mixer.Sound('firered_001D.wav')
            snd1.play(4)
            text = pygame.font.Font(None,25)
            data.xt = width/4
            data.yt = height - 50
            while data.counter < 5:
                data.x = random.randint((width*3/4)-100, width-data.imgW)
                data.y = random.randint(height/4, height*3/4)
                data.rect.center = (data.x, data.y)
                screen.blit(data.notification, (data.x, data.y))
                screen.blit(text.render(data.bypass,True,(0,0,0)),(data.xt,data.yt))
                pygame.display.flip()
                time.sleep(.2)
                data.counter +=1
            data.counter = 0
            
        class Struct(object): pass
        data = Struct()
        init(data)
        draw(data, screen)
