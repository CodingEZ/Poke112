import os, sys
import pygame
from pygame.locals import *
from ImageEdit import *

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
    resize_image(imgName, data.windowSize)     # in ImageEdit class
    data.backgroundImg = load_image(imgName)[0] # in ImageEdit class

    # Text on Background
    if pygame.font:     # checks if equals to None
        font = pygame.font.Font(None, 36)
        text = font.render("Poke112", 1, (10, 10, 10))
        textpos = text.get_rect(centerx = data.background.get_width()/2)
        data.background.blit(text, textpos)

def run(width=400, height=400):
    if not pygame.font:
        print('Warning, fonts disabled')
    if not pygame.mixer:
        print('Warning, sound disabled')

    data = Data()
    data.windowSize = (width, height)
    initScreen(data)
    initBackground(data)

    while True:
        data.background.blit(data.backgroundImg, [0, 0])
        data.screen.blit(data.background, (0, 0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                return
            elif event.type == MOUSEBUTTONDOWN:
                # make some kind of move?
                pass
            elif event.type == MOUSEBUTTONUP:
                # unmake some kind of move?
                pass
        pygame.display.flip()

run(400, 400)
print("Thank you for playing! :)")


