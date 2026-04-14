import pygame
pygame.init()
screen_width, screen_height = (900, 700)
display_suface= pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Image to Screen")
background_img = pygame.transform.scale(pygame.image.load('bg.png').convert(), (screen_width, screen_height))
def game_loop():
    running=True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
        display_suface.blit(background_img, (0, 0))
        pygame.display.flip()
    pygame.quit()
if __name__ == "__main__":
    game_loop()