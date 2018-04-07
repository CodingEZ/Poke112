import pygame
import random
pygame.init()

windowSize = (400,300)
win = pygame.display.set_mode(windowSize)


pygame.display.set_caption("First Game")

x = 100
y = 50
width = 40
height = 60
vel = 5

WHITE = (255,255,255)
GREEN = (0,255,0)
WIDTH = HEIGHT = 100

img = pygame.image.load('pikachu copy copy.jpg').convert()
bg = pygame.image.load('gates copy.jpg')

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.x = 0
        self.y = 0
    
    def handle_keys(self):
        key = pygame.key.get_pressed()
        dist = 5
        if key[pygame.K_DOWN]:
            self.y += dist
        elif key[pygame.K_UP]:
            self.y -= dist
        if key[pygame.K_RIGHT]:
            self.x += dist
        elif key[pygame.K_LEFT]:
            self.x -= dist
    
    def draw(self,surface):
        surface = win
        surface.blit(self.image, (self.x,self.y))

student = pygame.image.load('student face.jpg')

#230 x 230
class Student(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = student
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.x = 50
        self.y = 200
        self.health = 0
        self.attack = 0
        self.time = 200
        types = random.randint(0,2)
        if type == 0:
            self.type = 'grass'
        elif type == 1:
            self.type = 'water'
        else:
            self.type = 'fire'
        self.x2 = 50
        self.y2 = 265
        self.width = 75
        self.height = 2
    
    def handle_keys(self):
        key = pygame.key.get_pressed()
        dist = 5
        if key[pygame.K_DOWN]:
            self.y += dist
        elif key[pygame.K_UP]:
            self.y -= dist
        if key[pygame.K_RIGHT]:
            self.x += dist
        elif key[pygame.K_LEFT]:
            self.x -= dist
    
    def timerFired2(self,dt):
        self.time += 1
        if self.time%2 == 0:
            self.x+=dt
        else:
            self.x -= dt
    
    def testRegrade(self,obj):
        pass
    
    def health(self,surface):
        surface = win
        pygame.draw.rect(surface,GREEN,(self.x2,self.y2,width,height))
    
    def move(self):
        self.x += 5
    
    def moveBack(self):
        self.x -= 5
    
    def draw(self,surface):
        surface = win
        pygame.draw.rect(surface,GREEN,(self.x2,self.y2,self.width,self.height),5)
        surface.blit(self.image, (self.x,self.y))

#win.blit(bg,(0,0))

all_sprites = pygame.sprite.Group()
player = Player()
student = Student()
all_sprites.add(player)
all_sprites.add(student)

run = True
while run:
    win.blit(bg,(0,0))
    pygame.time.delay(100)
    #all_sprites.update()
    #all_sprites.handle_keys()
    #all_sprites.draw(win)
    student.timerFired2(2)
    #student.health(win)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    student.handle_keys()
    student.draw(win)
    pygame.display.flip()
    #pygame.display.update()
    

pygame.quit()