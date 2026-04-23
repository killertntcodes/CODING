import math
import random
import pygame
screen_width = 800
screen_height = 600
player_start_x = 370
player_start_y = 480
enemy_start_x = 50
enemy_start_y = 150
enemy_speed_x = 4
enemy_speed_y = 40
bullet_speed_y = 10
collision_distance = 27
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
background = pygame.image.load("background SPACE INVADERS.jpg")
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("sprite.png")
pygame.display.set_icon(icon)
player_img = pygame.image.load("ship sprite.png")
player_x = player_start_x
player_y = player_start_y
playerx_change=0
enemyImg = []
enemyx = []
enemyy = []
enemyx_change = []
enemyy_change = []
enemies = 6
for i in range(enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    47
    enemyx.append(random.randint(0, screen_width - 64))
    enemyy.append(random.randint(enemy_speed_y_min, enemy_start_x_max))
    enemyx_change.append(enemy_speed_x)
    enemyy_change.append(enemy_speed_y)

bulletIMG = pygame.image.load('bullet.png')
bulletx= 0
bullety= player_start_y
bulletx_change = 0
bullety_change = bullet_speed_y
bullet_state = "ready"

score_val= 0
font = pygame.font.Font('freesansbold.ttf', 32)
textx= 10
texty = 10

over_font= pygame.font.Font('freesansbold.ttf', 64)

def show_score(x,y):
    score=font.render("score: " + str(score_val), True , (255, 255,255))
    screen.blit(score, (x,y))

def game_ovr_txt():
    over_text = over_font.render("GAME OVER", True , (255,255,255))
    screen.blit(over_text, (200, 250))

def player(x,y):
    screen.blit(player_img, (x,y))
def enemy(x,y,i):
    screen.blit(enemyImg[i], (x,y))
def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletIMG, (x + 16, y + 10))
def isCollision(enemyx, enemyy, bulletx, bullety):
    distance= math.sqrt((enemyx - bulletx)**2 + (enemyy - bullety)**2) #speed formula
    return distance < collision_distance

running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerx_change = -5
            if event.key == pygame.K_RIGHT:
                playerx_change = 5
            if event.key == pygame.K_SPACE and bullet_state is "ready":
                bulletx = player_x
                fire_bullet(bulletx, bullety)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerx_change = 0
    player_x += playerx_change
    player_x = max(0, min(player_x, screen_width - 64))

    for i in range(enemies):