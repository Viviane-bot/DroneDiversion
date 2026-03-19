#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Const import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH, PLAYER_KEY_SHOOT
from code.entity import Entity
from code.playerShot import PlayerShot


class Player(Entity):
    def __init__(self, name:str, position: tuple):
        super().__init__(name, position)

    def move(self, ):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_UP] and self.rect.top >0:
            self.rect.centery -= ENTITY_SPEED[self.name]
        if pressed_keys[pygame.K_DOWN] and self.rect.bottom < WIN_HEIGHT:
            self.rect.centery += ENTITY_SPEED[self.name]
        if pressed_keys[pygame.K_LEFT] and self.rect.left >0:
            self.rect.centerx -= ENTITY_SPEED[self.name]
        if pressed_keys[pygame.K_RIGHT] and self.rect.right < WIN_WIDTH:
            self.rect.centerx += ENTITY_SPEED[self.name]
        pass

    def shoot(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[PLAYER_KEY_SHOOT[self.name]]:
            return PlayerShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))
