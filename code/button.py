from init import *

# Define a class for the button
class Button:
    # Initialize the button with its properties
    def __init__(self, text):
        self.text = text  # Text of the button
        self.width = 160  # Width of the button
        self.height = 50  # Height of the button
        self.x = (screen_width - self.width) / 2  # x-coordinate of the button
        self.y = (screen_height - self.height) / 2  # y-coordinate of the button
        self.button = pygame.image.load(replay).convert_alpha()  # Load the button's image with transparency

    # Method to draw the button on the screen
    def draw(self):
        screen.blit(self.button, (self.x, self.y))  # Draw the button on the screen

    # Method to check if the mouse is over the button
    def is_over(self, pos):
        if self.x < pos[0] < self.x + self.width:  # Check if the mouse's x-coordinate is within the button's width
            if self.y < pos[1] < self.y + self.height:  # Check if the mouse's y-coordinate is within the button's height
                return True  # Return True if the mouse is over the button
        return False  # Return False if the mouse is not over the button
