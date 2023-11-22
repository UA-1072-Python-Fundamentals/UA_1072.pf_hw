import pygame
from random import randint

# pygame setup
pygame.init()
size = (600, 300)
background_colour = (135, 0, 108)
font = pygame.font.SysFont('Calibri', 20, True, False)
text_colour = (255, 255, 255)
clock = pygame.time.Clock()

pygame.display.set_caption('Guess game')
screen = pygame.display.set_mode(size)

random_number = randint(1, 100)
max_attempts = 10
attempts = 0
message = ""
guess = None
attempt_counter = f"{max_attempts - attempts} attempts left! "
your_number = "Your number:"

running = True

while running:
    # poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if attempts < max_attempts:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif pygame.K_0 <= event.key <= pygame.K_9:
                    if guess is None:
                        guess = 0
                    guess = guess * 10 + (event.key - pygame.K_0)
                elif event.key == pygame.K_RETURN:
                    if attempts < max_attempts:
                        if guess is not None:
                            if guess < random_number:
                                message = "No, my number is higher!"
                            elif guess > random_number:
                                message = "No, my number is lower!"
                            else:
                                message = f"Congratulations! You guessed the number ({random_number})!"
                                attempts = max_attempts
                            attempts += 1
                            guess = None
                        if attempts >= max_attempts and running is not False:
                            message= f"Sorry, but you lose! I WIN! My number was {random_number}."
        
                    attempt_counter = f"{max_attempts - attempts} attempts left!"
                
                elif event.key == pygame.K_BACKSPACE:
                    if guess is not None:
                        guess //= 10

    # fill the screen with a color to wipe away anything from the last frame
    screen.fill(background_colour)

    # RENDER YOUR GAME HERE
    title = font.render("Guess the number between 1 and 100 in only 10 tries!", True, text_colour)
    screen.blit(title, (50, 10))

    task = font.render('Write your number and click on ENTER', True, text_colour)
    screen.blit(task, (100, 35))

    text = font.render(message, True, text_colour)
    screen.blit(text, (10, 90))

    attempt_counter_text = font.render(attempt_counter, True, text_colour)
    screen.blit(attempt_counter_text, (10, 120))

    user_number = font.render(f"{your_number}{guess if guess is not None else ''}", True, text_colour)
    screen.blit(user_number, (10, 170))

    # flip() the display to put your work on the screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()

