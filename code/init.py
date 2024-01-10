import pygame

# Define constants
GRAVITY = 0.45  # Gravity constant
SPEEDFLY = -5.5  # Flying speed
NEW_PIPE_TIME = 1200  # Time to create a new pipe
MAX_PIPES_SCREEN = 6  # Maximum number of pipes on the screen
MAX_LENGTH_OF_PIPES_LIST = 3  # Maximum length of the pipes list
FPS = 2  # Frames per second

# Define screen properties
screen_width = 900  # Screen width
screen_height = 500  # Screen height
screen = pygame.display.set_mode((screen_width, screen_height))  # Create the screen

# Define bird properties
bird_width = 30  # Bird width
bird_height = 30  # Bird height
bird = ["../assets/images/bird-midflap.png", "../assets/images/bird-upflap.png", "../assets/images/bird-downflap.png"]  # Bird images

# Load the background image
background = pygame.image.load("../assets/images/background.png").convert_alpha()

# Define audio files
wing = "../assets/audio/wing.wav"  # Wing sound
score = "../assets/audio/score.wav"  # Score sound
hit = "../assets/audio/hit.ogg"  # Hit sound

# Load and scale the floor image
floor = pygame.transform.scale(pygame.image.load("../assets/images/floor.png"), (screen_width, 100)).convert_alpha()

# Define the pipe image
pipe = "../assets/images/pipe.png"

# Define the replay image
replay = "../assets/images/replay.png"

# Initialize pygame and the mixer
pygame.init()
pygame.mixer.init()

# Set the window title
pygame.display.set_caption("Flappy Bird")

# Create a clock object
clock = pygame.time.Clock()

# Define a custom event for swapping pipes
swap_pipe = pygame.USEREVENT + 1
pygame.time.set_timer(swap_pipe, NEW_PIPE_TIME)

# Define the hand cursor
HAND_CURSOR = pygame.SYSTEM_CURSOR_HAND
