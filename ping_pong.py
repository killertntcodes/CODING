import pygame

def main():
    pygame.init()

    screen_width, screen_height = 900, 800
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('ping pong')

    x, y = 30, 30
    sprite_width, sprite_height = 100, 30

    sprite2_width, sprite2_height = 100, 30
    x2 = screen_width - sprite2_width
    y2 = screen_height - sprite2_height - 30

    ball_x, ball_y = screen_width // 2, screen_height // 2
    ball_radius = 10
    ball_dx, ball_dy = 5, 5

    font = pygame.font.SysFont(None, 72)
    game_over = False

    clock = pygame.time.Clock()
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]:
            x -= 9
        if pressed[pygame.K_RIGHT]:
            x += 9

        if pressed[pygame.K_a]:
            x2 -= 9
        if pressed[pygame.K_d]:
            x2 += 9

        x = max(0, min(screen_width - sprite_width, x))
        x2 = max(0, min(screen_width - sprite2_width, x2))

        if not game_over:
            ball_x += ball_dx
            ball_y += ball_dy

        if ball_x - ball_radius <= 0 or ball_x + ball_radius >= screen_width:
            ball_dx *= -1

        if ball_y - ball_radius <= 0 or ball_y + ball_radius >= screen_height:
            ball_dx = 0
            ball_dy = 0
            game_over = True

        if (x < ball_x < x + sprite_width and
            y < ball_y < y + sprite_height):
            ball_dy *= -1

        if (x2 < ball_x < x2 + sprite2_width and
            y2 < ball_y < y2 + sprite2_height):
            ball_dy *= -1

        screen.fill((0, 0, 0))

        pygame.draw.rect(screen, (255, 255, 255),
                         (x, y, sprite_width, sprite_height))

        pygame.draw.rect(screen, (255, 255, 255),
                         (x2, y2, sprite2_width, sprite2_height))

        pygame.draw.circle(screen, (255, 0, 0),
                           (ball_x, ball_y), ball_radius)

        #lives

        if game_over:
            text_str = "Game Over"
            text = font.render(text_str, True, (255, 0, 0))

            text_x = screen_width // 2 - text.get_width() // 2
            text_y = screen_height // 2 - text.get_height() // 2

            screen.blit(text, (text_x, text_y))

            o_index = 5

            char_width = text.get_width() / len(text_str)

            ball_x = int(text_x + o_index * char_width + char_width / 2)
            ball_y = int(text_y + text.get_height() / 2)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()