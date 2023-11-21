import pygame
import sys

pygame.init()

pygame.display.set_caption("Rectangle Game")
width_screen = 400
height_screen = 400

x_coord = 180
y_coord = 170
width_rect = 40
height_rect = 60
step = 5

blue = (12, 11, 38)
red = (255, 0, 0)  # Change the background color to red
white = (255, 255, 255)

screen = pygame.display.set_mode((width_screen, height_screen), pygame.RESIZABLE)
screen.fill(red)  # Set the background color to red
FPS = 60

font = pygame.font.Font(None, 36)

running = True
clock = pygame.time.Clock()

while running:
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x_coord - step > 0:
        x_coord = x_coord - step
    if keys[pygame.K_RIGHT] and x_coord + step < width_screen - width_rect:
        x_coord = x_coord + step
    if keys[pygame.K_UP] and y_coord - step > 0:
        y_coord = y_coord - step
    if keys[pygame.K_DOWN] and y_coord + step < height_screen - height_rect:
        y_coord = y_coord + step

    screen.fill(red)  # Fill the screen with the red background color

    pygame.draw.rect(screen, white, [x_coord, y_coord, width_rect, height_rect])

    # Add text "Player" to the rectangle
    text_surface = font.render("Player", True, blue)
    text_rect = text_surface.get_rect(center=(x_coord + width_rect / 2, y_coord + height_rect / 2))
    screen.blit(text_surface, text_rect)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
sys.exit()

