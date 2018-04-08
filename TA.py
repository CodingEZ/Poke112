import pygame
import random

class TA(pygame.sprite.Sprite):
    def __init__(self, data):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/student face.jpg')
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.center = (50, 50)
        self.x = data.windowSize[0] * (47/64)
        self.y = data.windowSize[1] * (5/8)
        self.health = 150
        self.attack = 15
        self.defense = 15
        types = ['grass', 'fire', 'water']
        self.type = types[random.choice([0, 1, 2])]
        self.time = 200
        self.x2 = data.windowSize[0] * (95/128)
        self.y2 = data.windowSize[1] * (13/16)
        self.width = 75
        self.height = 2
        self.moveSet = ["Style", "FixProjector", "VagueAnswers", "Clap"]

    def timerFired(self, dt):
        self.time += 1
        if self.time % 2 == 0:
            self.y += dt
        else:
            self.y -= dt
    
    def drawHealth(self, surface):
        pygame.draw.rect(surface,(0,255,0),(self.x2,self.y2,self.width,self.height),5)
        pygame.draw.rect(surface,(0,255,0),(self.x2,self.y2,self.width,self.height),2)
    
    def byeTA(self,surface):
        if self.width <= 0:
            student2 = pygame.draw.circle(surface,(255,255,255),(self.x+27,self.y+30),25)
    
    def move(self):
        self.x += 5
    
    def moveBack(self):
        self.x -= 5
    
    def draw(self, surface):
        width = 75
        height = 2
        pygame.draw.rect(surface,(255,0,0),(self.x2,self.y2,width,height))
        pygame.draw.rect(surface,(0,255,0),(self.x2,self.y2,self.width,self.height),5)
        surface.blit(self.image, (self.x,self.y))

def drawTA(data):
    pygame.time.delay(200)
    data.ta.timerFired(2)
    data.ta.drawHealth(data.backgroundImg)
    data.ta.draw(data.backgroundImg)
    data.ta.byeTA(data.backgroundImg)
