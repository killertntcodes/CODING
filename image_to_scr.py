import pygame
pygame.init()
screen_width, screen_height = (500, 500)
display_suface= pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Image to Screen")
background_img = pygame.transform.scale(pygame.image.load('JUICE WRRRLD.jpg').convert(), (screen_width, screen_height))
penguin_img = pygame.transform.scale(pygame.image.load('new pfp juice and x.png').convert_alpha(), (200, 200))
penguin_rect = penguin_img.get_rect(center=(screen_width//2, screen_height//2-30))
text = pygame.font.Font(None, 36).render('Hello, World!', True, pygame.Color('black'))
text_rect=text.get_rect(center=(screen_width//2, screen_height//2 + 110))
def game_loop():
    clock = pygame.time.Clock()
    running=True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
        display_suface.blit(background_img, (0, 0))
        display_suface.blit(penguin_img, penguin_rect)
        display_suface.blit(text, text_rect)
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()
if __name__ == "__main__":
    game_loop()