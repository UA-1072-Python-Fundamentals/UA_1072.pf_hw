import weather
import pygame
from pygame.color import THECOLORS as color

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((750, 200))
font = pygame.font.SysFont('monaco', 40)
font_big = pygame.font.SysFont('monaco', 60)
text = ['Hello!',
        'I will tell you the weather in any city.',
        'Enter your city and press "Enter".',
        ]
speach_01 = font.render(text[0], True, color['red'])
speach_02 = font.render(text[1], True, color['red'])
speach_03 = font.render(text[2], True, color['red'])
screen.fill((color['yellow']))
screen.blit(speach_01, (60, 40))
screen.blit(speach_02, (160, 40))
screen.blit(speach_03, (100, 90))
user_city = ''
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                result = str(weather.weather(user_city))
                speach_05 = font_big.render(result, True, color['blue'])
                screen.blit(speach_05, (0, 100))
                user_city = ''
                done = False
            else:
                user_city += event.unicode
                screen.fill(color['yellow'])
                speach_04 = font_big.render(user_city, True, color['red'])
                screen.blit(speach_04, (0, 0))

    pygame.display.flip()



# print(weather.weather('Kyiv'))