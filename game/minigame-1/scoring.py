import pygame
import background

class Score:
    def __init__(self):
        self.screen = background.Background().screen
        self.score = 0
        self.high_score = 0
        self.game_font = pygame.font.Font("minigame-1/04B_19.TTF", 40)
        

    def score_display(self, game_state):
        if game_state == "main_game":
            score_surface = self.game_font.render("red ginger collected: " + str(int(self.score)), True, (30, 30, 30))
            score_rect = score_surface.get_rect(topleft = (50, 50))
            self.screen.blit(score_surface, score_rect)

        if game_state == "game_over":
            score_surface = self.game_font.render("collected: " + str(int(self.score)), True, (30, 30, 30))
            score_rect = score_surface.get_rect(center = (512, 150))
            self.screen.blit(score_surface, score_rect)

            highscore_surface = self.game_font.render("high score: " + str(int(self.high_score)), True, (30, 30, 30))
            highscore_rect = score_surface.get_rect(center = (512, 200))
            self.screen.blit(highscore_surface, highscore_rect)

            instruction_surface = self.game_font.render("""Collect 30 red gingers to get the flavor!""", True, (30, 30, 30))
            instruction_rect = instruction_surface.get_rect(center = (512, 390))
            self.screen.blit(instruction_surface, instruction_rect)

            control_surface = self.game_font.render("""Press SPACE BAR to fly!""", True, (30, 30, 30))
            control_rect = control_surface.get_rect(center = (512, 440))
            self.screen.blit(control_surface, control_rect)



