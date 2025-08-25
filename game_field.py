import consts
import random
import pygame
import Screen

matrix = [[consts.NO_MINE for _ in range(consts.COL)] for _ in range(consts.ROW)]

def random_place_mine(matrix):
    count = 0
    while count <= 20 :
        random_row = random.randint(0,consts.ROW -1)
        random_col = random.randint(0, consts.COL -1)
        if matrix[random_row][random_col] == consts.NO_MINE:
            matrix[random_row][random_col] = consts.MINE
            count += 1

def player_move(screen):
    x, y = 0, 0
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        x += consts.SOLIDER_STEP
    if keys[pygame.K_LEFT]:
        x -= consts.SOLIDER_STEP
    if keys[pygame.K_UP]:
        y -= consts.SOLIDER_STEP
    if keys[pygame.K_DOWN]:
        y += consts.SOLIDER_STEP
    Screen.draw_soldier(screen,x,y)
pygame.display.flip()

def touched_flag(x,y):
