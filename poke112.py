import pygame
pygame.init()

win = pygame.display.set_mode((400,300))

pygame.display.set_caption("First Game")

x = 100
y = 50
width = 40
height = 60
vel = 5

WHITE = (255,255,255)
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

#win.blit(bg,(0,0))

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

run = True
while run:
    win.blit(bg,(0,0))
    pygame.time.delay(100)
    #all_sprites.update()
    #all_sprites.handle_keys()
    #all_sprites.draw(win)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    player.handle_keys()
    player.draw(win)
    pygame.display.flip()
    #pygame.display.update()
    

pygame.quit()