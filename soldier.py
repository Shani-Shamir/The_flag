import consts
import pygame
import Screen

def draw_soldier():
    soldier = pygame.image.load(consts.SOLIDER_IMG)
    soldier = pygame.transform.scale(soldier, consts.SOLDIER_SIZE)
    Screen.screen.blit(soldier,(100,100))

#