import pygame

pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("My First Pygame Window")

clock = pygame.time.Clock()
running = True

x = 300
y = 200

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((30, 30, 30))

    pygame.draw.circle(screen, (0, 200, 255), (x, y), 40)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()