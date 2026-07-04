import pygame
import random

pygame.init()

# Window settings
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

# Colors
BLACK = (20, 20, 20)
GREEN = (0, 200, 0)
RED = (220, 50, 50)
WHITE = (240, 240, 240)

def draw_text(text, x, y):
    img = font.render(text, True, WHITE)
    screen.blit(img, (x, y))

def random_food():
    x = random.randrange(0, WIDTH, CELL_SIZE)
    y = random.randrange(0, HEIGHT, CELL_SIZE)
    return [x, y]

snake = [[100, 100], [80, 100], [60, 100]]
direction = "RIGHT"
next_direction = "RIGHT"

food = random_food()
score = 0
running = True
game_over = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "DOWN":
                next_direction = "UP"
            elif event.key == pygame.K_DOWN and direction != "UP":
                next_direction = "DOWN"
            elif event.key == pygame.K_LEFT and direction != "RIGHT":
                next_direction = "LEFT"
            elif event.key == pygame.K_RIGHT and direction != "LEFT":
                next_direction = "RIGHT"

            if game_over and event.key == pygame.K_SPACE:
                snake = [[100, 100], [80, 100], [60, 100]]
                direction = "RIGHT"
                next_direction = "RIGHT"
                food = random_food()
                score = 0
                game_over = False

    if not game_over:
        direction = next_direction

        head = snake[0].copy()

        if direction == "UP":
            head[1] -= CELL_SIZE
        elif direction == "DOWN":
            head[1] += CELL_SIZE
        elif direction == "LEFT":
            head[0] -= CELL_SIZE
        elif direction == "RIGHT":
            head[0] += CELL_SIZE

        snake.insert(0, head)

        if head == food:
            score += 1
            food = random_food()
        else:
            snake.pop()

        # Check wall collision
        if (
            head[0] < 0 or head[0] >= WIDTH or
            head[1] < 0 or head[1] >= HEIGHT
        ):
            game_over = True

        # Check self collision
        if head in snake[1:]:
            game_over = True

    screen.fill(BLACK)

    pygame.draw.rect(screen, RED, (food[0], food[1], CELL_SIZE, CELL_SIZE))

    for part in snake:
        pygame.draw.rect(screen, GREEN, (part[0], part[1], CELL_SIZE, CELL_SIZE))

    draw_text(f"Score: {score}", 10, 10)

    if game_over:
        draw_text("Game Over!", 220, 160)
        draw_text("Press SPACE to restart", 150, 200)

    pygame.display.flip()
    clock.tick(10)

pygame.quit()