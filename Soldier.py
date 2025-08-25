import consts
import pygame
import Screen
import game_field
from consts import SOLDIER
from game_field import matrix_soldier

soldier_body = {"head" : None,
                "neck" : None,
                "stomach" : None,
                "legs" : None
}

# starting position screen
soldier_body["head"] = [(0,0) , (20,0)]
soldier_body["neck"] = [(0,20) , (20,20)]
soldier_body["stomach"] = [(0,40) , (20,40)]
soldier_body["legs"] = [(0,60) , (20,60)]

# starting position matrix
for i in range(4):
    for j in range(2):
        matrix_soldier[i][j] = consts.SOLDIER

def right():
    for i in range(consts.ROW):
        for j in range(consts.COL):
            if matrix_soldier[i][j] == consts.SOLDIER:
                matrix_soldier[i][j] = consts.EMPTY
                matrix_soldier[i][j+1] = consts.SOLDIER
def left():
    for i in range(consts.ROW):
        for j in range(consts.COL):
            if matrix_soldier[i][j] == consts.SOLDIER:
                matrix_soldier[i][j] = consts.EMPTY
                matrix_soldier[i][j-1] = consts.SOLDIER

def up():
    for i in range(consts.ROW):
        for j in range(consts.COL):
            if matrix_soldier[i][j] == consts.SOLDIER:
                matrix_soldier[i][j] = consts.EMPTY
                matrix_soldier[i+1][j] = consts.SOLDIER

def down():
    for i in range(consts.ROW):
        for j in range(consts.COL):
            if matrix_soldier[i][j] == consts.SOLDIER:
                matrix_soldier[i][j] = consts.EMPTY
                matrix_soldier[i-1][j] = consts.SOLDIER


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

update_soldier_place()