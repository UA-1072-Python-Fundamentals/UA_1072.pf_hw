import pygame
from random import randint

# setting
pygame.init()
gameDisplay = pygame.display.set_mode((900, 250))
pygame.display.set_caption("Your Game")
WHITE = (255, 255, 255)
done = False
clock = pygame.time.Clock()
have_tries = 10
x = randint(1, 100)
guess_number = ['0','0']
FONT = pygame.font.Font(None, 36)
color_text = (0, 20, 147)
comment = "Let's start"


# check answer
def try_guess_number(number, x):
    global have_tries
    global guess_number
    if have_tries > 0:
        if number == x:
            have_tries = 0
            guess_number = ['0', '0']
            return 'YOU ARE THE BEST'
        elif number > x:
            have_tries -= 1
            guess_number = ['0', '0']
            return 'Try lesser number'
        elif number < x:
            have_tries -= 1
            guess_number = ['0', '0']
            return 'Try higher number'
    else:
        return "You're lost"


# Game
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN and pygame.K_0 <= event.key <= pygame.K_9:
            if have_tries > 0:
                guess_number.append(event.dict['unicode'])
                guess_number.pop(0)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_KP_ENTER:
            comment = try_guess_number(int(''.join(guess_number)), x)

    y = int(''.join(guess_number))

    # Display
    gameDisplay.fill(WHITE)
    play_game_text = FONT.render("Guess the number between 1 and 100. And You have only 10 tries!", True, color_text)
    gameDisplay.blit(play_game_text, (5, 5))
    play_game_text = FONT.render("(Write 2 numbers and press Enter!)", True, color_text)
    gameDisplay.blit(play_game_text, (5, 35))
    guess_text = FONT.render(f'{comment}', True, color_text)
    gameDisplay.blit(guess_text, (5, 90))
    guess_text = FONT.render(f'You have tries {have_tries}', True, color_text)
    gameDisplay.blit(guess_text, (5, 120))
    guess_text = FONT.render(f'Your guess {y}', True, color_text)
    gameDisplay.blit(guess_text, (5, 150))
    pygame.display.update()

    clock.tick(10)
