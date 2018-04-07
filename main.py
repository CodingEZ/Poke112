import os, sys
import pygame
from pygame.locals import *
from ImageEdit import *
from ModeStart import *
from ModeBattle import *
from ModeMove import *
from ModeItem import *
from Student import *
from TA import *
from Move2 import *

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
            move = moveProcessClick(data, pos)
            if move == False:       return False
            data.move = move
            data.mode == "battleMode"
        elif data.mode == "itemMode":
            item = itemProcessClick(data, pos)
            if item == False:       return False
            data.mode == "battleMode"
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

    data.move = None
    data.student = Student(data)
    data.ta = TA(data)

    move1 = RegradeReq(data.screen)
    move2 = ThreeAMPiazza(data.screen)
    move3 = Sleep(data.student, data.screen)
    move4 = OHQueue(data.student, data.screen)
    move5 = Style(data.student, data.screen)
    move6 = FixProjector(data.screen)
    move7 = VagueAnswers(data.ta, data.screen)
    move8 = Clap(data.screen)

    while True:
        drawScreen(data)
        drawButtons(data)
        drawStudent(data)
        drawTA(data)
        if not switchScreens(data):     return
        if data.move == "RegradeReq":
            move1.animate(data.screen)
            move1.damage(data.student, data.ta)
        elif data.move == "ThreeAMPiazza":
            move2.animate(data.screen)
            move2.damage(data.student, data.ta)
        elif data.move == "Sleep":
            move3.animate(data.screen)
            move3.damage(data.student, data.ta)
        elif data.move == "OHQueue":
            move4.animate(data.screen)
            move4.damage(data.student, data.ta)
        elif data.move == "Style":
            move5.animate(data.screen)
            move5.damage(data.ta, data.student)
        elif data.move == "FixProjector":
            move6.animate(data.screen)
            move6.damage(data.ta, data.student)
        elif data.move == "VagueAnswers":
            move7.animate(data.screen)
            move7.damage(data.ta, data.student)
        elif data.move == "Clap":
            move8.animate(data.screen)
            move8.damage(data.ta, data.student)
        pygame.display.flip()

run(800, 600)
print("Thank you for playing! :)")

