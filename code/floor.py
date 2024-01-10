from init import *

class Floor:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def draw(self):
        screen.blit(floor, (self.x, self.y))
        screen.blit(floor, (self.x + floor.get_width(), self.y))
