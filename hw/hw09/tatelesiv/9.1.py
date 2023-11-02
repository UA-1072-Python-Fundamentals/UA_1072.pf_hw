# Task 9.1
import pygame
from random import randint

pygame.init()
gameDisplay = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
gameDisplay.fill("WHITE")
font = pygame.font.SysFont('Calibri', 25, True, False)
text = font.render("Enter your number: ", True, "BLACK")
running = True
require_input = True
input_text = ""
main_text = [f'Guess the number from 1 to 100 in 10 tries.',
             f'Input a number and press "Enter"']
number = randint(1, 100)
count = 1


def printing_the_text(msg_main, msg_number):
        font_type = pygame.font.SysFont('Calibri', 25, True, False)
        gameDisplay.fill("WHITE")
        pygame.draw.rect(gameDisplay, (200, 200, 200), (10, 110, 100, 25))
        i = 0
        for mess in msg_main:
            text_main = font_type.render(mess, True, (0, 0, 0))
            gameDisplay.blit(text_main, [10, 5 + i])
            i += 25
        text_number = font_type.render(msg_number, True, (0, 0, 0))
        gameDisplay.blit(text_number, [10, 110])


def guess(number, guess_number, i):
    global require_input
    number = int(number)
    if i < 10:
        if guess_number == number:
            t = [f"You won!!! The number is {number}.",
                 f"Attempts {i}/10"]
            require_input = False
            return t
        elif not (0 < number < 100):
            t = [f"Your number is not in range from 1 to 100.",
                 f"Attempts {i}/10.",
                 f"Try again.",
                 f"Input a number end press 'Enter'",
                 ]
            return t
        elif number < guess_number:
            t = [f"You number is less than guess number.",
                 f"Attempts {i}/10.",
                 f"Try again.",
                 f"Input a number end press 'Enter'",
                    ]
            return t
        elif number > guess_number:
            t = [f"You number is more than guess number.",
                 f"Attempts {i}/10.",
                 f"Try again.",
                 f"Input a number end press 'Enter'",
                 ]
            return t
    else:
        t = [f"You didn't guess a number.",
             f"Attempts 10/10.",
             f"Game over."]
        require_input = False
        return t


while running:
    for event in pygame.event.get ():
        if event.type == pygame.QUIT:
            running = False
        if require_input and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                main_text = guess(input_text, number, count)
                input_text = ""
                count += 1
            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            else:
                if len(input_text) < 3:
                    input_text += event.unicode
    printing_the_text(main_text, input_text)
    pygame.display.update()
    clock.tick(60)
pygame.quit()
