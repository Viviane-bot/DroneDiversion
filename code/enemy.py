#!/usr/bin/python
# -*- coding: utf-8 -*-
from pygame.examples.grid import WINDOW_WIDTH

from code.Const import ENTITY_SPEED
from code.enemyShot import EnemyShot
from code.entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self, ):
        self.rect.centerx -= ENTITY_SPEED[self.name]

    def shoot(self):
      pass



