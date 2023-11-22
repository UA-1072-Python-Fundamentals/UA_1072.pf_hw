import pygame
import random

pygame.init()
screen = pygame.display.set_mode((600, 300))
pygame.display.set_caption("Number Game")
font = pygame.font.Font(None, 40)
ran_num = random.randint(1, 100)

def game():
    tries = 10

    while tries > 0:
        screen.fill((114, 157, 224))

        text = font.render("Guess a number!", True, (0, 0, 0))
        screen.blit(text, (180, 120))
        text = font.render(f"Please enter a number (1-100): {tries} tries left", True, "Black")
        screen.blit(text, (17, 40))

        pygame.display.flip()

        user_num = ""

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    break
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if user_num:
                            guess = int(user_num)
                            if guess == ran_num:
                                screen.fill((123, 227, 166))
                                text = font.render("Congratulations! You've won! :)", True, (2, 38, 17))
                                screen.blit(text, (80, 100))
                                pygame.display.flip()
                                pygame.time.wait(1000)
                                pygame.quit()
                                break
                            elif guess > ran_num:
                                text = font.render("The number should be smaller", True, (161, 6, 6))
                                screen.blit(text, (5, 70))
                                tries -= 1
                            else:
                                text = font.render("The number should be bigger", True, (161, 6, 6))
                                screen.blit(text, (5, 70))
                                tries -= 1
                            user_num = ""
                            if tries == 0:
                                screen.fill((148, 33, 15))
                                text = font.render("You've lost :( Try harder next time", True, "Black")
                                screen.blit(text, (70, 100))
                                pygame.display.flip()
                                pygame.time.wait(2000)
                                pygame.quit()
                                break
                            break
                        else:
                            text = font.render("Please enter a number first.", True, "Black")
                            screen.blit(text, (180, 150))
                    else:
                        user_num += event.unicode
                        screen.fill((114, 157, 224))
                        tries_text = font.render(user_num, True, "Black")
                        screen.blit(tries_text, (100, 200))
                        amount_attempts = font.render(f"You have {tries} tries left", True, "Black")
                        screen.blit(amount_attempts, (5, 5))

            pygame.display.flip()

game()

