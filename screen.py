#יצירת מסך
import pygame
from sys import exit
import random
import consts

pygame.init()
screen = pygame.display.set_mode((1000,800))
pygame.display.set_caption(consts.TITLE)

def background():
    screen.fill(consts.GREEN)

def draw_bush(x,y):
    bush = pygame.image.load(consts.GRASS_IMG)
    bush_size = (60,60)
    bush = pygame.transform.scale(bush, bush_size)
    screen.blit(bush,(x,y))

def create_lists():
    list_x = []
    list_y = []
    for i in range(0, 1001, 20):
        list_x.append(i)
    for i in range(0, 501, 20):
        list_y.append(i)
    return list_x,list_y

def draw_random_bushes():
    x,y = create_lists()
    random_place = (random.choice(x),random.choice(y))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    background()
    draw_bush(60,60)
    pygame.display.flip()


