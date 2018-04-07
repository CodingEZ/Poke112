import pygame
from pygame.locals import *
from Button import Button

def battleProcessButtons(data):
    for button in data.buttons:
        button.draw(data.screen)
        msg = button.check()
        if msg != None:
            if msg == "Quit":
                pygame.quit()
                return False
            elif msg == "Moves":
                data.mode = "moveMode"
            elif msg == "Items":
                data.mode = "itemMode"
    return True

def battleModeButtons(data):
    buttonW = 100
    buttonH = 50
    data.buttons = {
                    Button("Moves", data.windowSize[0]//10 - buttonW//2,
                           data.windowSize[1]//10 - buttonH//2,
                           buttonW, buttonH, (0, 0, 255), (255, 0, 255)),
                    Button("Items", data.windowSize[0]//10 - buttonW//2,
                           data.windowSize[1]//10 + buttonH//2,
                           buttonW, buttonH, (0, 0, 255), (255, 0, 255)),
                    Button("Quit", data.windowSize[0]//10 - buttonW//2,
                           data.windowSize[1]//10 + 3*buttonH//2,
                           buttonW, buttonH, (0, 0, 255), (255, 0, 255))
                    }

def battleModeEvents(data):
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
