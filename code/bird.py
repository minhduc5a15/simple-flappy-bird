from init import *

# Define a class for the bird
class Bird:
    # Initialize the bird with its properties
    def __init__(self):
        self.width = bird_width  # Width of the bird
        self.height = bird_height  # Height of the bird
        self.x = 150  # Initial x-coordinate of the bird
        self.y = screen_height / 2 - self.height / 2  # Initial y-coordinate of the bird
        self.speed = 0  # Initial speed of the bird
        self.count = 0  # Counter for the bird's movement
        self.rect = pygame.image.load(bird[0])  # Load the bird's image
        self.bird_rect = self.rect.get_rect(center=(self.x, self.y))  # Get the bird's rectangle
        self.movement = 0  # Initial movement of the bird
        self.is_flew = False  # Flag to check if the bird has flown

    # Method to draw the bird on the screen
    def draw_bird(self):
        self.rect = pygame.image.load(bird[self.count // 18]).convert_alpha()  # Load the bird's image with transparency
        screen.blit(self.rect, self.bird_rect)  # Draw the bird on the screen

    # Method for the bird to fly
    def fly(self):
        if self.count == 53: self.count = 0  # Reset the counter if it reaches 53
        self.count += 1  # Increment the counter
        self.movement += GRAVITY if self.is_flew else 0  # Add gravity to the movement if the bird has flown
        self.bird_rect.centery += self.movement if self.is_flew else 0  # Update the bird's y-coordinate if the bird has flown
