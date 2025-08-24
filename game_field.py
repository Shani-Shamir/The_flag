import consts
import random
import pygame
import Screen
matrix1 = []

for i in range(consts.ROW):
    for j in range(consts.COL) :
        matrix1.append(consts.NO_MINE)

# def random_place_mine():
#     count = 0
#     while count <= 20 :
#         random_row = random.randint(0,consts.ROW)
#         random_col = random.randint(0, consts.COL)
#         if matrix[random_row][random_col] == consts.NO_MINE:
#             matrix[random_row][random_col] = consts.MINE
#             count += 1
# print(matrix)


def create_mine_lists():
    list_row = []
    list_col = []
    for i in range(0,consts.ROW):
        list_row.append(i)
    for i in range(0, consts.COL):
        list_col.append(i)
    return list_row,list_col

def random_place_mine():
    row,col = create_mine_lists()
    random_x = random.choice(col)
    random_y = random.choice(row)
    row.remove(random_x)
    col.remove(random_y)
    return random_x,random_y

def add_random_mine_matrix(matrix):
    for i in range(20):
        random_col,random_row = random_place_mine()
        matrix[random_row][random_col] = consts.MINE
    return matrix

matrix = add_random_mine_matrix(matrix1)
print(matrix)



# def player_move(screen):
#     x, y = 0, 0
#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_RIGHT]:
#         x += consts.SOLIDER_STEP
#     if keys[pygame.K_LEFT]:
#         x -= consts.SOLIDER_STEP
#     if keys[pygame.K_UP]:
#         y -= consts.SOLIDER_STEP
#     if keys[pygame.K_DOWN]:
#         y += consts.SOLIDER_STEP
#     Screen.draw_soldier(screen,x,y)
# pygame.display.flip()
