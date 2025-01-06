import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Screen setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple Pygame Project")

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Player setup
player_size = 50
player_x = SCREEN_WIDTH // 2 - player_size // 2
player_y = SCREEN_HEIGHT // 2 - player_size // 2
player_speed = 5

# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Key handling
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= player_speed
    if keys[pygame.K_DOWN] and player_y < SCREEN_HEIGHT - player_size:
        player_y += player_speed
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - player_size:
        player_x += player_speed

    # Drawing everything
    screen.fill(WHITE)  # Clear screen with white color
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_size, player_size))  # Draw player

    pygame.display.flip()  # Update the display

    clock.tick(30)  # Limit frame rate to 30 FPS

# Quit Pygame
pygame.quit()
sys.exit()
