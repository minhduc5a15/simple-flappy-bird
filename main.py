import sys
from components import *

class Game:
    def __init__(self):
        # create components
        self.bird = Bird()
        self.floor = Floor(0, screen_height - 50)
        self.pipe = Pipe()
        self.score = Score()
        self.start_button = Button("START")
        # create state properties
        self.running = True
        self.passed_pipe = False
        self.started_game = False
        self.ended_game = False
        self.hit_sound = pygame.mixer.Sound(hit)
        self.hit_pipe = False

    # increase score when the bird moves over the pipe
    def increase_score(self):
        if self.pipe.pipe_list:
            if (self.bird.bird_rect.centerx > self.pipe.pipe_list[0][1].centerx and self.bird.bird_rect.centerx > self.pipe.pipe_list[0][0].centerx) and not self.passed_pipe:
                self.score.increment()
                self.passed_pipe = True
            elif self.bird.bird_rect.centerx < self.pipe.pipe_list[0][1].centerx and self.bird.bird_rect.centerx < self.pipe.pipe_list[0][0].centerx:
                self.passed_pipe = False

    # define animation of the bird
    def bird_animation(self, event):
        if event.type == pygame.KEYDOWN:
            # when press space or key up, the bird will fly
            if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                self.bird.is_flew = True
                # play wing sound
                pygame.mixer.music.load(wing)
                pygame.mixer.music.play()
                pygame.mixer.music.set_volume(0.4)
                if self.bird.bird_rect.y >= self.bird.height // 2:
                    self.bird.movement = SPEEDFLY
                else:
                    self.bird.movement = 0

    # quite game function
    def quit_game(self):
        self.running = False
        pygame.quit()
        sys.exit()

    # remove the unnecessary pipes
    def remove_pipes(self):
        if self.pipe.pipe_list[2][0].centerx <= self.bird.bird_rect.centerx:
            self.pipe.pipe_list.pop(0)

    # check if the bird hit the pipe or not
    def is_hit_pipes(self):
        if self.bird.bird_rect.colliderect(self.pipe.pipe_list[0][0]) or self.bird.bird_rect.colliderect(self.pipe.pipe_list[0][1]):
            if not self.hit_pipe:
                self.hit_sound.play()
                self.hit_pipe = True
                self.started_game = False
                self.ended_game = True

    # self.quit_game()
    # check if the bird is fall down or not
    def is_fall_down(self):
        if self.bird.bird_rect.y > screen_height - 50 - self.bird.bird_rect.height:
            self.hit_sound.play()
            self.started_game = False
            self.ended_game = True
            self.clear()

    # clear all the properties of this class
    def clear(self):
        cls = self.__class__
        new_instance = cls.__new__(cls)
        cls.__init__(new_instance)
        self.__dict__ = new_instance.__dict__
        self.start_button.text = "RESTART"

    # run the game
    def run(self):
        self.running = True
        while self.running:
            for event in pygame.event.get():
                # quit game
                if event.type == pygame.QUIT:
                    self.quit_game()
                # if game is started, the bird will fly
                if self.started_game:
                    self.bird_animation(event)
                if event.type == swap_pipe:
                    pygame.time.set_timer(swap_pipe, NEW_PIPE_TIME)
                    if self.started_game:
                        # if the bird is flown, create new pipes, else do nothing
                        if self.bird.is_flew:
                            self.pipe.create_pipe()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # check if hover the start button
                    if self.start_button.is_over(pygame.mouse.get_pos()):
                        # reset all the properties and restart game
                        self.clear()
                        self.started_game = True
                if event.type == pygame.MOUSEMOTION:
                    if self.start_button.is_over(pygame.mouse.get_pos()):
                        pygame.mouse.set_cursor(HAND_CURSOR)

            screen.blit(background, (0, -50))
            self.floor.draw()
            if not self.started_game:
                self.start_button.draw()
                pygame.display.flip()
                pygame.display.update()
            else:
                self.pipe.draw_pipe()
                self.pipe.pipe_list = self.pipe.move_pipe()
                self.floor.x -= FPS
                if len(self.pipe.pipe_list) >= MAX_LENGTH_OF_PIPES_LIST:
                    self.remove_pipes()
                    self.is_hit_pipes()
                self.increase_score()

                if self.floor.x < -screen_width: self.floor.x = 0

                self.score.draw(screen)
                self.bird.draw_bird()
                self.bird.fly()

                self.is_fall_down()
                self.floor.draw()
                pygame.display.flip()
                pygame.display.update()
                clock.tick(60)

if __name__ == "__main__":
    game = Game()
    game.run()
