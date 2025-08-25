
import consts
import random


matrix = [[consts.NO_MINE for _ in range(consts.COL)] for _ in range(consts.ROW)]

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
#
# def player_move(screen):
#     x, y = 0, 0
#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_RIGHT] and 0 < x < consts.WINDOW_WIDTH:
#         x += consts.SOLIDER_STEP
#     if keys[pygame.K_LEFT] and 0 < x < consts.WINDOW_WIDTH:
#         x -= consts.SOLIDER_STEP
#     if keys[pygame.K_UP] and 0 < y < consts.WINDOW_HEIGHT :
#         y -= consts.SOLIDER_STEP
#     if keys[pygame.K_DOWN] and 0 < y < consts.WINDOW_HEIGHT:
#         y += consts.SOLIDER_STEP
#     Screen.draw_soldier(screen,x,y)
# pygame.display.flip()
#
# def touched_flag(x,y):
#     return x,y == consts.FLAG_LOCATION
#
# def touched_mine(x,y):
#     return x,y ==
#
# running = True
# if touched_flag(x,y):
#     running = False
#
# if touched_mine(x,y):
#     running = False

# pygame.display.flip()

# while running:
#     x, y = 0, 0
#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_RIGHT] and 0 < x < consts.WINDOW_WIDTH:
#         x += consts.SOLIDER_STEP
#     if keys[pygame.K_LEFT] and 0 < x < consts.WINDOW_WIDTH:
#         x -= consts.SOLIDER_STEP
#     if keys[pygame.K_UP] and 0 < y < consts.WINDOW_HEIGHT:
#         y -= consts.SOLIDER_STEP
#     if keys[pygame.K_DOWN] and 0 < y < consts.WINDOW_HEIGHT:
#         y += consts.SOLIDER_STEP
#     if keys == pygame.QUIT:
#         pygame.quit()
#         exit()
