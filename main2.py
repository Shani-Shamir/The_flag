import pygame
import consts
import Screen
# שינוי
screen = Screen.create_screen()
Screen.draw_random_bush(screen)
Screen.draw_soldier(screen,0,0)
Screen.text(screen)

Screen.draw_flag(screen)
# Screen.draw_web(screen)

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             exit()
#     pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()