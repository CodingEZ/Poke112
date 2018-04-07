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
RED = (255,0,0)
YELLOW = (255,215,0)
WIDTH = HEIGHT = 100

img = pygame.image.load('pikachu copy copy.jpg').convert()
bg = pygame.image.load('gates copy.jpg')
student = pygame.image.load('student face.jpg')

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
        self.x2 = 50
        self.y2 = 265
        self.width = 75
        self.height = 2
        self.eugene = "gO KnICks"
        self.roman = "these bad bois"

    def timerFired2(self,dt):
        self.time += 1
        if self.time%2 == 0:
            self.y+=dt
        else:
            self.y -= dt
    
    def sleep(self,surface):
        surface = win
        key = pygame.key.get_pressed()
        width = 75
        if key[pygame.K_UP] and self.width <= width:
            self.width += 5
            pygame.draw.rect(surface,GREEN,(self.x2,self.y2,self.width,self.height),5)
        if key[pygame.K_DOWN] and self.width >= 0:
            self.width -= 5
            pygame.draw.rect(surface,GREEN,(self.x2,self.y2,self.width,self.height),2)
    
    def byeStudent(self,surface):
        if self.width <= 0:
            student2 = pygame.draw.circle(surface,WHITE,(self.x+27,self.y+30),25)
    
    def draw(self,surface):
        surface = win
        width = 75
        height = 2
        pygame.draw.rect(surface,RED,(self.x2,self.y2,width,height))
        pygame.draw.rect(surface,GREEN,(self.x2,self.y2,self.width,self.height),5)
        surface.blit(self.image, (self.x,self.y))
    
    def goKnicks(self,surface):
        surface = win
        text = pygame.font.Font(None,40)
        # change according to window size
        posX = random.randint(0,400)
        posX2 = random.randint(0,400)
        posY = random.randint(0,300)
        posY2 = random.randint(0,300)
        if self.time%20 == 0:
            win.blit(text.render(self.eugene,True, (255,215,0)),(posX,posY))
            win.blit(text.render(self.roman,True,(255,0,0)),(posX2,posY2))
        

all_sprites = pygame.sprite.Group()
student = Student()
all_sprites.add(student)

run = True
while run:
    win.blit(bg,(0,0))
    pygame.time.delay(300)
    student.timerFired2(2)
    student.sleep(win)
    student.goKnicks(win)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    student.draw(win)
    student.byeStudent(win)
    pygame.display.flip()
    

pygame.quit()