import consts
import random

matrix = [[consts.NO_MINE for _ in range(consts.COL)] for _ in range(consts.ROW)]
matrix_soldier = [[consts.NO_MINE for _ in range(consts.COL)] for _ in range(consts.ROW)]

for row in range(22,25):
    for col in range(46,50):
        matrix[row][col] = consts.FLAG

def random_place_mine(matrix):
    count = 0
    list_mines = []
    while count <= 20 :
        random_row = random.randint(0,consts.ROW -1)
        random_col = random.randint(0, consts.COL -1)
        if matrix[random_row][random_col] == consts.NO_MINE:
            matrix[random_row][random_col] = consts.MINE
            count += 1
            list_mines.append((random_col*20,random_row*20))
    return list_mines
