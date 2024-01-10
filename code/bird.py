from init import *

class Bird:
    def __init__(self):
        self.width = bird_width
        self.height = bird_height
        self.x = 150
        self.y = screen_height / 2 - self.height / 2
        self.speed = 0
        self.count = 0
        self.rect = pygame.image.load(bird[0])
        self.bird_rect = self.rect.get_rect(center=(self.x, self.y))
        self.movement = 0
        self.is_flew = False

    def draw_bird(self):
        self.rect = pygame.image.load(bird[self.count // 18]).convert_alpha()
        screen.blit(self.rect, self.bird_rect)

    def fly(self):
        if self.count == 53: self.count = 0
        self.count += 1
        self.movement += GRAVITY if self.is_flew else 0
        self.bird_rect.centery += self.movement if self.is_flew else 0
