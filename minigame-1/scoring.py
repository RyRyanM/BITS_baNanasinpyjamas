import pygame
import background

class Score:
    def __init__(self):
        self.screen = background.Background().screen
        self.score = 0
        self.high_score = 0
        self.game_font = pygame.font.Font("minigame-1/04B_19.ttf", 30)

    def score_display(self, game_state):
        if game_state == "main_game":
            score_surface = self.game_font.render(str(int(self.score)), True, (255, 255, 255))
            score_rect = score_surface.get_rect(center = (512, 150))
            self.screen.blit(score_surface, score_rect)

        if game_state == "game_over":
            score_surface = self.game_font.render(str(int(self.score)), True, (255, 255, 255))
            score_rect = score_surface.get_rect(center = (512, 150))
            self.screen.blit(score_surface, score_rect)

            highscore_surface = self.game_font.render("high score: " + str(int(self.high_score)), True, (255, 255, 255))
            highscore_rect = score_surface.get_rect(center = (412, 200))
            self.screen.blit(highscore_surface, highscore_rect)
