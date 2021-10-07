import pygame, random
from background import Background

class Ginger:
    def __init__(self):
        self.ginger_surface = pygame.image.load("minigame-1/assets/sprites/ginger.png").convert_alpha()
        self.ginger_surface = pygame.transform.scale(self.ginger_surface, (50, 50))
        self.ginger_list = []
        self.SPAWNGINGER = pygame.USEREVENT + 2
        pygame.time.set_timer(self.SPAWNGINGER, 1000)
        self.ginger_location = [150, 200, 250, 350, 400, 450, 500]
        self.screen = Background().screen

    def spawn_ginger(self):
        random_ginger_location = random.choice(self.ginger_location)
        ginger_rect = self.ginger_surface.get_rect(center = (1024, random_ginger_location))
        return ginger_rect, ginger_rect

    def move_ginger(self, gingers):
        for ginger in gingers:
            ginger.centerx -= 1.5
        return gingers

    def draw_ginger(self, gingers):
        for ginger in gingers:
            self.screen.blit(self.ginger_surface, ginger)
