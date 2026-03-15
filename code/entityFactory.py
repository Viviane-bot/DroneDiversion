#!/usr/bin/python
# -*- coding: utf-8 -*-
import background

from code.Const import WIN_WIDTH
from code.background import Background


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



