import pygame, sys
import math
import time
from modules import menu

pygame.init()
# Set height and width of the screen
trigger = True
class Settings:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.distance_border = 20
        self.SoundOn = trigger
        #self.image = pygame.image.load("highscores.png")
        #self.add_background()
    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Give the signal to quit
                return True
            mouse = pygame.mouse.get_pos()

            #sound on
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouse[0] > (self.width/2 + 100) and mouse[0] < (self.width/2 + 150):
                    if mouse[1] > math.ceil(self.height/4) and mouse [1] < math.ceil(self.height/4) + 30:
                        menu.Sounds().click_sound()
                        time.sleep(0.2)
                        #self.SoundOn = 0
                        global trigger
                        trigger = True

            #sound off
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouse[0] > (self.width/2 + 175) and mouse[0] < (self.width/2 + 225):
                    if mouse[1] > math.ceil(self.height/4) and mouse [1] < math.ceil(self.height/4) + 30:
                        chk = Settings(800, 575).play_sound()
                        if chk == True:
                            menu.Sounds().click_sound()
                            time.sleep(0.2)
                        #self.SoundOn = 1
                        global trigger
                        trigger = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouse[0] > 350 and mouse[0] < 450:
                    if mouse[1] > math.ceil(7/8 * (self.height - self.distance_border * 2)) and mouse [1] < math.ceil(7/8 * (self.height - self.distance_border * 2)) + 35:
                        chk = Settings(800, 575).play_sound()
                        if chk == True:
                            menu.Sounds().click_sound()
                            time.sleep(0.2)
                        return True
        return False

    def show(self):
        while not self.process_events():
            self.draw_frame()
            self.add_text("Settings")
            self.sound_text("Sound")
            self.add_button()
            self.add_return()
            pygame.display.flip()

    def draw_frame(self):
        pygame.draw.rect(self.screen, (212, 212, 212),
                         pygame.Rect((self.distance_border, self.distance_border),
                                     ((self.width - self.distance_border * 2), (self.height - self.distance_border * 2))))

    def add_text(self, text):
        font = pygame.font.SysFont("arial", (math.ceil(self.width / 16)))
        caption = font.render(text, 1, (48, 148, 51))
        caption_position = caption.get_rect()
        self.screen.blit(caption, ((self.width / 2 - math.ceil(caption_position[2] / 2)), 50))

    def add_button(self):
        pygame.draw.rect(self.screen, (48, 148, 51), pygame.Rect((self.width/2 + 100, math.ceil(self.height/4)), (50, 30)))
        fonts = pygame.font.SysFont("arial", 20)
        menu = fonts.render("On", 1, (0, 0, 0))
        menu_position = (self.width/2 + 100, math.ceil(self.height/4))

        pygame.draw.rect(self.screen, (48, 148, 51), pygame.Rect((self.width / 2 + 175, math.ceil(self.height / 4)), (50, 30)))

        x = 500
        fonts = pygame.font.SysFont("arial", 20)
        start = fonts.render("On", 1, (0, 0, 0))
        stop = fonts.render("Off", 1, (0, 0, 0))
        stop_position = (stop.get_rect())
        start_position = (start.get_rect())
        list_of_fonts = [start_position, stop_position]
        list_of_text = [start, stop]
        text_items = 0
        for position_items in range(2):
            self.screen.blit(list_of_text[text_items], (math.ceil(x + ((50 - list_of_fonts[position_items][2]) / 2)),math.ceil(self.height / 4)))
            x = x + 65
            position_items = position_items + 1
            text_items = text_items + 1

    def sound_text(self, texts):
        font = pygame.font.SysFont("arial", 30)
        caption = font.render(texts, 1, (48, 148, 51))
        caption_position = caption.get_rect()
        self.screen.blit(caption, ((self.width / 2 - math.ceil(caption_position[2])),  math.ceil(self.height / 4)))

    def add_return(self):
        pygame.draw.rect(self.screen, (48, 148, 51), pygame.Rect((self.width/2 - 50, math.ceil(7/8 * (self.height - self.distance_border * 2))), (100, 35)))

    def play_sound(self):
        if self.SoundOn == True:
            return True