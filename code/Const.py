#C
import pygame

COLOR_BLUE = (0,12,123)
COLOR_WHITE = (255,255,255)
COLOR_BLACK = (0,0,0)
COLOR_YELLOW = (255,255,0)

#E
EVENT_ENEMY = pygame.USEREVENT + 1
ENTITY_SPEED = {
    'level1bg0': 0,
    'level1bg1': 1,
    'level1bg2': 2,
    'level1bg3': 3,
    'Player1':3,
    'Enemy':2,
}
ENTITY_HEALTH = {
    'level1bg0': 999,
    'level1bg1': 999,
    'level1bg2': 999,
    'level1bg3': 999,
    'Player1':300,
    'Enemy':50,
}

#MENU
MENU_OPTION = ('START GAME',
               'SCORE',
               'EXIT')




# W
WIN_WIDTH = 576
WIN_HEIGHT = 324