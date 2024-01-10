from init import *

# Define a class for the floor
class Floor:
    # Initialize the floor with its properties
    def __init__(self, x: int, y: int):
        self.x = x  # x-coordinate of the floor
        self.y = y  # y-coordinate of the floor

    # Method to draw the floor on the screen
    def draw(self):
        screen.blit(floor, (self.x, self.y))  # Draw the first part of the floor on the screen
        screen.blit(floor, (self.x + floor.get_width(), self.y))  # Draw the second part of the floor on the screen
