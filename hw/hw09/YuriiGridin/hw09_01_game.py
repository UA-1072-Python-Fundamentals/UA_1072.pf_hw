# Example file showing a basic pygame "game loop"
import pygame
from random import randint


# pygame setup
pygame.init()
screen = pygame.display.set_mode((640, 150))
clock = pygame.time.Clock()
screen.fill("gray")
font = pygame.font.SysFont('Calibri', 25, True, False)
text1 = font.render("Input number: ", True, [0, 0, 0])
running = True
need_input = True
input_text = ""
main_text = [f"Guess a number from range 1 to 100 in 10 tries!",
             f"Input a number end press 'Enter'"
             ]
num = randint(1, 100)
count = 1


def print_text(msg_main, msg_number):
    font_type = pygame.font.SysFont('Calibri', 25, True, False)
    screen.fill("gray")
    pygame.draw.rect(screen, (0, 200, 0), (10, 110, 100, 25))
    i = 0
    for mess in msg_main:
        text_main = font_type.render(mess, True, (0, 0, 0))
        screen.blit(text_main, [10, 5+i])
        i += 25
    text_number = font_type.render(msg_number, True, (0, 0, 0))
    screen.blit(text_number, [10, 110])


def guess(number, guess_number, i):
    global need_input
    number = int(number)
    if i < 10:
        if guess_number == number:
            t = [f"You are win!!! Number is {number}.",
                 f"Attempts {i}/10"]
            need_input = False
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
        need_input = False
        return t


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if need_input and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                main_text = guess(input_text, num,  count)
                input_text = ""
                count += 1
            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            else:
                if len(input_text) < 3:
                    input_text += event.unicode

    print_text(main_text, input_text)
    pygame.display.update()
    clock.tick(30)  # limits FPS to 60

pygame.quit()