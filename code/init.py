import pygame

# constant
GRAVITY = 0.45
SPEEDFLY = -5.5
NEW_PIPE_TIME = 1200
MAX_PIPES_SCREEN = 6
MAX_LENGTH_OF_PIPES_LIST = 3
FPS = 2
# screen
screen_width = 900
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))

# bird
bird_width = 30
bird_height = 30
bird = ["../assets/images/bird-midflap.png", "../assets/images/bird-upflap.png", "../assets/images/bird-downflap.png"]

# background
background = pygame.image.load("../assets/images/background.png").convert_alpha()

# audio
wing = "../assets/audio/wing.wav"
score = "../assets/audio/score.wav"
hit = "../assets/audio/hit.ogg";
# floor
floor = pygame.transform.scale(pygame.image.load("../assets/images/floor.png"), (screen_width, 100)).convert_alpha()

# pipe
pipe = "../assets/images/pipe.png"
# replay
replay = "../assets/images/replay.png"
# init
pygame.init()
pygame.mixer.init()
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()
swap_pipe = pygame.USEREVENT + 1
pygame.time.set_timer(swap_pipe, NEW_PIPE_TIME)
HAND_CURSOR = pygame.SYSTEM_CURSOR_HAND
