import os, sys
import time
import pygame
from pygame.locals import *

def load_image(name, colorkey=None):
    fullname = os.path.join('images', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error:
        print('Cannot load image:', name)
        raise SystemExit
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()

def run():
    if not pygame.font:
        print('Warning, fonts disabled')
    if not pygame.mixer:
        print('Warning, sound disabled')

    # Initialize
    pygame.init()
    screen = pygame.display.set_mode((400, 400))
    pygame.display.set_caption('Poke112')
    #pygame.mouse.set_visible(0)

    # Background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))

    # Text on Background
    if pygame.font:     # checks if equals to None
        font = pygame.font.Font(None, 36)
        text = font.render("Poke112", 1, (10, 10, 10))
        textpos = text.get_rect(centerx=background.get_width()/2)
        background.blit(text, textpos)

    while True:
        screen.blit(background, (0, 0))
        backImg, backImgRect = load_image('tree.png')
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


