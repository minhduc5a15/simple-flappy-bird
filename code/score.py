from init import *

class Score:
    def __init__(self):
        self.score = 0
        self.font = pygame.font.Font(None, 36)
        self.score_sound = pygame.mixer.Sound(score)

    def increment(self):
        self.score_sound.play()
        self.score += 1

    def draw(self, screen):
        score_text = self.font.render(f'Score: {self.score}', True, (255, 255, 255))
        screen.blit(score_text, (10, 10))
