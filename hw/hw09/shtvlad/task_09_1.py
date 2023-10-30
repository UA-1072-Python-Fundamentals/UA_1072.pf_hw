import random

tries=10
attempt=1
rnd_num=random.randint(1,100)
print(f"Try to guess a number from 1 to 100 (you have {tries} tries):")
user_num=int(input(f"{attempt} attempt: "))
text_str = "Game over(( Maybe next time..."
while attempt<tries:
    if user_num>rnd_num:
        attempt+=1
        print("Your number is greater. Try one more time")
        user_num = int(input(f"{attempt} attempt: "))
    elif user_num<rnd_num:
        attempt += 1
        print("Your number is less. Try one more time")
        user_num = int(input(f"{attempt} attempt: "))
    else:
        text_str="Congratulations!!! You are the winner!"
        break

import pygame
pygame.init()

FPS = 20
WIDTH_DISPLAY = 500
HEIGHT_DISPLAY = 50
DELTA_STEP = 20
WHITE_COLOR = (255, 255, 255)
RED_COLOR = (250, 0, 0)

font = pygame.font.SysFont("Calibri", 25, True, False)
gameDisplay = pygame.display.set_mode((WIDTH_DISPLAY, HEIGHT_DISPLAY), pygame.RESIZABLE)
pygame.display.set_caption("Game result")

i = 0
cnt = 0

run = True
clock = pygame.time.Clock()

while run:
        # pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    gameDisplay.fill(WHITE_COLOR)
    i += 1
    gameDisplay.blit(font.render(text_str[0:i], True, RED_COLOR), [DELTA_STEP, 10])
    pygame.display.update()
    clock.tick(FPS)