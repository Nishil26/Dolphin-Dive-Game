import pygame
import random
import sys
import os

pygame.init()
print(os.getcwd())
# High Score
HIGH_SCORE_FILE = "highscore.txt"

if os.path.exists(HIGH_SCORE_FILE):
    with open(HIGH_SCORE_FILE, "r") as f:
        high_score = int(f.read())
else:
    high_score = 0

# Window Settings
WIDTH, HEIGHT = 600, 400

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dolphin Dive")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

# Dolphin Sprite
dolphin_x = 100
dolphin_y = HEIGHT // 2

# Colors
BLUE = 0, 0, 255
CYAN = 0, 255, 255
BLACK = 0, 0, 0
MAGENTA = 255, 0, 255
WHITE = 255, 255, 255

# Game Physics
dolphin_velocity = 0
gravity = 0.5

# Coral
corals = []
for i in range(3):
    corals.append({
        "x": WIDTH + i * 250,
        "top_height": random.randint(50,180),
        "passed": False
    })

# Game State
game_state = "start" # start, playing, game_over

# Game Variables
speed = 3
speed_increase_timer = 0
gap = 150
score = 0
running = True

# Game Loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if game_state == "start":
                game_state = "playing"

            elif game_state == "game_over":
                # Reset Game
                dolphin_x = 100
                dolphin_y = HEIGHT // 2
                dolphin_velocity = 0
                score = 0
                speed = 3
                speed_increase_timer = 0

                if score > high_score:
                    high_score = score
                    with open(HIGH_SCORE_FILE, "w") as f:
                        f.write(str(high_score))

                corals.clear()
                for i in range(3):
                    corals.append({
                        "x": WIDTH + i * 250,
                        "top_height": random.randint(50,180),
                        "passed": False
                        })
                
                game_state = "playing"

            elif game_state == "playing":
                dolphin_velocity = -10
    
    if game_state == "playing":
        dolphin_velocity += gravity
        dolphin_y += dolphin_velocity

        for coral in corals:
            coral["x"] -= speed

            if coral["x"] < -150:  # Determines where it begins to recycle
                rightmost = max(c["x"] for c in corals)
                coral["x"] = rightmost + 250
                coral["top_height"] = random.randint(50, 180)
                coral["passed"] = False
            if not coral["passed"] and coral["x"] + 70 < dolphin_x:
                coral["passed"] = True
                score += 1
        
        speed_increase_timer += 1

        # Every 5 seconds (300 frames at 60 FPS)
        if speed_increase_timer >= 300:
            speed += 0.5
            speed_increase_timer = 0
    
    dolphin_rect = pygame.Rect(dolphin_x - 20, dolphin_y - 20, 40, 40)

    # Checking Collisions
    if game_state == "playing":
        if dolphin_y - 20 <= 0 or dolphin_y + 20 >= HEIGHT:
            game_state = "game_over"
        
        for coral in corals:
            bottom_y = coral["top_height"] + gap

            top_coral = pygame.Rect(coral["x"], 0, 70, coral["top_height"])
            bottom_coral = pygame.Rect(coral["x"], bottom_y, 70, HEIGHT - bottom_y)

            if dolphin_rect.colliderect(top_coral) or dolphin_rect.colliderect(bottom_coral):
                game_state = "game_over"

    screen.fill((BLUE))

    # Drawing Start Screen
    if game_state == "start":
        title = font.render("Dolphin Dive", True, WHITE)
        prompt = font.render("Press SPACE to Start", True, WHITE)
        screen.blit(title, (220, 140))
        screen.blit(prompt, (180, 200))

    # Drawing Dolphin
    pygame.draw.circle(screen, CYAN, (int(dolphin_x), int(dolphin_y)), 20)

    # Drawing Corals
    for coral in corals:
        bottom_y = coral["top_height"] + gap
        pygame.draw.rect(screen, MAGENTA, (coral["x"], 0, 70, coral["top_height"]))
        pygame.draw.rect(screen, MAGENTA, (coral["x"], bottom_y, 70, HEIGHT - bottom_y))
    
    # Drawing Score
    if game_state == "playing":
        score_text = font.render (f"Score: {score}", True, WHITE)
        screen.blit (score_text, (10, 10))
    
    # Drawing Game Over Screen
    if game_state == "game_over":
        game_over_text = font.render("GAME OVER", True, WHITE)
        screen.blit(game_over_text, (225, 150))
        score_text = font.render (f"Score: {score}", True, WHITE)
        screen.blit (score_text, (200, 190))
        high_score_text = font.render (f"High Score: {high_score}", True, WHITE)
        screen.blit (high_score_text, (300, 190))
        restart_text = font.render("Press SPACE to Restart", True, WHITE)
        screen.blit(restart_text, (156, 230))
        
    pygame.display.flip()
    clock.tick (60)

pygame.quit()
sys.exit()










#Point System




#Game Over / Restart


