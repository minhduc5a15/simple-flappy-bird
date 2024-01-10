from init import *
# create Button class
class Button:
    def __init__(self, text):
        self.text = text
        self.width = 160
        self.height = 50
        self.x = (screen_width - self.width) / 2
        self.y = (screen_height - self.height) / 2
        self.button = pygame.image.load(replay).convert_alpha()

    def draw(self):
        screen.blit(self.button, (self.x, self.y))

    def is_over(self, pos):
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                return True
        return False
