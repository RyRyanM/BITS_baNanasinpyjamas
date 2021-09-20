import pygame

class Background:
    def __init__(self):
        #This line will create a screeen (width,height)
        self.screen = pygame.display.set_mode((1024,768))
        #Clock is to define FPS
        self.clock = pygame.time.Clock()
        #Converting the image and make it as the game background
        self.bg = pygame.image.load("assets/sprites/a1Background.png").convert()
        #Size Doubling
        self.bg = pygame.transform.scale(self.bg, (1024,650))
        #Converting the image and make it as floor inside the game
        self.floor = pygame.image.load("assets/sprites/floor.png").convert()
        #Changing the scale of the floor image
        self.floor = pygame.transform.scale(self.floor, (1024, 300))
        #Set the floor position static
        self.floor_x_position = 0
        self.background_x_position = 0

    def draw_floor(self):
        self.screen.blit(self.floor, (self.floor_x_position, 650))
        #New floor outside the screen on the right (as the object goes by)
        self.screen.blit(self.floor, (self.floor_x_position + 1024, 650))
