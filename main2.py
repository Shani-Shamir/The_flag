import pygame
import consts
import Screen
from game_field import touched_flag

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
            if event.key == pygame.K_RIGHT:
                soldier.x += consts.SOLIDER_STEP
            if event.key == pygame.K_LEFT:
                soldier.x -= consts.SOLIDER_STEP
            if event.key == pygame.K_UP:
                soldier.y -= consts.SOLIDER_STEP
            if event.key == pygame.K_DOWN:
                soldier.y += consts.SOLIDER_STEP
        Screen.draw_soldier(screen2, soldier.x, soldier.y)
        screen2.blit(screen2, (0, 0))

        pygame.display.update()
        #
        # if event.type == pygame.KEYUP:
        #     screen2.blit(screen2, (0, 0))

            # pygame.display(screen2)

    #
    pygame.display.flip()

running = True
x, y = 0, 0
while running :
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and 0 <= x <= consts.WINDOW_WIDTH:
        x += consts.SOLIDER_STEP
    if keys[pygame.K_LEFT] and 0 <= x <= consts.WINDOW_WIDTH:
        x -= consts.SOLIDER_STEP
    if keys[pygame.K_UP] and 0 <= y <= consts.WINDOW_HEIGHT:
        y -= consts.SOLIDER_STEP
    if keys[pygame.K_DOWN] and 0 <= y <= consts.WINDOW_HEIGHT:
        y += consts.SOLIDER_STEP
    if keys == pygame.QUIT:
        pygame.quit()
        exit()
    if touched_flag(x,y):
        running = False
#

