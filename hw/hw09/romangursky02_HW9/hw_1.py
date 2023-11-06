import pygame
import random

pygame.init()
screen = pygame.display.set_mode((600, 300))
pygame.display.set_caption("Guess Number Game")
font = pygame.font.Font(None, 40)
ran_num = random.randint(1, 100)

# Define background colors
background_color = (114, 157, 224)
win_color = (123, 227, 166)
lose_color = (148, 33, 15)

def game_number():
    attempt = 10

    while attempt > 0:
        screen.fill(background_color)

        text = font.render("Guess a number!", True, (0, 0, 0))
        screen.blit(text, (180, 120))
        text = font.render(f"Please enter a number (1-100): {attempt} tries left", True, "Black")
        screen.blit(text, (17, 40))

        pygame.display.flip()

        user_num = ""

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if user_num:
                            guess = int(user_num)
                            if guess == ran_num:
                                screen.fill(win_color)
                                text = font.render("Congratulations! You've won! :)", True, (2, 38, 17))
                                screen.blit(text, (80, 100))
                                pygame.display.flip()
                                pygame.time.wait(1000)
                                pygame.quit()
                                return
                            elif guess > ran_num:
                                text = font.render("The number should be smaller", True, (161, 6, 6))
                                screen.blit(text, (5, 70))
                                attempt -= 1
                            else:
                                text = font.render("The number should be bigger", True, (161, 6, 6))
                                screen.blit(text, (5, 70))
                                attempt -= 1
                            user_num = ""
                            if attempt == 0:
                                screen.fill(lose_color)
                                text = font.render("You've lost :( Try harder next time", True, "Black")
                                screen.blit(text, (70, 100))
                                pygame.display.flip()
                                pygame.time.wait(2000)
                                pygame.quit()
                                return
                            break
                        else:
                            text = font.render("Please enter a number first.", True, "Black")
                            screen.blit(text, (180, 150))
                    else:
                        user_num += event.unicode
                        screen.fill(background_color)
                        tries_text = font.render(user_num, True, "Black")
                        screen.blit(tries_text, (100, 200))
                        amount_attempts = font.render(f"You have {attempt} tries left", True, "Black")
                        screen.blit(amount_attempts, (5, 5))

            pygame.display.flip()

game_number()
