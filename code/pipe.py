import random

from init import *

MIN_HEIGHT_DISPLAY = 100
MAX_HEIGHT_DISPLAY = 385
MIN_SPACE_BETWEEN_TWO_PIPES = 45
MAX_SPACE_BETWEEN_TWO_PIPES = 80
# create pipes

class Pipe:
    def __init__(self):
        self.pipe_height_list = [i for i in range(MIN_HEIGHT_DISPLAY, MAX_HEIGHT_DISPLAY - MIN_HEIGHT_DISPLAY + 1)]
        self.space_between_two_pipes_list = [i for i in range(MIN_SPACE_BETWEEN_TWO_PIPES, MAX_SPACE_BETWEEN_TWO_PIPES + 1)]
        self.pipe_bottom = pygame.transform.scale(pygame.image.load(pipe).convert_alpha(), (45, MAX_HEIGHT_DISPLAY))
        self.pipe_top = pygame.transform.rotate(self.pipe_bottom.copy(), 180)
        self.pipe_list = []
        self.middle_of_screen = screen_height // 2 - 25  # 500 / 2 - 25 = 225

    def create_pipe(self):
        pipe_top_height = random.choice(self.pipe_height_list)
        space_between_two_pipes = random.choice(self.space_between_two_pipes_list)
        pipe_top = self.pipe_top.get_rect(midtop=(900, -pipe_top_height))
        pipe_bottom = self.pipe_bottom.get_rect(midtop=(900, 450 - max((pipe_top_height - space_between_two_pipes, MIN_HEIGHT_DISPLAY))))
        # print(pipe_top_height)
        self.pipe_list.append((pipe_bottom, pipe_top))

    def move_pipe(self):
        for pipe_bottom, pipe_top in self.pipe_list:
            pipe_bottom.centerx -= 5
            pipe_top.centerx -= 5
        return self.pipe_list

    def draw_pipe(self):
        for pipe_bottom, pipe_top in self.pipe_list:
            screen.blit(self.pipe_bottom, pipe_bottom)
            screen.blit(self.pipe_top, pipe_top)
        if len(self.pipe_list) > MAX_LENGTH_OF_PIPES_LIST:
            self.pipe_list.pop(0)
