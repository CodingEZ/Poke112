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
        self.update()

    def update(self):
        self.mouse = pygame.mouse.get_pos()
        self.click = pygame.mouse.get_pressed()

    def draw(self, surface):
        self.update()
        if (self.x + self.width > self.mouse[0] > self.x) and (self.y + self.height > self.mouse[1] > self.y):
            color = self.hoverColor
        else:
            color = self.normalColor
        pygame.draw.rect(surface, color, (self.x, self.y, self.width, self.height))
        smallText = pygame.font.Font(None, 25)
        surface.blit(smallText.render(self.msg, True, (255, 255, 255)),
                     (self.x + (self.width/4), self.y + (self.height/2)))

    def check(self):
        if (self.x + self.width > self.mouse[0] > self.x) and (self.y + self.height > self.mouse[1] > self.y):
            if self.click[0] == 1:
                return self.msg
        return None
