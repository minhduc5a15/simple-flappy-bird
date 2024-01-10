import random
from init import *

# Define the minimum and maximum display height for the pipes
MIN_HEIGHT_DISPLAY = 100
MAX_HEIGHT_DISPLAY = 385

# Define the minimum and maximum space between two pipes
MIN_SPACE_BETWEEN_TWO_PIPES = 45
MAX_SPACE_BETWEEN_TWO_PIPES = 80

# Define a class for the pipes
class Pipe:
    # Initialize the pipe with its properties
    def __init__(self):
        # Create a list of possible pipe heights
        self.pipe_height_list = [i for i in range(MIN_HEIGHT_DISPLAY, MAX_HEIGHT_DISPLAY - MIN_HEIGHT_DISPLAY + 1)]
        # Create a list of possible spaces between two pipes
        self.space_between_two_pipes_list = [i for i in range(MIN_SPACE_BETWEEN_TWO_PIPES, MAX_SPACE_BETWEEN_TWO_PIPES + 1)]
        # Load the bottom pipe image and scale it to the maximum display height
        self.pipe_bottom = pygame.transform.scale(pygame.image.load(pipe).convert_alpha(), (45, MAX_HEIGHT_DISPLAY))
        # Create the top pipe image by rotating the bottom pipe image 180 degrees
        self.pipe_top = pygame.transform.rotate(self.pipe_bottom.copy(), 180)
        # Initialize the list of pipes
        self.pipe_list = []
        # Calculate the middle of the screen
        self.middle_of_screen = screen_height // 2 - 25  # 500 / 2 - 25 = 225

    # Method to create a pipe
    def create_pipe(self):
        # Randomly select a height for the top pipe
        pipe_top_height = random.choice(self.pipe_height_list)
        # Randomly select a space between the two pipes
        space_between_two_pipes = random.choice(self.space_between_two_pipes_list)
        # Create the top pipe rectangle
        pipe_top = self.pipe_top.get_rect(midtop=(900, -pipe_top_height))
        # Create the bottom pipe rectangle
        pipe_bottom = self.pipe_bottom.get_rect(midtop=(900, 450 - max((pipe_top_height - space_between_two_pipes, MIN_HEIGHT_DISPLAY))))
        # Add the pipe to the list of pipes
        self.pipe_list.append((pipe_bottom, pipe_top))

    # Method to move the pipes
    def move_pipe(self):
        for pipe_bottom, pipe_top in self.pipe_list:
            # Move the bottom pipe to the left
            pipe_bottom.centerx -= 5
            # Move the top pipe to the left
            pipe_top.centerx -= 5
        # Return the list of pipes
        return self.pipe_list

    # Method to draw the pipes
    def draw_pipe(self):
        for pipe_bottom, pipe_top in self.pipe_list:
            # Draw the bottom pipe on the screen
            screen.blit(self.pipe_bottom, pipe_bottom)
            # Draw the top pipe on the screen
            screen.blit(self.pipe_top, pipe_top)
        # Remove the first pipe from the list if the list is too long
        if len(self.pipe_list) > MAX_LENGTH_OF_PIPES_LIST:
            self.pipe_list.pop(0)
