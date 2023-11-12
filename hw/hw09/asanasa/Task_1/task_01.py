import pygame
import random

pygame.init()

window_width = 800
window_height = 600

window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Guess the number!")

white = (200, 114, 204)
black = (0, 0, 0)

font = pygame.font.Font(None, 36)

target_number = random.randint(1, 100)
attempts = 0
max_attempts = 10

input_text = ''
input_rect = pygame.Rect(100, 400, 140, 32)
active = False

result_text = ''

attempts = 0

running = True
while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                try:
                    guess = int(input_text)
                except ValueError:
                    result_text = "Please enter an integer number."
                else:
                    attempts += 1
                    if guess == target_number:
                        result_text = f"Congratulations! You guessed the number {target_number} after {attempts} attempts."
                        running = True
                    elif attempts >= max_attempts:
                        result_text = f"You have exhausted all attempts. The hidden number was {target_number}."
                        running = True
                    else:
                        result_text = "The hidden number is greater." if guess < target_number else "The hidden number is smaller."
                input_text = ''
            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            else:
                input_text += event.unicode

    window.fill(white)


    text_surface = font.render("Guess the number from 1 to 100:", True, black)
    window.blit(text_surface, (10, 40))


    result_surface = font.render(result_text, True, black)
    window.blit(result_surface, (10, 70))


    txt_surface = font.render(input_text, True, black)
    width = max(200, txt_surface.get_width() + 10)
    input_rect.w = width
    window.blit(txt_surface, (input_rect.x + 5, input_rect.y + 5))
    pygame.draw.rect(window, black, input_rect, 2)

    attempts_text = font.render(f"Attempts: {attempts}/{max_attempts}", True, (0, 0, 0))
    window.blit(attempts_text, (10, 10))

    pygame.display.flip()



