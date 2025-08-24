import pygame
import consts
import Screen
# שינוי
screen = Screen.create_screen()

Screen.background(screen)
Screen.draw_random_bush(screen)
Screen.draw_soldier(screen,0,0)
Screen.draw_flag(screen)
Screen.draw_web(screen)

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             exit()
#     pygame.display.flip()

x,y =0,0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            x += consts.SOLIDER_STEP
        if keys[pygame.K_LEFT]:
            x -= consts.SOLIDER_STEP
        if keys[pygame.K_UP]:
            y -= consts.SOLIDER_STEP
        if keys[pygame.K_DOWN]:
            y += consts.SOLIDER_STEP
        Screen.draw_soldier(screen,x,y)

    pygame.display.flip()
