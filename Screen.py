#יצירת מסך
import pygame
from sys import exit
import random
import consts

def create_screen():
    pygame.init()
    screen = pygame.display.set_mode((consts.WINDOW_WIDTH,consts.WINDOW_HEIGHT))
    pygame.display.set_caption(consts.TITLE)
    return screen

def background(screen):
    screen.fill(consts.GREEN)

def draw_bush(screen,x,y):
    bush = pygame.image.load(consts.GRASS_IMG)
    bush_size = (60,60)
    bush = pygame.transform.scale(bush, bush_size)
    screen.blit(bush,(x,y))

def create_lists():
    list_x = []
    list_y = []
    for i in range(0, 981, 20):
        list_x.append(i)
    for i in range(0, 481, 20):
        list_y.append(i)
    return list_x,list_y

def random_place_bush():
    x,y = create_lists()
    random_x = random.choice(x)
    random_y = random.choice(y)
    x.remove(random_x)
    y.remove(random_y)
    return random_x,random_y

def draw_random_bush(screen):
    for i in range(20):
        random_x,random_y = random_place_bush()
        draw_bush(screen,random_x,random_y)

def draw_soldier(screen,x,y):
    soldier = pygame.image.load(consts.SOLIDER_IMG)
    soldier = pygame.transform.scale(soldier, consts.SOLDIER_SIZE)
    screen.blit(soldier,(x,y))

def draw_flag(screen):
    flag = pygame.image.load(consts.FLAG_IMG)
    flag = pygame.transform.scale(flag, consts.FLAG_SIZE)
    screen.blit(flag, (920, 440))

def draw_horizontal_lines():
    for i in range(20,501,20):
        pygame.draw.line(screen, (consts.GREEN),
                         [0, 20],
                         [1000, 20], 1)

def draw_web(screen):
    screen.fill((0,0,0))

    pygame.draw.line(screen, (consts.GREEN),
                     [0, 20],
                     [1000, 20], 1)


# background()
# draw_random_bush()
# draw_soldier(0,0)
# draw_flag()
# draw_web()
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             exit()
#     pygame.display.flip()


