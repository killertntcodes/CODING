import pygame
import random
screen_width, screen_height = 500, 400
movement_speed = 5
font_size = 72
pygame.init()
bg=pygame.transform.scale(pygame.image.load("bg.png"), (screen_width, screen_height))
font = pygame.font.SysFont('times new roman', font_size)
class Sprite(pygame.sprite.Sprite):
    def __init__(self, width, height, color):
        super().__init__()
        self.image= pygame.Surface((width, height))
        self.image.fill(pygame.Color("dodgerblue"))
        pygame.draw.rect(self.image, color, (0, 0, width, height))
        self.rect = self.image.get_rect()
    def move(self, xchange, ychange):
        self.rect.x = max(0, min(screen_width - self.rect.width, self.rect.x + xchange))
        self.rect.y = max(0, min(screen_height - self.rect.height, self.rect.y + ychange))
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Sprite collision')
all_sprites = pygame.sprite.Group()
sprite1 = Sprite(30, 20, pygame.Color("black"))
sprite1.rect.x, sprite1.rect.y = random.randint(0, screen_width - sprite1.rect.width), random.randint(0, screen_height - sprite1.rect.height)
sprite2 = Sprite(30, 20, pygame.Color("red"))
sprite2.rect.x, sprite2.rect.y = random.randint(0, screen_width - sprite2.rect.width), random.randint(0, screen_height - sprite2.rect.height)
all_sprites.add(sprite1)
running, won = True, False
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False
    if not won:
        keys = pygame.key.get_pressed()
        xchange = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * movement_speed
        ychange = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * movement_speed
        sprite1.move(xchange, ychange)

        if sprite1.rect.colliderect(sprite2.rect):
            all_sprites.remove(sprite2)
            won = True
    screen.blit(bg, (0, 0))
    all_sprites.draw(screen)

    if won:
        text = font.render("You win!", True, pygame.Color("black"))
        text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))
        screen.blit(text, text_rect)
    pygame.display.flip()
    clock.tick(90)
pygame.quit()