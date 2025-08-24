import pygame
import consts
import Screen

screen = Screen.create_screen()

Screen.background(screen)
Screen.draw_random_bush(screen)
Screen.draw_soldier(screen,0,0)
Screen.draw_flag(screen)
# Screen.draw_web(screen)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.flip()
