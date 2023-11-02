from random import randint
import pygame
from pygame.color import THECOLORS
from time import sleep

pygame.init()
screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()
font = pygame.font.SysFont('monaco', 40)
ex_text = ['Try again.',
            '>>> GUESSING GAME <<<',
            'PRESS "S" TO START!',
            'My number is higher!',
            'My number is less!',
            'YOU LOOSE!',
            'YOU WINNER!',
            'Enter number and press "Enter"'
            ]
magic_number = randint(1, 101)

def display():

    text = font.render(ex_text[1], True, THECOLORS['green'])
    screen.blit(text, (100, 100))
    text = font.render(ex_text[2], True, THECOLORS['green'])
    screen.blit(text, (130, 150))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                   game()
        pygame.display.flip()


def game():
    attempts = 10
    response = ''
    screen.fill((0, 0, 0))
    text = font.render(ex_text[7], True, THECOLORS['white'])
    screen.blit(text, (80, 150))

    while attempts > 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if int(response) > magic_number:
                        res = font.render(ex_text[4], True, THECOLORS['orange'])
                        screen.blit(res, (180, 150))
                    elif int(response) < magic_number:
                        res = font.render(ex_text[3], True, THECOLORS['orange'])
                        screen.blit(res, (180, 150))
                    else:
                        res = font.render(ex_text[6], True, THECOLORS['green'])
                        screen.blit(res, (220, 150))
                        attempts = 0
                    response = ''
                    attempts -= 1
                    if attempts == 0:
                        screen.fill((0, 0, 0))
                        loose = font.render(ex_text[5], True, THECOLORS['red'])
                        screen.blit(loose, (220, 150))
                else:
                    response += event.unicode
                    screen.fill((0, 0, 0))
                    tries = font.render(response, True, THECOLORS['blue'])
                    screen.blit(tries, (100, 200))
                    amount_attempts = font.render(f'You have {attempts} tries', True, THECOLORS['blue'])
                    screen.blit(amount_attempts, (5, 5))
   
        pygame.display.flip()
               
    sleep(2)
    pygame.quit()


display()
