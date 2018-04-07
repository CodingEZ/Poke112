import pygame
from pygame.locals import *
from Button import Button

def moveDrawButtons(data, pos):
    for button in data.buttons:
        button.draw(pos, data.screen)

def moveProcessClick(data, pos):
    for button in data.buttons:
        msg = button.check(pos)
        if msg != None:
            if msg == "Back":
                data.mode = "battleMode"
            elif msg == "Quit":
                pygame.quit()
                return False
            else:
                data.mode = "battleMode"
    return True

def moveModeButtons(data):
    buttonW = 200
    buttonH = 50

    moves = data.student.moveSet
    data.buttons = []
    for index in range(len(moves)):
        data.buttons.append( Button(moves[index], data.windowSize[0]//10 - buttonW//2,
                               data.windowSize[1]//10 - buttonH//2 + index * buttonH,
                               buttonW, buttonH, (0, 0, 255), (255, 0, 255)) )
    data.buttons.append( Button("Back", data.windowSize[0]//10 - buttonW//2,
                           data.windowSize[1]//10 - buttonH//2 + (index+1) * buttonH,
                           buttonW, buttonH, (0, 0, 255), (255, 0, 255)) )
    data.buttons.append( Button("Quit", data.windowSize[0]//10 - buttonW//2,
                           data.windowSize[1]//10 - buttonH//2 + (index+2) * buttonH,
                           buttonW, buttonH, (0, 0, 255), (255, 0, 255)) )

def moveModeEvents(data):
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
