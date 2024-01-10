from init import *

# Define a class for the score
class Score:
    # Initialize the score with its properties
    def __init__(self):
        self.score = 0  # Initial score
        self.font = pygame.font.Font(None, 36)  # Font of the score
        self.score_sound = pygame.mixer.Sound(score)  # Sound when the score is incremented

    # Method to increment the score
    def increment(self):
        self.score_sound.play()  # Play the score sound
        self.score += 1  # Increment the score

    # Method to draw the score on the screen
    def draw(self, screen):
        score_text = self.font.render(f'Score: {self.score}', True, (255, 255, 255))  # Render the score text
        screen.blit(score_text, (10, 10))  # Draw the score text on the screen
