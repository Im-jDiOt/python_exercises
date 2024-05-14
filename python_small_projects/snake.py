import pygame
import sys
import random
from collections import deque

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
movement = 50
key_pressed = False
condition = 0
running = True
point = 0
queue = deque(maxlen=5)

white = (255, 255, 255)
black = (0, 0, 0)
food = (255,0,0)

pos_x = 200
pos_y = 200
food_x = random.randint(0,9)*50
food_y = random.randint(0,9)*50

pygame.init()
pygame.display.set_caption("snake.py")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()
while running:
    clock.tick(5)

    # movement
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
    elif condition == 2:
        pos_x += movement
        key_pressed = True
    elif condition == 3:
        pos_y -= movement
        key_pressed = True
    elif condition == 4:
        pos_y += movement
        key_pressed = True

    queue.append((pos_x, pos_y))
    print(queue)

    # food event
    if (pos_x==food_x) and (pos_y==food_y):
        point += 1

        food_x = random.randint(0,9)*50
        food_y = random.randint(0,9)*50
   
    # screen draw
    screen.fill(black)

    for i in range(point+1):
        pygame.draw.rect(screen, white, (queue[-1-i][0], queue[-1- i][1], 50, 50))
    pygame.draw.rect(screen, food, (food_x, food_y, 50, 50))

    for i in range(10):     
        pygame.draw.line(screen, white, (50*i, 0), (50*i, SCREEN_HEIGHT), 1)
    for j in range(10):
        pygame.draw.line(screen, white, (0, 50*j), (SCREEN_WIDTH, 50*j), 1)

    pygame.display.update()
