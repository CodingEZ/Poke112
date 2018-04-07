import os, sys
import time
import pygame
from pygame.locals import *
from PIL import Image

class TA:
    def __init__(self):
        # position of TA 
        self.img = pygame.image.load('pikachu copy copy.jpg')
        self.width = 400 
        self.height = 400
        self.x = 0
        self.y = 0
        self.display = pygame.display.set_mode((self.width,self.height))
        self.speed = 10
        self.time = 0
        self.hand = pygame.image.load('open-hand-clip-art-9TzMxyAqc.png')
        # position of hands 
        self.xhand,self.yhand = 250,50
        self.xhand1,self.yhand1 = 150,200
        style = pygame.font.Font(None, 48)
        self.text = style.render('-2', True, (255, 0, 0))
        self.textRect = eval(str(self.text.get_rect(center=(200,200)))[5:-1])
        self.sound = False 
        self.points = "-2"
        
    
    def drawTA(self,screen):
        screen.blit(self.img,(self.x,self.y))
    
    def drawHands(self,screen):
        screen.blit(self.hand,(self.xhand,self.yhand))
        screen.blit(self.hand,(self.xhand1,self.yhand1))
        if self.sound==True and self.xhand==self.xhand1:
            pygame.draw.polygon(screen,(0,0,0),[(200,100),(220,90),(225,150),(210,160)])
            pygame.draw.polygon(screen,(0,0,0),[(250,50),(270,40),(275,100),(260,110)])
            pygame.draw.polygon(screen,(0,0,0),[(320,60),(340,50),(345,110),(330,120)])
            self.sound=False 
            
        
    def moveHands(self):
        self.xhand-=self.speed
        self.xhand1+=self.speed
        self.yhand+=self.speed
        self.yhand1-=self.speed 
        
    def drawBadStyle(self,screen):
        styleText = pygame.font.Font(None, 25)
        screen.blit(styleText.render(self.points, True, (255, 255, 255)),
                     (400, 400))
    

    
class PygameGame(object):

    def init(self):
        self.ta = TA()
        self.speed = 2 
        self.time = 0 
        self.sound = True 
        self.style = False 
        self.clap = False 

    def mousePressed(self, x, y):
        pass

    def mouseReleased(self, x, y):
        pass

    def mouseMotion(self, x, y):
        pass

    def mouseDrag(self, x, y):
        pass

    def keyPressed(self, keyCode, modifier):
        print('a')
        pass  
        

    def keyReleased(self, keyCode, modifier):
        pass 
    
    def pressedKey(self,event):
        if event==pygame.K_UP:
            self.clap = True 
        elif event==pygame.K_DOWN:
            self.style = True 
        
    
    
    def timerFired(self, dt):
        self.time+=1
        if self.time%2==0:
            self.ta.y-=self.speed
        else:
            self.ta.y+=self.speed 
            
        if self.clap:
            if (self.ta.xhand!=self.ta.xhand1 and self.ta.yhand!=self.ta.yhand1):
                self.ta.moveHands()
            

    def redrawAll(self, screen):
        screen.blit(self.ta.img,(self.ta.x,self.ta.y))
        if self.clap:
            self.ta.drawHands(screen)
        if self.style:
            self.ta.drawBadStyle(screen)
            

    def __init__(self, width=600, height=400, fps=50, title="112 Pygame Game"):
        self.width = width
        self.height = height
        self.fps = fps
        self.title = title
        self.bgColor = (255, 255, 255)
        pygame.init()

    def run(self):
        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((self.width, self.height))
        # set the title of the window
        pygame.display.set_caption(self.title)

        # stores all the keys currently being held down
        self._keys = dict()

        # call game-specific initialization
        self.init()
        playing = True
        while playing:
            time = clock.tick(self.fps)
            self.timerFired(time)
            for event in pygame.event.get():
                self.clap = False
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.mousePressed(*(event.pos))
                elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    self.mouseReleased(*(event.pos))
                elif (event.type == pygame.MOUSEMOTION and
                      event.buttons == (0, 0, 0)):
                    self.mouseMotion(*(event.pos))
                elif (event.type == pygame.MOUSEMOTION and
                      event.buttons[0] == 1):
                    self.mouseDrag(*(event.pos))
                if event.type == pygame.KEYDOWN:
                    self._keys[event.key] = True
                    self.pressedKey(event.key)
                    self.keyPressed(event.key, event.mod)
                elif event.type == pygame.KEYUP:
                    print("hereeeee")
                    # BAD STYLE 
                    #self._keys[event.key] = False
                    self.keyReleased(event.key, event.mod)
                elif event.type == pygame.QUIT:
                    playing = False
            screen.fill(self.bgColor)
            self.ta.drawTA(screen)
            self.redrawAll(screen)
            pygame.display.flip()
        pygame.quit()


def main():
    game = PygameGame()
    game.run()

if __name__ == '__main__':
    main()
