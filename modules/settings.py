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
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.distance_border = 20
        #self.image = pygame.image.load("highscores.png")
        #self.add_background()
    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Give the signal to quit
                return True
        return False

    def show(self):
        while not self.process_events():
            self.draw_frame()
            pygame.display.flip()

    def draw_frame(self):
        pygame.draw.rect(self.screen, (212, 212, 212),
                         pygame.Rect((self.distance_border, self.distance_border),
                                     ((self.width - self.distance_border * 2), (self.height - self.distance_border * 2))))

#Settings(width_screen, height).show()