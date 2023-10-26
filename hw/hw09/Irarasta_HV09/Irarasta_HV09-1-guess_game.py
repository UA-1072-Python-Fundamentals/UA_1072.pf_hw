  ## Guess game with 10 tries:
import pygame
import random

pygame.init()

WIDTH, HEIGHT = 700, 300
BACKGROUND_COLOR = (0, 0, 0)
TEXT_COLOR = (255, 20, 147)
FONT = pygame.font.Font(None, 36)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Guess Game")

TARGET_NUMBER = random.randint(1, 100)
ATTEMPTS = 10
attempts = 0
guess = None
message = ""
attempt_counter = f"Attempts left: {ATTEMPTS}"
your_guess = "Your guess: "

running = True
game_over = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if not game_over:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif pygame.K_0 <= event.key <= pygame.K_9:
                    if attempts < ATTEMPTS:
                        if guess is None:
                            guess = 0
                        guess = guess * 10 + (event.key - pygame.K_0)
                elif event.key == pygame.K_RETURN:
                    if attempts < ATTEMPTS:
                        if guess is not None:
                            if guess < TARGET_NUMBER:
                                message = "No, my number is higher!"
                            elif guess > TARGET_NUMBER:
                                message = "No, my number is lower!"
                            else:
                                message = f"Congrats! You WIN! You`ve guessed the number ({TARGET_NUMBER})!"

                                game_over = True
                            attempts += 1
                            guess = None
                        if attempts >= ATTEMPTS and not game_over:
                            message = f"Sorry, but you lose! I WIN! My number was {TARGET_NUMBER}."
                            game_over = True
                    attempt_counter = f"Attempts left: {ATTEMPTS - attempts}"

                elif event.key == pygame.K_BACKSPACE:
                    if guess is not None:
                        guess //= 10

    screen.fill(BACKGROUND_COLOR)

    play_game_text = FONT.render("Play a Guess Game with me!", True, TEXT_COLOR)
    screen.blit(play_game_text, (10, 10))

    text = FONT.render(message, True, TEXT_COLOR)
    screen.blit(text, (10, 50))

    attempt_counter_text = FONT.render(attempt_counter, True, TEXT_COLOR)
    screen.blit(attempt_counter_text, (10, 90))

    guess_text = FONT.render(your_guess, True, TEXT_COLOR)
    screen.blit(guess_text, (10, 130))

    if not game_over:
        guess_text = FONT.render(f"{guess if guess is not None else ''}", True, TEXT_COLOR)
        screen.blit(guess_text, (160, 130))

    pygame.display.flip()

pygame.quit()


