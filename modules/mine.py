import pygame
import random
pygame.init()

class Mine:
    def __init__(self):
        pass
    def random_x(self):
        return random.randint(1, 20)
    def random_y(self):
        return random.randint(1, 20)
