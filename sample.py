import os, sys
import time
import pygame
from pygame.locals import *
from PIL import Image
from ImageEdit import *

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
        self.sound = True 
        self.points = "-2"
        
    
    def drawTA(self,screen):
        screen.blit(self.img,(self.x,self.y))
    
    # Draw hands then claps them once 
    # need to figure out how to end this once clap has ended 
    def drawHands(self,screen):
        screen.blit(self.hand,(self.xhand,self.yhand))
        screen.blit(self.hand,(self.xhand1,self.yhand1))
        if self.sound==True and self.xhand==self.xhand1:
            # slap uploaded slap sound 
            sound = pygame.mixer.Sound('Slap-SoundMaster13-49669815.wav')
            sound.play()
            pygame.draw.polygon(screen,(0,0,0),[(200,100),(220,90),(225,150),(210,160)])
            pygame.draw.polygon(screen,(0,0,0),[(250,50),(270,40),(275,100),(260,110)])
            pygame.draw.polygon(screen,(0,0,0),[(320,60),(340,50),(345,110),(330,120)])
    
    # NEEd it to move hands!!    
    def moveHands(self):
        self.xhand-=self.speed
        self.xhand1+=self.speed
        self.yhand+=self.speed
        self.yhand1-=self.speed 
   
    # NEEDs to call this with a certain button     
    def drawBadStyle(self,screen):
        styleText = pygame.font.Font(None, 25)
        # SCratching sound
        sound = pygame.mixer.Sound('Scratching-Lisa_Redfern-839241243.wav')
        sound.play(0,1000,0)
        screen.blit(styleText.render(self.points, True, (255, 0, 0)),
                     (150, 150))

# PROFESSOR ATTACKS -
class Professor:
    def __init__(self):
        pass 
        
  # 1 PROFESSOR ATTACK IS RECURSION      
    def recursion(self,screen,x,y,size,level):
        if level==0:
            sound = pygame.mixer.Sound('Alien_siren-KevanGC-610357990.wav')
            sound.play(0,1000,0)
            pygame.draw.polygon(screen,(0,0,0),[(x, y,),(x+size, y),
                              (x+size/2, y-size*(3**0.5)/2)])
        else:
            self.recursion( screen,x, y, size/2, level-1)
            self.recursion( screen,x+size/2, y, size/2, level-1)
            self.recursion( screen,x+size/4, y-size*(3**0.5)/4, size/2, level-1)
    
    
class PygameGame(object):
    # initializing stuff 
    def init(self):
        self.ta = TA()
        self.speed = 2 
        self.time = 0 
        self.style = False 
        self.clap = False 
        self.recursion= False
        self.prof = Professor()
         

    def mousePressed(self, x, y):
        pass

    def mouseReleased(self, x, y):
        pass

    def mouseMotion(self, x, y):
        pass

    def mouseDrag(self, x, y):
        pass

    def keyPressed(self, keyCode, modifier):
        pass  
        

    def keyReleased(self, keyCode, modifier):
        pass 
    
    def pressedKey(self,event):
        if event==pygame.K_UP:
            self.clap = True 
        elif event==pygame.K_DOWN:
            self.style = True 
        
    
    # need this too 
    # controls how long features show up 
    def timerFired(self, dt):
        self.time+=1
        # bobbing players 
        if self.time%2==0:
            self.ta.y-=self.speed
        else:
            self.ta.y+=self.speed
        # controlling movement of clap and resetting position after 1 clap once
        if self.clap:
            if (self.ta.xhand!=self.ta.xhand1 and self.ta.yhand!=self.ta.yhand1):
                self.ta.moveHands()
            else:
                self.clap = False 
                self.ta.xhand,self.ta.yhand = 250,50
                self.ta.xhand1,self.ta.yhand1 = 150,200
        # recursion and style features that stay on screen for a second before disappearing
        # increase mod to allow features to stay on screen for longer 
        if self.recursion:
            if self.time % 20==0:
                self.recursion= False 
        if self.style:
            if self.time % 20==0:
                self.style = False 
                


    # need this too 
    def redrawAll(self, screen):
        self.ta.drawTA(screen)
        if self.recursion:
            self.prof.recursion(screen,100,100,100,3)
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
                    self.clap = True 
                    self.style = True 
                    self.recursion = True 
                    self.keyPressed(event.key, event.mod)
                elif event.type == pygame.KEYUP:
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
