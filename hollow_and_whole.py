import pygame
pygame.init()
window = pygame.display.set_mode((400, 400))
window.fill((255, 255, 255))
green = (200, 200, 200)
pygame.draw.circle(window, green, (300, 300), 50)
pygame.draw.circle(window,green, (100, 100),50, 3)
runnin = True
while runnin:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runnin = False
    pygame.display.flip()
pygame.quit()