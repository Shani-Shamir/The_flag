import pygame
import Soldier
import consts
import Screen
import game_field

def main():
    screen = Screen.create_screen()
    screen2 = Screen.draw_random_bush(screen)
    Screen.text(screen2)
    Screen.draw_flag(screen2)

    Screen.screenshot(screen2)
    pic_screenshot = pygame.image.load("screenshot.jpg")

    soldier = pygame.Rect(0,0,consts.WINDOW_WIDTH,consts.WINDOW_HEIGHT)
    soldier.x = 0
    soldier.y = 0
    Screen.draw_soldier(screen2, soldier.x, soldier.y)
    flag = True
    while flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
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
                    Screen.draw_random_mines(pic_screenshot, game_field.matrix,soldier.x,soldier.y)
                    pygame.time.delay(1000)
                    screen2.blit(pic_screenshot, (0, 0))
                Soldier.update_soldier_place()

                screen2.blit(pic_screenshot, (0, 0))
                Screen.draw_soldier(screen2, soldier.x, soldier.y)

        if Soldier.solider_touch_flag():
            Screen.win_text(screen2)
            pygame.time.delay(3000)
            flag = False
        if Soldier.soldier_touch_mine():
            Screen.lose_text(screen2)
            pygame.time.delay(3000)
            flag = False

        pygame.display.update()
        pygame.display.flip()

if __name__ == "__main__":
    main()

