import pygame
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

# this code maintains the aspect ratio
'''
def resize_image(name, windowWidth):
    img = Image.open('images/' + name)
    img.thumbnail(windowWidth, Image.ANTIALIAS)
    img.save('images/fit_' + name, 'JPEG')
'''

def resize_image(name, windowWidth):
    img = Image.open('images/' + name)
    
    width = windowWidth[0]
    img = Image.open('images/' + name)
    widthChange = (width / float(img.size[0]))
    newHeight = int((float(img.size[1]) * float(widthChange)))
    img = img.resize((width, newHeight), Image.ANTIALIAS)

    height = windowWidth[1]
    img = Image.open('images/' + name)
    heightChange = (height / float(img.size[1]))
    newWidth = int((float(img.size[0]) * float(heightChange)))
    img = img.resize((newWidth, height), Image.ANTIALIAS)
    img.save('images/fit_' + name, 'JPEG')
