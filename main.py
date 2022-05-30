import pygame

pygame.init()

win = pygame.display.set_mode((1000, 500))

pygame.display.set_caption("Ciekawa Gierka")

x = 250
y = 250
radius = 15
vel_x = 10
vel_y = 10
jump = False

run = True
while run:

    win.fill((255, 255, 255))

    pygame.draw.circle(win, (0, 0, 0), (int(x), int(y)), radius)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    userInput = pygame.key.get_pressed()

    if userInput[pygame.K_a] and x > 0:
        x -= vel_x

    if userInput[pygame.K_d] and x < 1000:
        x += vel_x

    if jump is False and userInput[pygame.K_w]:
        jump = True

    if jump is True:
        y -= vel_y*4
        vel_y -= 1
        if vel_y < -10:
            jump = False
            vel_y = 10

    pygame.time.delay(20)

    pygame.display.update()
