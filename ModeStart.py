import pygame
from pygame.locals import *
from Button import Button

def startDrawButtons(data, pos):
    for button in data.buttons:
        button.draw(pos, data.screen)

def startProcessClick(data, pos):
    for button in data.buttons:
        msg = button.check(pos)
        if msg != None:
            if msg == "Start":
                data.mode = "battleMode"
            elif msg == "Quit":
                pygame.quit()
                return False
    return True

def startModeButtons(data):
    buttonW = 200
    buttonH = 50
    data.buttons = {
                    Button("Start", data.windowSize[0]//3 + buttonW//2,
                           data.windowSize[1]//3 - buttonH//2,
                           buttonW, buttonH, (0, 0, 255), (255, 0, 255)),
                    Button("Quit", data.windowSize[0]//3 + buttonW//2,
                           data.windowSize[1]//3 + buttonH//2,
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
