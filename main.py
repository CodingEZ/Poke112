import os, sys
import pygame
from pygame.locals import *
from ImageEdit import *
from ModeStart import *
from ModeBattle import *
from ModeMove import *
from ModeItem import *

class Data():
    pass

def initScreen(data):
    pygame.init()
    data.screen = pygame.display.set_mode(data.windowSize)
    pygame.display.set_caption('Poke112')
    #pygame.mouse.set_visible(0)

def initBackground(data):
    data.background = pygame.Surface(data.screen.get_size())
    data.background = data.background.convert()
    data.background.fill((250, 250, 250))
    imgName = 'gates.jpg'
    resize_image(imgName, data.windowSize)      # in ImageEdit class
    data.backgroundImg = load_image(imgName)[0] # in ImageEdit class

def drawTitle(data):
    # Text on Screen
    if pygame.font:     # checks if equals to None
        font = pygame.font.Font(None, 36)
        text = font.render("Poke112", 1, (10, 10, 10))
        textpos = text.get_rect(centerx = data.screen.get_width()/2)
        data.screen.blit(text, textpos)

##############################################################
# run function to call
##############################################################

def run(width=400, height=400):
    if not pygame.font:     print('Warning, fonts disabled')
    if not pygame.mixer:    print('Warning, sound disabled')

    data = Data()
    data.windowSize = (width, height)
    data.mode = "startMode"
    initScreen(data)
    initBackground(data)

    while True:
        data.background.blit(data.backgroundImg, [0, 0])
        data.screen.blit(data.background, (0, 0))
        drawTitle(data)

        if data.mode == "startMode":
            startModeButtons(data)
            if not startProcessButtons(data):   return
            if not startModeEvents(data):   return
        elif data.mode == "battleMode":
            battleModeButtons(data)
            if not battleProcessButtons(data):  return
            if not battleModeEvents(data):  return
        elif data.mode == "moveMode":
            moveModeButtons(data)
            if not moveProcessButtons(data):    return
            if not moveModeEvents(data):    return
        elif data.mode == "itemMode":
            itemModeButtons(data)
            if not itemProcessButtons(data):    return
            if not itemModeEvents(data):    return
        else:
            pass
        # other game modes
        
        pygame.display.flip()

run(800, 600)
print("Thank you for playing! :)")

# possible game modes:
    # battleMode
    # menuMode
    # attackMode
    # itemMode

