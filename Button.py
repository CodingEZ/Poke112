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

    def draw(self, pos, surface):
        if (self.x + self.width > pos[0] > self.x) and (self.y + self.height > pos[1] > self.y):
            color = self.hoverColor
        else:
            color = self.normalColor
        pygame.draw.rect(surface, color, (self.x, self.y, self.width, self.height))
        smallText = pygame.font.Font(None, 25)
        surface.blit(smallText.render(self.msg, True, (255, 255, 255)),
                     (self.x + (self.width/4), self.y + (self.height/2)))

    def check(self, pos):
        if (self.x + self.width > pos[0] > self.x) and (self.y + self.height > pos[1] > self.y):
            return self.msg
        return None
