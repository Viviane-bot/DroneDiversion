#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        pygame.mixer.music.load('asset/menu.wav')
        pygame.mixer.music.play(-1)

        while True:
            menu = Menu(self.window)
            menu.run()
            pass

            # Check for all events
            #for envent in pygame.event.get():
                #if envent.type == pygame.QUIT:
                    #pygame.quit()  # Close Window
                    #quit() # end pygame

