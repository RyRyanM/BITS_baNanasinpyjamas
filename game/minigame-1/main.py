import pygame
import os
import random
from game import Game 

# Init and Create Window (win)
pygame.init()
win_height = 800
win_width = 1000
win = pygame.display.set_mode((win_width, win_height))
clock = pygame.time.Clock()

# Load and Size Images
# Hero (Joyaki)
slime_flat = pygame.transform.scale(pygame.image.load(os.path.join("minigame-1/Sprites/Joyaki", "slime_flat.png")), (120, 100))
slime_high = pygame.transform.scale(pygame.image.load(os.path.join("minigame-1/Sprites/Joyaki", "slime_high.png")), (120, 100))

left = [slime_flat,
        slime_high,
        slime_flat,
        slime_high,
        slime_flat,
        slime_high,
        slime_flat,
        slime_high,
        slime_flat,
        slime_high]

right = [slime_high,
         slime_flat,
         slime_high,
         slime_flat,
         slime_high,
         slime_flat,
         slime_high,
         slime_flat,
         slime_high]

# Enemy (Octoboss)
octoboss = pygame.transform.scale(pygame.image.load(os.path.join("minigame-1/Sprites/Boss", "octoboss.png")), (210,210))
octoboss_2 = pygame.transform.scale(pygame.image.load(os.path.join("minigame-1/Sprites/Boss", "octoboss_2.png")), (210,210))

left_enemy = [octoboss_2,
              octoboss,
              octoboss_2,
              octoboss,
              octoboss_2,
              octoboss,
              octoboss_2,
              octoboss,
              octoboss_2]
              
right_enemy = [octoboss,
              octoboss_2,
              octoboss,
              octoboss_2,
              octoboss,
              octoboss_2,
              octoboss,
              octoboss_2,
              octoboss]

hit_enemy = pygame.image.load(os.path.join("minigame-1/Sprites/Boss", "octoboss_hit.png"))
hit_enemy = pygame.transform.scale(hit_enemy, (300, 300))
hit_enemy = [hit_enemy]

# Bullet
bullet_img = pygame.transform.scale(pygame.image.load(os.path.join("minigame-1/Sprites/Bullets", "redGinger.png")), (100, 100))

# Background
background = pygame.transform.scale(pygame.image.load(os.path.join("minigame-1/Sprites", "kitchenBackground.png")), (win_width, win_height))
class Hero:
    def __init__(self, x, y):
        # Walk
        self.x = x
        self.y = y
        self.velx = 12
        self.vely = 12
        self.face_right = True
        self.face_left = False
        self.stepIndex = 0
        # Jump
        self.jump = False
        # Bullet
        self.bullets = []
        self.cool_down_count = 0
        # Health
        self.hitbox = [self.x, self.y, 120, 100]
        self.health = 30
        self.lives = 1
        self.alive = True

    def move_hero(self, userInput):
        if userInput[pygame.K_RIGHT] and self.x <= win_width - 62:
            self.x += self.velx
            self.face_right = True
            self.face_left = False
        elif userInput[pygame.K_LEFT] and self.x >= 0:
            self.x -= self.velx
            self.face_right = False
            self.face_left = True
        else:
            self.stepIndex = 0

    def draw(self, win):
        self.hitbox = (self.x, self.y, 120, 100)
        pygame.draw.rect(win, (255, 0, 0), (self.x, self.y - 20, 120, 10))
        if self.health >= 0:
            pygame.draw.rect(win, (0, 255, 0), (self.x, self.y - 20, self.health*4, 10))
        if self.stepIndex >= 9:
            self.stepIndex = 0
        if self.face_left:
            win.blit(left[self.stepIndex], (self.x, self.y))
            self.stepIndex += 1
        if self.face_right:
            win.blit(right[self.stepIndex], (self.x, self.y))
            self.stepIndex += 1

    def jump_motion(self, userInput):
        if userInput[pygame.K_SPACE] and self.jump is False:
            self.jump = True
        if self.jump:
            self.y -= self.vely*4
            self.vely -= 1
        if self.vely < -12:
            self.jump = False
            self.vely = 12

    def direction(self):
        if self.face_right:
            return 1
        if self.face_left:
            return -1

    def cooldown(self):
        if self.cool_down_count >= 6:
            self.cool_down_count = 0
        elif self.cool_down_count > 0:
            self.cool_down_count += 1

    def shoot(self):
        self.hit()
        self.cooldown()
        if (userInput[pygame.K_f] and self.cool_down_count == 0):
            bullet = Bullet(self.x, self.y, self.direction())
            self.bullets.append(bullet)
            self.cool_down_count = 1
        for bullet in self.bullets:
            bullet.move()
            if bullet.off_screen():
                self.bullets.remove(bullet)

    def hit(self):
        for enemy in enemies:
            for bullet in self.bullets:
                if (bullet.x in range(enemy.hitbox[0], enemy.hitbox[0] + enemy.hitbox[2]) or (bullet.x + 100) in range(enemy.hitbox[0], enemy.hitbox[0] + enemy.hitbox[2])) and (bullet.y in range(enemy.hitbox[1], enemy.hitbox[1] + enemy.hitbox[3]) or (bullet.y + 100) in range(enemy.hitbox[1], enemy.hitbox[1] + enemy.hitbox[3])):
                    enemy.health -= 3
                    player.bullets.remove(bullet)


class Bullet:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

    def draw_bullet(self):
        win.blit(bullet_img, (self.x, self.y))

    def move(self):
        if self.direction == 1:
            self.x += 15
        if self.direction == -1:
            self.x -= 15

    def off_screen(self):
        return not(self.x >= 0 and self.x <= win_width)


class Enemy:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.stepIndex = 0
        # Health
        self.hitbox = [self.x, self.y, 210, 210]
        self.health = 30

    def step(self):
        if self.stepIndex >= 9:
            self.stepIndex = 0

    def draw(self, win):
        self.hitbox = (self.x, self.y, 210, 210)
        pygame.draw.rect(win, (255, 0, 0), (self.x, self.y - 20, 210, 10))
        if self.health >= 0:
            pygame.draw.rect(win, (0, 255, 0), (self.x, self.y - 20, self.health*7, 10))
        self.step()
        if self.direction == left:
            win.blit(left_enemy[self.stepIndex//3], (self.x, self.y))
        if self.direction == right:
            win.blit(right_enemy[self.stepIndex//3], (self.x, self.y))
        self.stepIndex += 1

    def move(self):
        self.hit()
        if self.direction == left:
            self.x -= 7
        if self.direction == right:
            self.x += 7

    def hit(self):
        if player.hitbox[0] < enemy.x < player.hitbox[0] + player.hitbox[2] or player.hitbox[0] < enemy.x + 210 < player.hitbox[0] + player.hitbox[2] and player.hitbox[1] < enemy.y <player.hitbox[1] + player.hitbox[3] or player.hitbox[1] < enemy.y + 210 <player.hitbox[1] + player.hitbox[3]:
            if player.health >0:
                player.health -= 1
                if player.health == 0 and player.lives > 0:
                    player.lives -= 1
                    player.health = 30
                elif player.health == 0 and player.lives == 0:
                    player.alive = False

    def off_screen(self):
        return not(self.x >= -50 and self.x <= win_width + 50)


# Draw Game
def draw_game():
    win.fill((0, 0, 0))
    win.blit(background, (0,0))
    # Draw Player
    player.draw(win)
    # Draw Bullets
    for bullet in player.bullets:
        bullet.draw_bullet()
    # Draw Enemies
    for enemy in enemies:
        enemy.draw(win)
    # Player Health
    if player.alive == False:
        win.fill((0,0,0))
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render('You Died! Press R to restart', True, (255, 255, 255))
        textRect = text.get_rect()
        textRect.center = (win_width//2, win_height//2)
        win.blit(text, textRect)
        if userInput[pygame.K_r]:
            player.alive = True
            player.lives = 1
            player.health = 30

    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render('Lives: '+ str(player.lives), True, (0,0,0))
    win.blit(text, (650, 20))
    # Delay and Update
    pygame.time.delay(100)
    pygame.display.update()

# Instance of Hero-Class
player = Hero(250, 600)

# Instance of Enemy-Class
enemies = []

# Mainloop
run = False
game = Game()
game.game_loop()
if game.scores.score >= 30:
    run = True
while run:

    # Quit Game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Input
    userInput = pygame.key.get_pressed()

    # Shoot
    player.shoot()

    # Movement
    player.move_hero(userInput)
    player.jump_motion(userInput)

    # Enemy
    if len(enemies) == 0:
        rand_nr = random.randint(0,1)
        if rand_nr == 1:
            enemy = Enemy(750, 500, left)
            enemies.append(enemy)
        if rand_nr == 0:
            enemy = Enemy(50, 500, right)
            enemies.append(enemy)
    for enemy in enemies:
        enemy.move()
        if enemy.off_screen():
            enemies.remove(enemy)

    # Draw Game in Window
    draw_game()