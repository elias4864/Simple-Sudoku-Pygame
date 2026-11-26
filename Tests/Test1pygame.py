import pygame

# 1. Initialize Pygame
pygame.init()

# 2. Set up the display window
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My First Pygame")

# Set up a clock to control the frame rate (FPS)
clock = pygame.time.Clock()

# Player properties (x, y, width, height)
player = pygame.Rect(375, 275, 50, 50)
player_speed = 5

# 3. Main Game Loop
running = True
while running:
    # A. Process Player Inputs (Events)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Continuous key presses for smooth movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= player_speed
    if keys[pygame.K_RIGHT]:
        player.x += player_speed
    if keys[pygame.K_UP]:
        player.y -= player_speed
    if keys[pygame.K_DOWN]:
        player.y += player_speed

    # B. Render Graphics
    screen.fill((30, 30, 30))  # Fill background with dark gray (RGB)
    pygame.draw.rect(screen, (220, 50, 50), player)  # Draw the red player

    # Update the display and cap at 60 FPS
    pygame.display.flip()
    clock.tick(60)

# 4. Quit Pygame cleanly
pygame.quit()
