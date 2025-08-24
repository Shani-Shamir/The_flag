import consts
import random
matrix = []

for i in range(consts.ROW):
    for j in range(consts.COL) :
        matrix.append(consts.NO_MINE)

def random_place_mine():

    while True:
        random_matrix_place = matrix[random.randint(0, consts.ROW)][0, consts.COL]
        if random_matrix_place == consts.NO_MINE:
            random_matrix_place = consts.MINE


