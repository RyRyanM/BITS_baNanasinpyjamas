import sys, pygame
from background import Background
from pipes_all import Pipes
from slime_sprite import Slime
from scoring import Score
from sounds import Sounds
from ginger import Ginger
class Game: 

    def __init__(self):
        self.game_active = False
        self.sounds = Sounds()
        self.background = Background()
        self.slime = Slime()
        self.pipes = Pipes()
        self.scores = Score()
        self.ginger = Ginger()
        self.game_over = pygame.image.load("minigame-1/assets/sprites/joyaki.png").convert_alpha()
        self.game_over = pygame.transform.scale(self.game_over, (300, 100))
        self.get_ready = pygame.image.load("minigame-1/assets/sprites/get-ready.png").convert_alpha()
        self.get_ready = pygame.transform.scale(self.get_ready, (250, 75))
        self.game_over_rect = self.game_over.get_rect(center = (512, 300))
        self.get_ready_rect = self.get_ready.get_rect(center = (512, 500))

    def check_collision(self, ps):
        if self.slime.slime_rect.bottom >= 600 or self.slime.slime_rect.top <= 0:
            self.sounds.play_collision_sound()
            return False
        
        for p in ps: 
            if self.slime.slime_rect.colliderect(p):
                self.sounds.play_collision_sound()
                return False

        return True

    def collect_ginger(self, gingers):
        for ginger in gingers:
            if self.slime.slime_rect.colliderect(ginger):
                self.sounds.play_score_sound()
                self.scores.score += .5
                self.ginger.ginger_list.remove(ginger)
                return True

    def draw_background(self):
        self.background.screen.blit(self.background.bg, (self.background.background_x_position, 0))
        self.background.screen.blit(self.background.bg, (self.background.background_x_position + 1024, 0))

    def game_loop(self):
        while True: 
            

            for event in pygame.event.get(): #captures all the events
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN: 
                    if event.key == pygame.K_SPACE and self.game_active:
                        self.slime.slime_movement = -5
                        self.sounds.play_flap_sound()
                    if event.key == pygame.K_SPACE and self.game_active == False:
                        self.game_active = True
                        self.pipes.pipe_list.clear()
                        self.ginger.ginger_list.clear()
                        self.slime.slime_rect.center = (150, 250)
                        self.slime.slime_movement = 0
                        self.scores.score = 0
                if event.type == self.pipes.SPAWNPIPE:
                    self.pipes.pipe_list.extend(self.pipes.create_pipe())
                if event.type == self.slime.SLIMECHANGE:
                    if self.slime.frame_index < 1:
                        self.slime.frame_index += 1
                    else:
                        self.slime.frame_index = 0
                    self.slime.slime_current, self.slime.slime_rect = self.slime.bird_animation()
                if event.type == self.ginger.SPAWNGINGER:
                    self.ginger.ginger_list.extend(self.ginger.spawn_ginger())

            self.background.background_x_position -= .3
            self.draw_background()
            if self.background.background_x_position <= -1024:
                self.background.background_x_position = 0
            

            if self.game_active:
                #bird
                self.slime.slime_movement += self.slime.gravity
                rotated_bird = self.slime.rotate_bird(self.slime.slime_current)
                self.slime.slime_rect.centery += self.slime.slime_movement #move the bird rectangle down
                self.background.screen.blit(rotated_bird, self.slime.slime_rect)
                self.game_active = self.check_collision(self.pipes.pipe_list)

                #pipe
                self.pipes.pipe_list = self.pipes.move_pipes(self.pipes.pipe_list)
                self.pipes.draw_pipes(self.pipes.pipe_list)

                self.ginger.ginger_list = self.ginger.move_ginger(self.ginger.ginger_list)
                self.ginger.draw_ginger(self.ginger.ginger_list)

                self.collect_ginger(self.ginger.ginger_list)

                if self.scores.score > self.scores.high_score: self.scores.high_score = self.scores.score
                self.scores.score_display("main_game")
            else: 
                self.background.screen.blit(self.game_over, self.game_over_rect)
                self.background.screen.blit(self.get_ready, self.get_ready_rect)
                self.scores.score_display("game_over")

            #floor
            self.background.floor_x_position -= 1 #floor moving to the right
            self.background.draw_floor()
            if self.background.floor_x_position <= -1024:
                self.background.floor_x_position = 0

            pygame.display.update() #draws everything before this line
            if self.scores.score >= 30:
                break
            self.background.clock.tick(120) #120 FPS
            