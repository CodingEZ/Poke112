import pygame
import random
<<<<<<< HEAD
=======
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
>>>>>>> 4d4109d265aa4f62c918a2222918a948504ac1ed

class Student(pygame.sprite.Sprite):
    def __init__(self, data):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/student face.jpg')
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.center = (50, 50)
        self.x = data.windowSize[0] * (1/4)
        self.y = data.windowSize[1] * (5/8)
        self.health = 112
        self.attack = 20
        self.defense = 20
        types = ['grass', 'fire', 'water']
        self.type = types[random.choice([0, 1, 2])]
        self.time = 200
        self.x2 = data.windowSize[0] * (17/64)
        self.y2 = data.windowSize[1] * (13/16)
        self.width = 75
        self.height = 2
<<<<<<< HEAD
        self.moveSet = ["RegradeReq", "ThreeAMPiazza", "Sleep", "OHQueue"]
=======
        self.eugene = "gO KnICks"
        self.roman = "these bad bois"
>>>>>>> 4d4109d265aa4f62c918a2222918a948504ac1ed

    def timerFired(self, dt):
        self.time += 1
        if self.time % 2 == 0:
            self.y += dt
        else:
            self.y -= dt
    
    def drawHealth(self, surface):
        pygame.draw.rect(surface,(0,255,0),(self.x2,self.y2,self.width,self.height),5)
        pygame.draw.rect(surface,(0,255,0),(self.x2,self.y2,self.width,self.height),2)
    
    def byeStudent(self,surface):
        if self.width <= 0:
            student2 = pygame.draw.circle(surface,(255,255,255),(self.x+27,self.y+30),25)
    
<<<<<<< HEAD
    def move(self):
        self.x += 5
    
    def moveBack(self):
        self.x -= 5
    
    def draw(self, surface):
=======
    def draw(self,surface):
        surface = win
>>>>>>> 4d4109d265aa4f62c918a2222918a948504ac1ed
        width = 75
        height = 2
        pygame.draw.rect(surface,(255,0,0),(self.x2,self.y2,width,height))
        pygame.draw.rect(surface,(0,255,0),(self.x2,self.y2,self.width,self.height),5)
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
        

<<<<<<< HEAD
def drawStudent(data):
    pygame.time.delay(200)
    data.student.timerFired(2)
    data.student.drawHealth(data.backgroundImg)
    data.student.draw(data.backgroundImg)
    data.student.byeStudent(data.backgroundImg)
    #pygame.display.flip()
=======
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
>>>>>>> 4d4109d265aa4f62c918a2222918a948504ac1ed
