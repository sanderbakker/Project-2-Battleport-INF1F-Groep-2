import pygame, sys
import random
import math
import time
import os

from os import path
width = 117
height = 113
display = ((width, height))
pygame.init()
Display = pygame.display.set_mode(display)

clock = pygame.time.Clock()
explosion_list = ['explosion_frame_0.png', 'explosion_frame_1.png', 'explosion_frame_2.png', 'explosion_frame_3.png', 'explosion_frame_4.png', 'explosion_frame_5.png', 'explosion_frame_6.png']

def load_image(name):
    image = pygame.image.load("effects/explosion/" + str(name))
    #image = pygame.image.load(name)
    #bakkie = os.path.basename('assets/effects/explosion/')
    #image = pygame.image.load(os.path.join(bakkie, str(name)))
    return image

class TestSprite(pygame.sprite.Sprite):
    def __init__(self):
        super(TestSprite, self).__init__()
        self.images = []

        for img in explosion_list:
            self.images.append(load_image((img)))
        # assuming both images are 64x64 pixels

        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(5, 5, 64, 64)

    def update(self):
        '''This method iterates through the elements inside self.images and
        displays the next one each tick. For a slower animation, you may want to
        consider using a timer of some sort so it updates slower.'''
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]

def main():
    pygame.init()
    screen = pygame.display.set_mode((117, 113))

    my_sprite = TestSprite()
    my_group = pygame.sprite.Group(my_sprite)


    while True:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

        # Calling the 'my_group.update' function calls the 'update' function of all
        # its member sprites. Calling the 'my_group.draw' function uses the 'image'
        # and 'rect' attributes of its member sprites to draw the sprite.
        my_group.clear(screen, pygame.Surface(Display.get_size()))
        my_group.update()
        my_group.draw(screen)
        time.sleep(0.1)
        pygame.display.flip()
main()