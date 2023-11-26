import pygame
import sys
import random


pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Розмір екрану
WIDTH, HEIGHT = 800, 600

# Розмір платформи та блоків
PLATFORM_WIDTH, PLATFORM_HEIGHT = 100, 10
BLOCK_WIDTH, BLOCK_HEIGHT = 50, 20


platform_speed = 0

# Екран
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Арканоїда")

# Початкові координати м'яча
ball_x = WIDTH // 2
ball_y = HEIGHT // 2

# Початкова швидкість м'яча
ball_speed_x = 5.2 * random.choice((1, -1))
ball_speed_y = 5.2

# Початкові координати платформи
platform_x = WIDTH // 2 - PLATFORM_WIDTH // 2
platform_y = HEIGHT - PLATFORM_HEIGHT - 10

# Створення блоків
blocks = []
for row in range(5):
    for col in range(16):
        block = pygame.Rect(col * (BLOCK_WIDTH + 5), row * (BLOCK_HEIGHT + 5), BLOCK_WIDTH, BLOCK_HEIGHT)
        blocks.append(block)

class Button:
    def __init__(self, text, x, y, width, height, color, highlight_color, action=None):
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.highlight_color = highlight_color
        self.action = action
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, screen, font):
        pygame.draw.rect(screen, self.color, self.rect)
        pygame.draw.rect(screen, BLACK, self.rect, 2)
        text_surface = font.render(self.text, True, BLACK)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def is_mouse_over(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())

# Кнопки
play_button = Button("Грати", WIDTH // 2 - 100, HEIGHT // 2, 265, 50, (0, 255, 0), (0, 200, 0), "play")
exit_main_menu_button = Button("Вийти", WIDTH // 2 - 100, HEIGHT // 2 + 60, 265, 50, (255, 0, 0), (200, 0, 0), "exit_main_menu")
try_again_button = Button("Спробувати ще раз", WIDTH // 2 - 100, HEIGHT // 2, 265, 50, (0, 255, 0), (0, 200, 0), "try_again")
exit_game_button = Button("Вийти", WIDTH // 2 - 100, HEIGHT // 2 + 60, 265, 50, (255, 0, 0), (200, 0, 0), "exit_game")

def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)

# Функція відображення головного меню
def show_main_menu(clock):
    font = pygame.font.Font(None, 36)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if play_button.is_mouse_over():
                    return True
                elif exit_main_menu_button.is_mouse_over():
                    pygame.quit()
                    sys.exit()

        screen.fill(WHITE)
        draw_text("Арканоїда", font, BLACK, screen, WIDTH // 2, HEIGHT // 4)
        play_button.draw(screen, font)
        exit_main_menu_button.draw(screen, font)
        pygame.display.flip()
        clock.tick(60)

# Функція для відображення меню після програшу або перемоги
def show_menu(message, clock):
    global platform_speed
    font = pygame.font.Font(None, 36)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    platform_speed = 0  # Скидаю швидкість платформи
                    return True  # Повертаю True для розпочатку гри

                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if try_again_button.is_mouse_over():
                    platform_speed = 0
                    return True
                elif exit_game_button.is_mouse_over():
                    pygame.quit()
                    sys.exit()

        screen.fill(WHITE)
        draw_text(message, font, BLACK, screen, WIDTH // 2, HEIGHT // 4)
        try_again_button.draw(screen, font)
        exit_game_button.draw(screen, font)
        pygame.display.flip()
        clock.tick(60)

# Цикл гри
def main():
    global ball_speed_x, ball_speed_y, ball_x, ball_y, platform_x, platform_speed, platform_y, blocks

    clock = pygame.time.Clock()

    while True:
        if show_main_menu(clock):  # Показую головне меню та чекаю, поки гравець вибере "Грати"
            # Скидаю стан гри
            ball_x = WIDTH // 2
            ball_y = HEIGHT // 2
            ball_speed_x = 5.2 * random.choice((1, -1))
            ball_speed_y = 5.2
            platform_x = WIDTH // 2 - PLATFORM_WIDTH // 2
            platform_y = HEIGHT - PLATFORM_HEIGHT - 10
            blocks = []
            for row in range(5):
                for col in range(16):
                    block = pygame.Rect(col * (BLOCK_WIDTH + 5), row * (BLOCK_HEIGHT + 5), BLOCK_WIDTH, BLOCK_HEIGHT)
                    blocks.append(block)

            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            platform_speed = -7
                        if event.key == pygame.K_RIGHT:
                            platform_speed = 7

                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                            platform_speed = 0

                    # Рух миші
                    if event.type == pygame.MOUSEMOTION:
                        platform_x = event.pos[0] - PLATFORM_WIDTH / 2

                # Рух платформи
                platform_x += platform_speed

                # Рух м'яча
                ball_x += ball_speed_x
                ball_y += ball_speed_y

                # Відбивання м'яча від стін
                if ball_x <= 0 or ball_x >= WIDTH:
                    ball_speed_x = -ball_speed_x

                if ball_y <= 0:
                    ball_speed_y = -ball_speed_y

                # Відбивання м'яча від платформи
                if (
                    platform_x < ball_x < platform_x + PLATFORM_WIDTH
                    and platform_y < ball_y + 10 < platform_y + PLATFORM_HEIGHT
                ):
                    ball_speed_y = -ball_speed_y

                # Зіткнення м'яча з блоками
                for block in blocks:
                    if block.colliderect(pygame.Rect(ball_x, ball_y, 10, 10)):
                        blocks.remove(block)
                        ball_speed_y = -ball_speed_y

                # Перевірка, чи всі блоки знищені (перемога)
                if not blocks:
                    if show_menu("Ви перемогли! Розпочати нову гру?", clock):
                        break  # Якщо гравець вибрав "Розпочати нову гру", виходимо з циклу та починаю нову гру

                # Перевірка, чи м'яч впав нижче платформи (програш)
                if ball_y >= HEIGHT:
                    if not show_menu("Упс, ви не зловили м'яч:(", clock):
                        pygame.quit()
                        sys.exit()
                    else:
                        break  # Якщо гравець вибрав "Спробувати ще раз", виходимо з циклу та починаю нову гру

                # Оновлення екрану
                screen.fill(WHITE)
                pygame.draw.rect(screen, RED, (platform_x, platform_y, PLATFORM_WIDTH, PLATFORM_HEIGHT))
                pygame.draw.circle(screen, BLACK, (ball_x, ball_y), 10)

                for block in blocks:
                    pygame.draw.rect(screen, BLACK, block)

                pygame.display.flip()
                clock.tick(60)

if __name__ == "__main__":
    main()
