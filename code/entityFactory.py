#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

import background

from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.background import Background
from code.enemy import Enemy
from code.player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name:str, position=(0,0)):
        match entity_name:
            case 'level1bg':
                list_bg = []
                for i in range(4):
                    list_bg.append(Background(f'level1bg{i}', (0, 0)))
                    list_bg.append(Background(f'level1bg{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'Player1':
                return Player('Player1',(10,    WIN_HEIGHT / 2))
            case 'Enemy':
                return Enemy('Enemy',(WIN_WIDTH + 10, random.randint(0, WIN_HEIGHT)))



