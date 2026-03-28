#C
import pygame

COLOR_BLUE = (0,12,123)
COLOR_WHITE = (255,255,255)
COLOR_BLACK = (0,0,0)
COLOR_YELLOW = (255,255,0)
COLOR_GREEN = (0,128,0)
COLOR_CYAN = (0,128,128)

#E
EVENT_ENEMY = pygame.USEREVENT + 1
ENTITY_SPEED = {
    'level1bg0': 0,
    'level1bg1': 1,
    'level1bg2': 0,
    'level1bg3': 2,
    'Player1':3,
    'Player1Shot':3,
    'Enemy':1,
    'EnemyShot':2,

}

ENTITY_HEALTH = {
    'level1bg0': 999,
    'level1bg1': 999,
    'level1bg2': 999,
    'level1bg3': 999,
    'Player1':300,
    'Player1Shot':1,
    'Enemy':50,
    'EnemyShot':50,

}
ENTITY_DAMAGE = {
    'level1bg0': 0,
    'level1bg1': 0,
    'level1bg2': 0,
    'level1bg3': 0,
    'Player1':1,
    'Player1Shot':25,
    'Enemy':1,
    'EnemyShot':20,

}

ENTITY_SCORE = {
    'level1bg0': 0,
    'level1bg1': 0,
    'level1bg2': 0,
    'level1bg3': 0,
    'Player1':0,
    'Player1Shot':0,
    'Enemy':100,
    'EnemyShot':0,

}



ENTITY_SHOT_DELAY = {
    'Player1':20,
    'Enemy':100,
}
#MENU
MENU_OPTION = ('START GAME',
               'SCORE',
               'EXIT')

#P
PLAYER_KEY_UP = {'Player1':pygame.K_UP}
PLAYER_KEY_DOWN = {'Player1':pygame.K_DOWN}
PLAYER_KEY_LEFT = {'Player1':pygame.K_LEFT}
PLAYER_KEY_RIGHT = {'Player1':pygame.K_RIGHT}
PLAYER_KEY_SHOOT = {'Player1': pygame.K_RCTRL}

#S
SPAWN_TIME = 4000



# W
WIN_WIDTH = 576
WIN_HEIGHT = 324