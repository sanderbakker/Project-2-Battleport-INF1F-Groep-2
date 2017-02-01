import pygame, sys
import time
import os

from os import path
class Animation:
    def __init__(self, Game):
        self.explosion = ['explosion_frame_0.png', 'explosion_frame_1.png', 'explosion_frame_2.png',
                          'explosion_frame_3.png', 'explosion_frame_4.png', 'explosion_frame_5.png',
                          'explosion_frame_6.png']
        self.Game = Game
    def load_explosion(self):
        list_loaded = [pygame.image.load("modules/effects/explosion/explosion_frame_0.png"),
                       pygame.image.load("modules/effects/explosion/explosion_frame_1.png"),
                       pygame.image.load("modules/effects/explosion/explosion_frame_2.png"),
                       pygame.image.load("modules/effects/explosion/explosion_frame_3.png"),
                       pygame.image.load("modules/effects/explosion/explosion_frame_4.png"),
                       pygame.image.load("modules/effects/explosion/explosion_frame_5.png"),
                       pygame.image.load("modules/effects/explosion/explosion_frame_6.png")]
        return list_loaded

    def add_animation(self):
        list_loaded = [pygame.image.load("modules/effects/explosion/explosion_frame_0.png"),
                       pygame.image.load("modules/effects/explosion/explosion_frame_1.png"),
                       pygame.image.load("modules/effects/explosion/explosion_frame_2.png"),
                       pygame.image.load("modules/effects/explosion/explosion_frame_3.png"),
                       pygame.image.load("modules/effects/explosion/explosion_frame_4.png"),
                       pygame.image.load("modules/effects/explosion/explosion_frame_5.png"),
                       pygame.image.load("modules/effects/explosion/explosion_frame_6.png")]
        for animation in range(len(list_loaded)):
            print(self.Game.get_screen())
            screen = self.Game.get_screen()
            screen.blit(list_loaded[animation], (100, 100))
            #time.sleep(0.1)
            #pygame.display.flip()

