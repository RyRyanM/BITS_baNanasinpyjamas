import pygame

class Sounds: 
    def __init__(self):
        pygame.mixer.init()
        self.button_sound = pygame.mixer.Sound("assets/sounds/flap_wing.wav")
        self.death_sound = pygame.mixer.Sound("assets/sounds/flap_die.wav")
        self.point_sound = pygame.mixer.Sound("assets/sounds/flap_point.wav")
        self.point_sound_countdown = 1000

    def play_flap_sound(self):
        self.button_sound.play()

    def play_collision_sound(self):
        self.death_sound.play()

    def play_score_sound(self):
        self.point_sound.play()
        self.point_sound_countdown = 1000