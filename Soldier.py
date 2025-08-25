import consts
import pygame
import Screen
import game_field
from consts import SOLDIER
from game_field import matrix_soldier
from game_field import matrix

# soldier_body = {"head" : None,
#                 "neck" : None,
#                 "stomach" : None,
#                 "legs" : None
# }
#
# # starting position screen
# soldier_body["head"] = [(0,0) , (20,0)]
# soldier_body["neck"] = [(0,20) , (20,20)]
# soldier_body["stomach"] = [(0,40) , (20,40)]
# soldier_body["legs"] = [(0,60) , (20,60)]

# starting position matrix
for i in range(4):
    for j in range(2):
        if i == 3:
            matrix_soldier[i][j] = consts.FEET
        else:
            matrix_soldier[i][j] = consts.BODY

def right():
    for i in range(consts.ROW):
        for j in range(consts.COL):
            if matrix_soldier[i][j] == consts.FEET:
                matrix_soldier[i][j] = consts.NO_MINE
                matrix_soldier[i][j+1] = consts.FEET
            if matrix_soldier[i][j] == consts.BODY:
                matrix_soldier[i][j] = consts.NO_MINE
                matrix_soldier[i][j + 1] = consts.BODY

def left():
    for i in range(consts.ROW):
        for j in range(consts.COL):
            if matrix_soldier[i][j] == consts.FEET:
                matrix_soldier[i][j] = consts.NO_MINE
                matrix_soldier[i][j-1] = consts.FEET
            if matrix_soldier[i][j] == consts.BODY:
                matrix_soldier[i][j] = consts.NO_MINE
                matrix_soldier[i][j - 1] = consts.BODY

def up():
    for i in range(consts.ROW):
        for j in range(consts.COL):
            if matrix_soldier[i][j] == consts.FEET:
                matrix_soldier[i][j] = consts.NO_MINE
                matrix_soldier[i+1][j] = consts.FEET
            if matrix_soldier[i][j] == consts.BODY:
                matrix_soldier[i][j] = consts.NO_MINE
                matrix_soldier[i+1][j] = consts.BODY

def down():
    for i in range(consts.ROW):
        for j in range(consts.COL):
            if matrix_soldier[i][j] == consts.FEET:
                matrix_soldier[i][j] = consts.NO_MINE
                matrix_soldier[i-1][j] = consts.FEET
            if matrix_soldier[i][j] == consts.BODY:
                matrix_soldier[i][j] = consts.NO_MINE
                matrix_soldier[i-1][j] = consts.BODY

def update_soldier_place():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                 right()
            if event.key == pygame.K_LEFT:
                left()
            if event.key == pygame.K_UP:
                up()
            if event.key == pygame.K_DOWN:
                down()

def soldier_touch_mine():
    for row in range (consts.ROW):
        for col in range(consts.COL):
            if matrix[row][col] == consts.MINE:
                if matrix_soldier[row][col] == consts.FEET:
                    return True
    return False

def solider_touch_flag():
    for row in range(22,25):
        for col in range(46,50):
            if matrix_soldier[row][col] == consts.BODY:
                return True
    return False


