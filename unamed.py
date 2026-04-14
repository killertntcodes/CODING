import pygame
import random

def main():
    pygame.init()

    bg_color = pygame.Color('black')

    # Screen setup
    screen_width, screen_height = 950, 700
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("DVD Bounce")

    # Colors
    colors = [
        pygame.Color('red'),
        pygame.Color('green'),
        pygame.Color('blue'),
        pygame.Color('yellow'),
        pygame.Color('white')
    ]
    current_color = random.choice(colors)

    colors2 = [
        pygame.Color('cyan'),
        pygame.Color('magenta'),
        pygame.Color('orange'),
        pygame.Color('purple'),
        pygame.Color('pink')
    ]

    x, y = 30, 30
    sprite_width, sprite_height = 60, 60    

    dx, dy = 4, 4

    clock = pygame.time.Clock()
    running = True

    pygame.event.post(pygame.event.Event(pygame.USEREVENT + 1))


    while running:
        # Quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        x += dx
        y += dy

        if x <= 0 or x >= screen_width - sprite_width:
            dx *= -1
            current_color = random.choice(colors)
            bg_color = random.choice(colors2)
        

        if y <= 0 or y >= screen_height - sprite_height:
            dy *= -1
            current_color = random.choice(colors)
            bg_color = random.choice(colors2)
            

        screen.fill(bg_color)
        pygame.draw.rect(screen, current_color, (x, y, sprite_width, sprite_height))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()