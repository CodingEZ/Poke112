import os, sys
import pygame
from pygame.locals import *
from ImageEdit import *
from ModeStart import *
from ModeBattle import *
from ModeMove import *
from ModeItem import *
from Student import *

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

def drawScreen(data):
    data.background.blit(data.backgroundImg, [0, 0])
    data.screen.blit(data.background, (0, 0))
    drawTitle(data)

    if data.mode == "startMode":
        startModeButtons(data)
    elif data.mode == "battleMode":
        battleModeButtons(data)
    elif data.mode == "moveMode":
        moveModeButtons(data)
    elif data.mode == "itemMode":
        itemModeButtons(data)

def drawButtons(data):
    pos = pygame.mouse.get_pos()
    if data.mode == "startMode":
        startDrawButtons(data, pos)
    elif data.mode == "battleMode":
        battleDrawButtons(data, pos)
    elif data.mode == "moveMode":
        moveDrawButtons(data, pos)
    elif data.mode == "itemMode":
        itemDrawButtons(data, pos)

def switchScreens(data):
    events = pygame.event.get()
    clicked = False
    if len(events) > 0:
        event = events[0]
        if event.type == MOUSEBUTTONDOWN:
            clicked = True
            pos = event.pos
        else:
            pass

    if clicked:
        if data.mode == "startMode":
            if not startProcessClick(data, pos):    return False
        elif data.mode == "battleMode":
            if not battleProcessClick(data, pos):   return False
        elif data.mode == "moveMode":
            if not moveProcessClick(data, pos):     return False
        elif data.mode == "itemMode":
            if not itemProcessClick(data, pos):     return False
    return True

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
    student = Student
    while True:
        drawScreen(data)
        
        drawButtons(data)
        if not switchScreens(data):     return
        pygame.display.flip()

run(800, 600)
print("Thank you for playing! :)")

# possible game modes:
    # battleMode
    # menuMode
    # attackMode
    # itemMode