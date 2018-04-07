import os, sys
import time
import pygame
from pygame.locals import *
from PIL import Image

def load_image(name, colorkey=None):
    fileName = 'images/fit_' + name
    try:
        image = pygame.image.load(fileName)
    except pygame.error:
        print('Cannot load image:', fileName)
        raise SystemExit
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()

'''
def resize_image(name, windonewWidth):
    img = Image.open('images/' + name)
    img.thumbnail(windonewWidth, Image.ANTIALIAS)
    img.save('images/fit_' + name, 'JPEG')
'''

def resize_image(name, windonewWidth):
    img = Image.open('images/' + name)
    
    width = windonewWidth[0]
    img = Image.open('images/' + name)
    widthChange = (width / float(img.size[0]))
    newHeight = int((float(img.size[1]) * float(widthChange)))
    img = img.resize((width, newHeight), Image.ANTIALIAS)

    height = windonewWidth[1]
    img = Image.open('images/' + name)
    heightChange = (height / float(img.size[1]))
    newWidth = int((float(img.size[0]) * float(heightChange)))
    img = img.resize((newWidth, height), Image.ANTIALIAS)
    img.save('images/fit_' + name, 'JPEG')

def run():
    if not pygame.font:
        print('Warning, fonts disabled')
    if not pygame.mixer:
        print('Warning, sound disabled')

    # Initialize
    pygame.init()
    windonewWidth = (400, 400)
    screen = pygame.display.set_mode((400, 400))
    pygame.display.set_caption('Poke112')
    #pygame.mouse.set_visible(0)

    # Background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))
    imgName = 'gates.jpg'
    resize_image(imgName, windonewWidth)
    backgroundImg = load_image(imgName)[0]

    # Text on Background
    if pygame.font:     # checks if equals to None
        font = pygame.font.Font(None, 36)
        text = font.render("Poke112", 1, (10, 10, 10))
        textpos = text.get_rect(centerx=background.get_width()/2)
        background.blit(text, textpos)

    while True:
        background.blit(backgroundImg, [0, 0])
        screen.blit(background, (0, 0))
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

run()
print("Thank you for playing! :)")


