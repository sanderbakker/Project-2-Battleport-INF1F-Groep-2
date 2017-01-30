import pygame, sys
import math
import time

WHITE = (205 ,205 ,205)
pygame.init()
width_screen = 800
height = 575
sound = 0
# Set height and width of the screen


class Settings:
    def __init__(self, width_screen, height):
        self.width_screen = width_screen
        self.height = height
        self.display = ((width_screen, height))
        self.screen = pygame.display.set_mode(self.display)

    def background(self):
        settback = pygame.image.load("assets/window.png")
        self.screen.blit(settback, (0, 0))

    def sound_button(self, position):
        sound_on = pygame.image.load("assets/sound_on.png")
        sound_off = pygame.image.load("assets/sound_off.png")
        sound_onresize = pygame.transform.scale(sound_on, (50, 50))
        sound_offresize = pygame.transform.scale(sound_off, (50, 50))
        self.screen.blit(sound_onresize, (0,0))

    def show(self):
            self.background()
            self.sound_button()
            pygame.display.flip()

Settings(width_screen, height)
