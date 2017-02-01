import pygame, sys
import math
import random
import time
from modules import highscores
from modules import settings
from modules import sounds
WHITE = (255 ,255 ,255)
pygame.init()
width_screen = 800
height = 575
pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
# Set height and width of the screen


class Menu:
    def __init__(self, distance_border, width_screen, height):
        self.distance_border = distance_border
        self.width_screen = width_screen
        self.height = height
        self.display = ((width_screen, height))
        self.screen = pygame.display.set_mode(self.display)
        # formula by Gerard Bakker
        self.width_blocks = 100
        self.number_blocks = 3
        self.space_left_with_blocks = self.width_screen - (self.width_blocks * self.number_blocks)
        # space left after space_left_with_block - distance_border
        self.space_left = self.space_left_with_blocks - (self.distance_border * 2)
        # distance between border and first block
        self.distance_between = self.space_left / (self.number_blocks + 1)
        # space between the blocks
        self.space_between = self.width_blocks + self.distance_between
        # start point of the blocks
        self.start_point = self.distance_between + self.distance_border
        # end point of the blocks
        self.end_point = self.width_screen - int(self.start_point + self.width_blocks)
        self.help_needed = False
    def draw_frame(self):
        pygame.draw.rect(self.screen, (212, 212, 212),
                         pygame.Rect((self.distance_border, self.distance_border),
                                     ((self.width_screen - self.distance_border * 2), (self.height - self.distance_border * 2))))

    def add_logo(self):
        size_image = 280
        radius_image = 280/2

        img = pygame.image.load("assets/logo.png")
        self.screen.blit(img, (self.width_screen/2 - radius_image, self.width_screen*(1/16)))

    def add_help(self, position):
        help_img = pygame.image.load("assets/help.png")

        help_positon_x = self.width_screen - self.distance_border - position
        pygame.draw.rect(self.screen, (212, 212, 212),
                         pygame.Rect((help_positon_x, self.distance_border),(position, position)))
        self.screen.blit(help_img, (help_positon_x, self.distance_border))

    def add_settings(self, position):
        help_img = pygame.image.load("assets/settings.png")
        add_square_x = self.distance_border
        settings_x = self.distance_border  + 5
        pygame.draw.rect(self.screen, (212, 212, 212),
                         pygame.Rect((add_square_x, self.distance_border),(position, position)))
        self.screen.blit(help_img, (settings_x, self.distance_border + 5))


    def draw_button(self):
        # calculates the remaining space after the blocks are added

        x = self.start_point
        # draws the blocks on the screen
        while x <= self.end_point:
            pygame.draw.rect(self.screen, (48, 148, 51),
                             pygame.Rect((x, ((self.height - self.distance_border * 2) * (7 / 8))), (self.width_blocks, 35)))

            x = x + self.space_between
        x = self.start_point
        fonts = pygame.font.SysFont("arial", 20)
        start = fonts.render("Start", 1, (0, 0, 0))
        stop = fonts.render("Quit", 1, (0, 0, 0))
        highscores = fonts.render("Highscores", 1, (0, 0, 0))
        stop_position = (stop.get_rect())
        start_position = (start.get_rect())
        highscores_position = (highscores.get_rect())
        list_of_fonts = [start_position, stop_position, highscores_position]
        list_of_text = [stop, start, highscores]
        text_items = 0
        for position_items in range(self.number_blocks):
            self.screen.blit(list_of_text[text_items], (math.ceil(x + ((self.width_blocks - list_of_fonts[position_items][2]) /2)), ((self.height - self.distance_border * 2) * (7 / 8) + 5)))
            x = x + self.space_between
            position_items = position_items + 1
            text_items = text_items+ 1

    def show(self):
        while not self.process_events():
            menu = Menu(20, 800, 575)
            menu.draw_frame()
            menu.add_logo()
            menu.add_help(40)
            menu.add_settings(40)
            menu.draw_button()
            menu.show_instructions()
            pygame.display.flip()

    def show_instructions(self):

        mouse = pygame.mouse.get_pos()
        if mouse[1] >= 20 and mouse[1] <= 60:
            if mouse[0] >= 740 and mouse[0] <= 780:
                image = pygame.image.load("assets/help.jpg")
                self.screen.blit(image, (0, 0))


    def process_events(self):
        coordinates = self.start_point
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Give the signal to quit
                sys.exit()
            mouse = pygame.mouse.get_pos()
            if mouse[0] > 20 and mouse[0] < 60:
                if mouse[1] > 20 and mouse[1] < 60:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        settings.Settings(800, 575).show()
            if (mouse[1] >= (math.ceil(((7/8) * self.height) - 35)) and mouse[1] <= math.ceil(7/8 * self.height)):
                if (mouse[0] >= coordinates and mouse[0] <= coordinates + self.width_blocks):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        chk = settings.Settings(800, 575).play_sound()
                        if chk == True:
                            sounds.Sounds().exit_sound()
                            time.sleep(0.3)
                        sys.exit()
                elif (mouse[0] >= (coordinates + self.width_blocks +  self.distance_between) and mouse[0] <= (coordinates + self.width_blocks + self.distance_between + self.width_blocks)):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        chk = settings.Settings(800, 575).play_sound()
                        if chk == True:
                            sounds.Sounds().click_sound()
                            time.sleep(0.2)
                        return True
                elif (mouse[0] >= 565 and mouse[0] <= 665):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        highscores.Highscores(800, 575).show()
        return False