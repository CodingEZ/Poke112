import os, sys
import pygame
from pygame.locals import *
from ImageEdit import *
from ModeStart import *
from ModeBattle import *
from ModeMove import *
from ModeItem import *

class Data():
    def __repr__(self):
        attrs = vars(self)
        result = ""
        for attr in attrs:
            if attr != "windowSize" and attr != "screen" and attr != "background" and attr != "backgroundImg":
                result += str(attr) + " " + str(eval("self." + str(attr))) + '\n'
        return result + '\n'

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
    data.message = None
    initScreen(data)
    initBackground(data)

    while True:
        data.background.blit(data.backgroundImg, [0, 0])
        data.screen.blit(data.background, (0, 0))
        drawTitle(data)

        draw = False
        click = False
        events = pygame.event.get()
        if len(events) > 0:
            event = events[0]
            if event.type == MOUSEMOTION:
                draw = True
            elif event.type == MOUSEBUTTONDOWN:
                click = True

        if data.mode == "startMode":
            startModeButtons(data)
            if draw:
                if not startDrawButtons(data, pos):           return
            elif click:
                if not startProcessClick(data, pos):   return
        elif data.mode == "battleMode":
            battleModeButtons(data)
            if draw:
                if not battleDrawButtons(data, pos):           return
            elif click:
                if not battleProcessClick(data, pos):   return
        elif data.mode == "moveMode":
            moveModeButtons(data)
            if draw:
                if not moveDrawButtons(data, pos):           return
            elif click:
                if not moveProcessClick(data, pos):   return
        elif data.mode == "itemMode":
            itemModeButtons(data)
            if draw:
                if not itemDrawButtons(data, pos):           return
            elif click:
                if not itemProcessClick(data, pos):   return
        else:
            pass
        # other game modes
        
        pygame.display.flip()
        data.message = None

run(800, 600)
print("Thank you for playing! :)")

# possible game modes:
    # battleMode
    # menuMode
    # attackMode
    # itemMode

