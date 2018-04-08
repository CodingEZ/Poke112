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
    def __init__(self): 
        self.power = 42 
        self.type = "water"
        self.hands = pygame.image.load('images/prayemoji.png').convert() 
        self.imgW = 100 
        self.imgH = 100 
        self.rect = self.hands.get_rect() 
        self.counter = 0 
        self.regrade = "Player made a regrade request!¡" 

    def animate(self, screen): 
        #snd1 = pygame.mixer.Sound('firered_003F.wav') 
        #snd1.play(2) 
        text = pygame.font.Font(None, 25) 
        xt = width/4 
        yt = height - 50 
        while self.counter < 3: 
            x = random.randint(0, width/2-self.imgW) 
            y = random.randint(0, height/2-self.imgH) 
            self.rect.center = (x, y) 
            screen.blit(self.hands, (x, y)) 
            screen.blit(text.render(self.regrade, True, (0,0,0)),(xt, yt)) 
            pygame.display.flip() 
            time.sleep(.25) 
            self.counter += 1 
        self.counter = 0
         
class ThreeAMPiazza(Move): 
    def __init__(self): 
        self.power = 60 
        self.type = 'water'
        self.piazza = "Player posted a question on Piazza at 3AM!" 
        self.x = width/4 
        self.y = height - 50 
        self.counter = 0 
     
    def animate(self, screen): 
        #snd1 = pygame.mixer.Sound('firered_0014.wav') 
        #snd1.play(2) 
        text = pygame.font.Font(None, 25) 
        while self.counter < 3: 
            screen.blit(text.render(self.piazza, True, (0,0,0)), (self.x, self.y)) 
            pygame.display.flip() 
            time.sleep(.25) 
            self.counter += 1 
        self.counter = 0
         
class Sleep(Move): 
    def __init__(self, attacker): 
        self.power = 0 
        attacker.health += 30 
        self.type = "grass"
        self.zs = pygame.image.load('images/zs.png') 
        self.imgW = 100 
        self.imgH = 100 
        self.rect = self.zs.get_rect() 
        self.y = height/2 
        self.x = width/4 
        self.vel = 10 
        self.animSize = 50 
        self.counter = 0 
        self.sleep = "Player has crashed!" 
         
    def animate(self, screen): 
        #snd1 = pygame.mixer.Sound('sparkle.wav') 
        #snd1.play() 
        text = pygame.font.Font(None, 25) 
        self.xt = width/4 
        self.yt = height - 50 
        while self.counter <= 1: 
            pygame.draw.rect(screen, (0,0,255), (0,0,800,600)) 
            screen.blit(self.zs, (self.x, self.y)) 
            screen.blit(text.render(self.sleep,True,(0,0,0)),(self.xt,self.yt)) 
            pygame.display.flip() 
            if self.x+self.vel < width/3: 
                self.x += self.vel 
                self.y -= self.vel 
            else: 
                self.y = height/2 
                self.x = width/4 
            time.sleep(.2) 
            self.counter += .1 
        self.counter = 0 
         
class OHQueue(Move): 
    def __init__(self, attacker): 
        self.power = 0 
        attacker.attack +=3 
        self.type='grass'
        self.OH = "Student is back on queue!?" 
        self.x = width/4 
        self.y = height - 50 
        self.counter = 0
     
    def animate(self, screen): 
        #snd1 = pygame.mixer.Sound('firered_0010.wav') 
        #snd1.play(2) 
        text = pygame.font.Font(None, 25) 
        while self.counter < 3: 
            screen.blit(text.render(self.OH, True, (0,0,0)), (self.x, self.y)) 
            pygame.display.flip() 
            time.sleep(.25) 
            self.counter += 1 
        self.counter = 0
         
### TA MOVES ### 
         
class Style(Move): 
    def __init__(self, defender): 
        defender.health -= 2
        self.style = "Line length violation oops" 
        self.x = width/4 
        self.y = height - 50 
        self.counter = 0 
     
    def animate(self, screen): 
        text = pygame.font.Font(None, 25) 
        while self.counter < 3: 
            screen.blit(text.render(self.style, True, (0,0,0)), (self.x, self.y)) 
            pygame.display.flip() 
            time.sleep(.25) 
            self.counter += 1 
        self.counter = 0 
         
class FixProjector(Move): 
    def __init__(self): 
        self.power = 30 
        self.type = 'grass'
        self.projector = "TA failed to work projector" 
        self.x = width/4 
        self.y = height - 50 
        self.counter = 0 
     
    def animate(self, screen): 
        text = pygame.font.Font(None, 25) 
        while self.counter < 3: 
            screen.blit(text.render(self.projector,True,(0,0,0)),(self.x,self.y)) 
            pygame.display.flip() 
            time.sleep(.25) 
            self.counter += 1 
        self.counter = 0
         
class VagueAnswers(Move): 
    def __init__(self, attacker): 
        attacker.defense += 3
        self.vague = "What do you think?¡?" 
        self.x = width/4 
        self.y = height - 50 
        self.counter = 0 
     
    def animate(self, screen): 
        text = pygame.font.Font(None, 25) 
        while self.counter < 3: 
            screen.blit(text.render(self.vague, True, (0,0,0)), (self.x, self.y)) 
            pygame.display.flip() 
            time.sleep(.25) 
            self.counter += 1 
        self.counter = 0
         
class Clap(Move): 
    def __init__(self): 
        self.power = 42 
        self.type = 'fire'
        self.clap = "TA's prevented sleep" 
        self.x = width/4 
        self.y = height - 50 
        self.counter = 0 
     
    def animate(self, screen): 
        text = pygame.font.Font(None, 25) 
        while self.counter < 3: 
            screen.blit(text.render(self.clap, True, (0,0,0)), (self.x, self.y)) 
            pygame.display.flip() 
            time.sleep(.25) 
            self.counter += 1 
        self.counter = 0 

         
### PROFESSOR MOVES ### 
 
class DebugInClass(Move): 
    def __init__(self): 
        self.power = 30 
        self.type = 'grass'
        self.debug = "Professor tried to debug... and made more bugs!" 
        self.x = width/4 
        self.y = height - 50 
        self.counter = 0 
    
    def animate(self, screen): 
        text = pygame.font.Font(None, 25) 
        while self.counter < 3: 
            screen.blit(text.render(self.debug, True, (0,0,0)), (self.x, self.y)) 
            pygame.display.flip() 
            time.sleep(.25) 
            self.counter += 1
        self.counter = 0
         
class LongLecture(Move): 
    def __init__(self, attacker): 
        attacker.attack += 3
        self.lecture = "You still have two more minutes!" 
        self.x = width/4 
        self.y = height - 50 
        self.counter = 0 
     
    def animate(self, screen): 
        text = pygame.font.Font(None, 25) 
        while self.counter < 3: 
            screen.blit(text.render(self.lecture, True, (0,0,0)), (self.x, self.y)) 
            pygame.display.flip() 
            time.sleep(.25) 
            self.counter += 1 
        self.counter = 0 
 
class Recursion(Move): 
    def __init__(self): 
        self.power = 60 
        self.type = 'fire'
        self.recursion = "45 points recursion question on homework!" 
        self.x = width/4 
        self.y = height - 50 
        self.counter = 0 
     
    def recurseanimate(self, screen): 
        text = pygame.font.Font(None, 25) 
        while self.counter < 3: 
            screen.blit(text.render(self.recursion, True, (0,0,0)), (self.x, self.y)) 
            pygame.display.flip() 
            time.sleep(.25) 
            self.counter += 1 
        self.counter = 0 
     
class BypassPiazza(Move): 
    def __init__(self): 
        self.power = 30 
        self.type = 'grass'
        self.imgW = 200 
        self.imgH = 43 
        self.notification = pygame.image.load('images/piazzasmall.png') 
        self.rect = self.notification.get_rect() 
        self.counter = 0 
        self.bypass = "Professor chose to bypass user preferences!" 
         
    def animate(self, screen): 
        snd1 = pygame.mixer.Sound('sounds/firered_001D.wav') 
        snd1.play(4) 
        text = pygame.font.Font(None, 25) 
        self.xt = width/4 
        self.yt = height - 50 
        while self.counter < 5: 
            self.x = random.randint((width*3/4)-100, width-self.imgW) 
            self.y = random.randint(height/4, height*3/4) 
            self.rect.center = (self.x, self.y) 
            screen.blit(self.notification, (self.x, self.y)) 
            screen.blit(text.render(self.bypass,True,(0,0,0)),(self.xt,self.yt)) 
            pygame.display.flip() 
            time.sleep(.2) 
            self.counter +=1  
        self.counter = 0
