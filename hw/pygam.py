import pygame
pygame.init()
gameDisplay = pygame.display.set_mode((800,600)) 
pygame.display.set_caption('My first game')
clock = pygame.time.Clock() 
BLUE = (255, 255, 255)
done = False
clock = pygame.time.Clock()
while not done:
# --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
            gameDisplay.fill(WHITE)
# --- Go ahead and update the screen with what we've drawn.
pygame.display.update()
# --- Limit to 60 frames per second
clock.tick(60)
