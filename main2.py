import pygame
import consts
import Screen
import game_field
import time

from Screen import draw_night_soldier

screen = Screen.create_screen()
screen2 = Screen.draw_random_bush(screen)
Screen.text(screen2)
Screen.draw_flag(screen2)

Screen.screenshot(screen2)
pic_screenshot = pygame.image.load("screenshot.jpg")
# screen2.blit(pic_screenshot, (0, 0))

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             exit()
#     pygame.display.flip()
# soldier = pygame.image.load(consts.SOLIDER_IMG)

soldier = pygame.Rect(0,0,consts.WINDOW_WIDTH,consts.WINDOW_HEIGHT)
soldier.x = 0
soldier.y = 0
Screen.draw_soldier(screen2, soldier.x, soldier.y)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # x, y = 0, 0
        # keys = pygame.key.get_pressed()
        if event.type == pygame.KEYDOWN:
            screen2.blit(screen2, (0, 0))
            if event.key == pygame.K_RIGHT:
                if 0 <= soldier.x <= consts.WINDOW_WIDTH-40:
                    soldier.x += consts.SOLIDER_STEP
                else:
                    soldier.x = 950
            if event.key == pygame.K_LEFT:
                if 0 <= soldier.x <= consts.WINDOW_WIDTH:
                    soldier.x -= consts.SOLIDER_STEP
                else:
                    soldier.x = 0
            if event.key == pygame.K_UP:
                if 0<= soldier.y <= consts.WINDOW_HEIGHT :
                    soldier.y -= consts.SOLIDER_STEP
                else:
                    soldier.y = 0
            if event.key == pygame.K_DOWN:
                if 0 <= soldier.y < consts.WINDOW_HEIGHT-60:
                    soldier.y += consts.SOLIDER_STEP
                else:
                    soldier.y = 420
            if event.key == pygame.K_RETURN:
                screen3 = Screen.draw_random_mines(pic_screenshot, game_field.matrix,soldier.x,soldier.y)
            # screen2.blit(screen2, (0, 0))

            screen2.blit(pic_screenshot, (0, 0))
            Screen.draw_soldier(screen2, soldier.x, soldier.y)


        pygame.display.update()
        #
        # if event.type == pygame.KEYUP:
        #     screen2.blit(screen2, (0, 0))

            # pygame.display(screen2)
    pygame.display.flip()

# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             exit()
#
#         # x, y = 0, 0
#         # keys = pygame.key.get_pressed()
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_RIGHT and 0 <= soldier.x <= consts.WINDOW_WIDTH:
#                 soldier.x += consts.SOLIDER_STEP
#             if event.key == pygame.K_LEFT and 0 <= soldier.x <= consts.WINDOW_WIDTH:
#                 soldier.x -= consts.SOLIDER_STEP
#             if event.key == pygame.K_UP and 0 <= soldier.y <= consts.WINDOW_HEIGHT:
#                 soldier.y -= consts.SOLIDER_STEP
#             if event.key == pygame.K_DOWN and 0 <= soldier.y <= consts.WINDOW_HEIGHT:
#                 soldier.y += consts.SOLIDER_STEP
#             if game_field.touched_flag(soldier.x, soldier.y):
#                 pygame.quit()
#                 running = False
#         # Screen.draw_soldier(screen2, soldier.x, soldier.y)
#         screen2.blit(screen2, (0, 0))
#         pygame.display.update()
#
#             # pygame.display(screen2)
#     pygame.display.flip()

