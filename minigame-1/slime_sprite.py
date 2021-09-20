import pygame

class Slime:
    def __init__(self):
        pygame.init()
        self.slime_flat = pygame.image.load("assets/sprites/slime_flat.PNG").convert_alpha()
        self.slime_flat = pygame.transform.scale(self.slime_flat, (90, 50))
        self.slime_high = pygame.image.load("assets/sprites/slime_high.PNG").convert_alpha()
        self.slime_high = pygame.transform.scale(self.slime_high, (90, 50))
        self.slime_frames = [self.slime_flat, self.slime_high] #create animation 
        self.frame_index = 0
        self.slime_current = self.slime_frames[self.frame_index]
        self.slime_rect = self.slime_current.get_rect(center = (150, 250)) #create a rectangle around the bird
        self.gravity = 0.2
        self.slime_movement = 0
        self.SLIMECHANGE = pygame.USEREVENT + 1
        pygame.time.set_timer(self.SLIMECHANGE, 400)


    def rotate_bird(self, slime):
        new_slime = pygame.transform.rotozoom(slime, -self.slime_movement * 4, 1)
        return new_slime

    def bird_animation(self):
        new_slime = self.slime_frames[self.frame_index]
        new_slime_rect = new_slime.get_rect(center = (150, self.slime_rect.centery))
        return (new_slime, new_slime_rect)

    