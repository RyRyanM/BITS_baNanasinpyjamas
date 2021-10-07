import pygame, random
from background import Background

class Pipes:
    def __init__(self):
        self.pipe = pygame.image.load("minigame-1/assets/sprites/knife.png").convert_alpha()
        self.pipe = pygame.transform.scale(self.pipe, (50, 350))
        self.pipe_list = [] #throw in a lot of rectangles
        self.SPAWNPIPE = pygame.USEREVENT
        pygame.time.set_timer(self.SPAWNPIPE, 1000)
        self.pipe_height = [300, 350, 400, 450, 500, 550]
        self.screen = Background().screen

    def create_pipe(self):
        random_pipe_position = random.choice(self.pipe_height)
        bottom_pipe = self.pipe.get_rect(midtop = (1024, random_pipe_position))
        top_pipe = self.pipe.get_rect(midbottom = (1024, random_pipe_position - 250))
        return bottom_pipe, top_pipe

    def move_pipes(self, pipes):
        for p in pipes:
            p.centerx -= 2.5
        return pipes

    def draw_pipes(self, pipes):
        for p in pipes:
            if p.bottom >= 600:
                self.screen.blit(self.pipe, p)
            else: 
                flip_pipe = pygame.transform.flip(self.pipe, False, True)
                self.screen.blit(flip_pipe, p)