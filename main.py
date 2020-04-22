import pygame
import math
from random import randint, random

# Initialise pygame
pygame.init()

# create the screen (determin window size)
screen = pygame.display.set_mode((800, 600))

#Title and Icon
pygame.display.set_caption("Pong")
icon = pygame.image.load('ping-pong.png')
pygame.display.set_icon(icon)

# Background Image
background = pygame.image.load('background.png')

# Player1 Image
player1_img = pygame.image.load('paddle.png')
player1_X = 385
player1_Y = 550

player1_X_change = 0

# Player2 Image
player2_img = pygame.image.load('paddle.png')
player2_X = 385
player2_Y = 20

player2_X_change = 0


# Ball Image
ballImg = pygame.image.load('block.png')

ballY_start = 290
ballX_start = 385

ballX = ballX_start
ballY = ballY_start

ballX_change = 0
ballY_change = 0

#Score and Text
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
textY = 10

# def show_score(x,y):
#     score = font.pygame.font.render(text, antialias, color, background=None)


player1_score = 0
player2_score = 0

# Draw game elements to screen


def player(playerImg, x, y):
    screen.blit(playerImg, (x, y))


def ball(x, y):
    screen.blit(ballImg, (x, y))

# Collision Detection


def isCollision_1(playerX, playerY, ballX, ballY):
    ball_size = 50
    paddle_size = 100

    if (ballX + ball_size) >= playerX and ballX <= (playerX + paddle_size) and (ballY + ball_size) == playerY:
        return True


def isCollision_2(playerX, playerY, ballX, ballY):
    ball_size = 50
    paddle_size = 100

    if ballY <= (playerY + 20) and (ballX + ball_size) >= playerX and ballX <= (playerX + paddle_size):
        return True


# Main Loop
running = True
while running:
    screen.fill((0, 0, 0))
    # Background image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            running = False

    # Player 1 movement if key stroke is pressed check its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("left arrow pressed")
                player1_X_change = -4
            elif event.key == pygame.K_RIGHT:
                print("right arrow pressed")
                player1_X_change = 4
            elif event.key == pygame.K_SPACE:
                print('ball started')
                ballY_change = 2

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                print("key released")
                player1_X_change = 0

    # Player 2 movement if key stroke is pressed check its A or D
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                print("a  pressed")
                player2_X_change = -4
            elif event.key == pygame.K_d:
                print("d pressed")
                player2_X_change = 4

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                print("key released")
                player2_X_change = 0


# Render objects to the screen
    player(player1_img, player1_X, player1_Y)
    player(player2_img, player2_X, player2_Y)
    ball(ballX, ballY)

# Updating movement
    player1_X += player1_X_change
    player2_X += player2_X_change
    ballY += ballY_change
    ballX += ballX_change

# Collition
    collision_player1 = isCollision_1(player1_X, player1_Y, ballX, ballY)
    if collision_player1:
        ballY_change *= -1
        ballX_change += random()

        print('collition')

    collision_player2 = isCollision_2(player2_X, player2_Y, ballX, ballY)
    if collision_player2:
        ballY_change *= -1
        ballX_change += random()
        print('collition')

# Giving objects boundries
    # Paddel
    if player1_X <= 0:
        player1_X = 0
    elif player1_X >= 700:
        player1_X = 700

    if player2_X <= 0:
        player2_X = 0
    elif player2_X >= 700:
        player2_X = 700

    # Ball Y Boundires
    if ballY <= -50:
        ballY = ballY_start
        ballX = ballX_start
        ballY_change = 0
        ballX_change = 0

        player2_score += 1
        print("Player 2 Score: " + str(player2_score))
    elif ballY > 600:
        ballY = ballY_start
        ballX = ballX_start
        ballY_change = 0
        ballX_change = 0

        player1_score += 1
        print("Player 1 Score: " + str(player1_score))

    # Ball X Boundries
    if ballX <= 0:
        ballX_change *= -1
    elif ballX >= 750:
        ballX_change *= -1

    pygame.display.update()
