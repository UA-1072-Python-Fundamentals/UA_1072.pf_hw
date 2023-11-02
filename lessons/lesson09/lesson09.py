import pygame

pygame.init()

gameDisplay = pygame.display.set_mode((900, 600))
pygame.display.set_caption('My first game')
font = pygame.font.SysFont('Calibri', 25, True, False)

clock = pygame.time.Clock()
colors = {
    'Aqua': (0, 255, 255),
    'Black': (0, 0, 0),
    'Blue': (0, 0, 255),
    'Fuchsia': (255, 0, 255),
    'Gray': (128, 128, 128),
    'Green': (0, 128, 0),
    'Lime': (0, 255, 0),
    'Maroon': (128, 0, 0),
    'Navy Blue': (0, 0, 128),
    'Olive': (128, 128, 0),
    'Purple': (128, 0, 128),
    'Red': (255, 0, 0),
    'Silver': (192, 192, 192),
    'Teal': (0, 128, 128),
    'White': (255, 255, 255),
    'Yellow': (255, 255, 0),
    'WHITE': (255, 255, 255),
}
r, g, b = 0, 0, 0
done = False
figures = []
pointlist = []
text = font.render("Congratilations", True, colors["Black"])
point = [100, 100]
KEYDOWN = False


def rect_move(key):
    if key == 119 and point[1] > 0:
        point[1] -= 20
    elif key == 100:
        point[0] += 20
    elif key == 115:
        point[1] += 20
    elif key == 97:
        point[0] -= 20


while not done:
    # # --- Main event loop
    # r += 1
    # if r > 255:
    #     r = 0
    #     g += 1
    #     if g > 255:
    #         g = 0
    #         b += 1
    #         if b > 255:
    #             r = g = b = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            print("User asked to quit.")
        elif event.type == pygame.KEYDOWN:
            print("User pressed a key.", event)
            KEYDOWN = True
            key = event.dict.get("key")
        elif event.type == pygame.KEYUP:
            print("User let go of a key.", event)
            KEYDOWN = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # print("User pressed a mouse button", event.dict)
            if event.dict.get("button") == 3:
                figures.append(pointlist)
                pointlist = []
            elif event.dict.get("button") == 1:
                pointlist.append(event.dict.get("pos"))

    # print((r, g, b))
    # gameDisplay.fill((r, g, b))
    gameDisplay.fill(colors['WHITE'])
    gameDisplay.blit(text, [10, 10])
    # print(figures)
    for i in range(len(figures)):
        if len(figures[i]) > 2:
            # pygame.draw.polygon(gameDisplay, random.choice(list(colors.values())), figures[i], width=0)
            pygame.draw.polygon(gameDisplay, list(colors.values())[i % len(list(colors.values()))], figures[i], width=0)
            text = font.render(f"figure_{i}", True, colors["Black"])
            gameDisplay.blit(text, figures[i][0])
    if KEYDOWN:
        rect_move(key)
    # pygame.draw.rect(gameDisplay, colors["Lime"], pygame.Rect(point[0], point[1], 30, 30), width=0)
    car_img = pygame.image.load("./images.jfif")
    gameDisplay.blit(car_img, point)
    pygame.display.update()
    clock.tick(60)

