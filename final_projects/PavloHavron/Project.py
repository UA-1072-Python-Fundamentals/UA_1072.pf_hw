import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Simple Game")

# Set up colors
white = (255, 255, 255)
red = (255, 0, 0)

# Set up player
player_size = 50
player_x = width // 2 - player_size // 2
player_y = height - 2 * player_size
player_speed = 5

# Set up obstacles
obstacle_size = 50
obstacle_speed = 8
obstacle_frequency = 15
obstacles = []

# Set up font
font = pygame.font.Font(None, 36)

# Game loop
clock = pygame.time.Clock()
score = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < width - player_size:
        player_x += player_speed

    # Spawn obstacles
    if random.randint(1, obstacle_frequency) == 1:
        obstacle_x = random.randint(0, width - obstacle_size)
        obstacle_y = -obstacle_size
        obstacles.append([obstacle_x, obstacle_y])

    # Move obstacles
    for obstacle in obstacles:
        obstacle[1] += obstacle_speed

    # Check for collisions
    for obstacle in obstacles:
        if (
            player_x < obstacle[0] < player_x + player_size
            and player_y < obstacle[1] < player_y + player_size
        ):
            pygame.quit()
            sys.exit()

    # Remove off-screen obstacles
    obstacles = [obstacle for obstacle in obstacles if obstacle[1] < height]

    # Draw background
    screen.fill((0, 50, 255))

    # Draw player
    pygame.draw.rect(screen, white, [player_x, player_y, player_size, player_size])

    # Draw obstacles
    for obstacle in obstacles:
        pygame.draw.rect(screen, red, [obstacle[0], obstacle[1], obstacle_size, obstacle_size])

    # Display score
    score_text = font.render(f"Score: {score}", True, white)
    screen.blit(score_text, (10, 10))

    # Update display
    pygame.display.flip()

    # Frame rate
    clock.tick(90)

    # Increase score
    score += 1