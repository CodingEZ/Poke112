import pygame

class Button():
    def __init__(self, msg, x, y, w, h, nc, hc):
        self.msg = msg
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.normalColor = nc
        self.hoverColor = hc

    def draw(self, mouse, click, surface):
        if (self.x + self.width > mouse[0] > self.x) and (self.y + self.height > mouse[1] > self.y):
            color = self.hoverColor
        else:
            color = self.normalColor
        pygame.draw.rect(surface, color, (self.x, self.y, self.width, self.height))
        smallText = pygame.font.Font(None, 25)
        surface.blit(smallText.render(self.msg, True, (255, 255, 255)),
                     (self.x + (self.width/4), self.y + (self.height/2)))

    def check(self, mouse, click):
        if (self.x + self.width > mouse[0] > self.x) and (self.y + self.height > mouse[1] > self.y):
            if click[0] == 1:
                return self.msg
        return None
