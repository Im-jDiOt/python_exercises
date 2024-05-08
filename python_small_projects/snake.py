import pygame
import sys

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
movement = 50
key_pressed = False
condition = 0
running = True

white = (255, 255, 255)
black = (0, 0, 0)

pygame.init()
pygame.display.set_caption("Simple PyGame Example")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pos_x = 200
pos_y = 200

clock = pygame.time.Clock()
while running:
    clock.tick(5)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                condition = 1
                key_pressed = True
            elif event.key == pygame.K_RIGHT:
                condition = 2
                key_pressed = True
            elif event.key == pygame.K_UP:
                condition = 3
                key_pressed = True
            elif event.key == pygame.K_DOWN:
                condition = 4
                key_pressed = True
        elif event.type == pygame.KEYUP:
            key_pressed = False

    if condition == 1:
        pos_x -= movement
        key_pressed = True
    elif condition ==2:
        pos_x += movement
        key_pressed = True
    elif condition ==3:
        pos_y -= movement
        key_pressed = True
    elif condition ==4:
        pos_y += movement
        key_pressed = True

    screen.fill(black)
    pygame.draw.rect(screen, white, (pos_x, pos_y, 50, 50))

    for i in range(10):     
        pygame.draw.line(screen, white, (50*i, 0), (50*i, SCREEN_HEIGHT), 1)
    for j in range(10):
        pygame.draw.line(screen, white, (0, 50*j), (SCREEN_WIDTH, 50*j), 1)

    pygame.display.update()
