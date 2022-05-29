import pygame

pygame.init()

win = pygame.display.set_mode((800, 800))

pygame.display.set_caption("Ciekawa Gierka")

x = 400
y = 400
radius = 15
vel = 10

run = True
while run:

    win.fill((0, 0, 0))

    pygame.draw.circle(win, (50, 135, 168), (int(x), int(y)), radius)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    userInput = pygame.key.get_pressed()

    if userInput[pygame.K_a] and x > 0:
        x -= vel

    if userInput[pygame.K_d] and x < 800:
        x += vel

    if userInput[pygame.K_w] and y > 0:
        y -= vel

    if userInput[pygame.K_s] and y < 800:
        y += vel

    pygame.time.delay(15)

    pygame.display.update()
