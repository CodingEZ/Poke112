import pygame
from pygame.locals import *
from Button import Button

def startProcessButtons(data):
    for button in data.buttons:
        button.draw(data.screen)
        msg = button.check()
        if msg != None:
            if msg == "Start":
                data.mode = "battleMode"
            elif ms == "Quit":
                pygame.quit()
                return False
    return True

def startModeButtons(data):
    buttonW = 100
    buttonH = 50
    data.buttons = {
                    Button("Start", data.windowSize[0]//2 + buttonW//2,
                           data.windowSize[1]//2 - buttonH//2,
                           buttonW, buttonH, (0, 0, 255), (255, 0, 255)),
                    Button("Quit", data.windowSize[0]//2 + buttonW//2,
                           data.windowSize[1]//2 + buttonH//2,
                           buttonW, buttonH, (0, 0, 255), (255, 0, 255))
                    }

def startModeEvents(data):
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            return False
        elif event.type == KEYDOWN:
            pass            
        elif event.type == MOUSEBUTTONDOWN:
            # make some kind of move?
            pass
    return True
