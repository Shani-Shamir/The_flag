import pygame
import consts
import Screen
import game_field

# שינוי
screen = Screen.create_screen()
screen2 = Screen.draw_random_bush(screen)
Screen.draw_soldier(screen2,0,0)
Screen.text(screen2)

Screen.draw_flag(screen2)
# Screen.draw_web(screen)

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

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # x, y = 0, 0
        # keys = pygame.key.get_pressed()
        if event.type == pygame.KEYDOWN:
            screen2.blit(screen2, (0, 0))
            if event.key == pygame.K_RIGHT and 0 <= soldier.x <= consts.WINDOW_WIDTH:
                soldier.x += consts.SOLIDER_STEP
            if event.key == pygame.K_LEFT and 0 <= soldier.x <= consts.WINDOW_WIDTH:
                soldier.x -= consts.SOLIDER_STEP
            if event.key == pygame.K_UP and 0 <= soldier.y <= consts.WINDOW_HEIGHT:
                soldier.y -= consts.SOLIDER_STEP
            if event.key == pygame.K_DOWN and 0 <= soldier.y <= consts.WINDOW_HEIGHT:
                soldier.y += consts.SOLIDER_STEP
        Screen.draw_soldier(screen2, soldier.x, soldier.y)
        screen2.blit(screen2, (0, 0))
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

