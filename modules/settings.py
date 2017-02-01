import pygame, sys
import math
import time
from modules import menu
from modules import sounds
pygame.init()
# Set height and width of the screen
trigger = True #menu effects
trigger2 = True #game effects
sounds.Sounds().stop_game_sound()
sounds.Sounds().start_game_sound()
class Settings:
    # inits the settings
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.distance_border = 20
        self.SoundOn = trigger
        self.GameSoundOn = trigger2
        #self.image = pygame.image.load("highscores.png")
        #self.add_background()
    # checks if the buttons in the settings are clicked on
    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Give the signal to quit
                return True
            mouse = pygame.mouse.get_pos()

            chk = Settings(800, 575).play_sound()
            chk2 = Settings(800, 575).play_gamesound()

            #sound on menu sounds
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouse[0] > (self.width/2 + 100) and mouse[0] < (self.width/2 + 150):
                    if mouse[1] > math.ceil(self.height/4) and mouse [1] < math.ceil(self.height/4) + 30:
                        sounds.Sounds().click_sound()
                        time.sleep(0.2)
                        #self.SoundOn = 0
                        global trigger
                        trigger = True

            #sound off menu sounds
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouse[0] > (self.width/2 + 175) and mouse[0] < (self.width/2 + 225):
                    if mouse[1] > math.ceil(self.height/4) and mouse [1] < math.ceil(self.height/4) + 30:

                        if chk == True:
                            sounds.Sounds().click_sound()
                            time.sleep(0.2)
                        #self.SoundOn = 1
                        global trigger
                        trigger = False

            # sound on game sounds
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouse[0] > (self.width / 2 + 100) and mouse[0] < (self.width / 2 + 150):
                    if mouse[1] > math.ceil(self.height / 3) and mouse[1] < math.ceil(self.height / 3) + 30:
                        pass
                        if chk == True:
                            sounds.Sounds().click_sound()
                            time.sleep(0.2)
                        #self.SoundOn = 1
                        #global trigger2
                        #trigger2 = False
                    sounds.Sounds().start_game_sound()

            # sound off game sounds
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouse[0] > (self.width / 2 + 175) and mouse[0] < (self.width / 2 + 225):
                    if mouse[1] > math.ceil(self.height / 3) and mouse[1] < math.ceil(self.height / 3) + 30:
                        pass
                        if chk == True:
                            sounds.Sounds().click_sound()
                            time.sleep(0.2)
                        #self.SoundOn = 1
                        #global trigger2
                        #trigger2 = False
                    sounds.Sounds().stop_game_sound()

            # start button
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouse[0] > 350 and mouse[0] < 450:
                    if mouse[1] > math.ceil(7/8 * (self.height - self.distance_border * 2)) and mouse [1] < math.ceil(7/8 * (self.height - self.distance_border * 2)) + 35:

                        if chk == True:
                            sounds.Sounds().click_sound()
                            time.sleep(0.2)
                        return True
        return False
    # shows the settings menu
    def show(self):
        while not self.process_events():
            self.draw_frame()
            self.add_text("Settings")
            self.sound_text(["Menu Effects", "Game Effects"])
            self.add_button()
            self.add_return()
            self.add_button_text("Menu")
            pygame.display.flip()
    # draws a frame
    def draw_frame(self):
        pygame.draw.rect(self.screen, (212, 212, 212),
                         pygame.Rect((self.distance_border, self.distance_border),
                                     ((self.width - self.distance_border * 2), (self.height - self.distance_border * 2))))
    # add text "Settings" to the screen
    def add_text(self, text):
        font = pygame.font.SysFont("arial", (math.ceil(self.width / 16)))
        added_text = font.render(text, 1, (48, 148, 51))
        text_position = added_text.get_rect()
        self.screen.blit(added_text, ((self.width / 2 - math.ceil(text_position[2] /2)), 50))
    # add's a button to the screen
    def add_button(self):
        pygame.draw.rect(self.screen, (48, 148, 51), pygame.Rect((self.width/2 + 100, math.ceil(self.height/4)), (50, 30)))
        pygame.draw.rect(self.screen, (48, 148, 51), pygame.Rect((self.width / 2 + 175, math.ceil(self.height / 4)), (50, 30)))
        pygame.draw.rect(self.screen, (48, 148, 51),
                         pygame.Rect((self.width / 2 + 100, math.ceil(self.height / 3)), (50, 30)))
        pygame.draw.rect(self.screen, (48, 148, 51),
                         pygame.Rect((self.width / 2 + 175, math.ceil(self.height / 3)), (50, 30)))

        x = 500
        fonts = pygame.font.SysFont("arial", 20)
        on_text = fonts.render("On", 1, (0, 0, 0))
        off_text = fonts.render("Off", 1, (0, 0, 0))
        on_position = (on_text.get_rect())
        off_position = (off_text.get_rect())
        list_of_fonts = [on_position, off_position, off_position, on_position]
        list_of_text = [on_text, off_text, off_text, on_text]
        text_items = 0
        for position_items in range(4):
            if position_items < 2:
                self.screen.blit(list_of_text[text_items], (math.ceil(x + ((50 - list_of_fonts[position_items][2]) / 2)),math.ceil(self.height / 4) + 2))
                x = x + 75
                position_items = position_items + 1
                text_items = text_items + 1
            else:
                x = x - 75
                self.screen.blit(list_of_text[text_items], (
                math.ceil(x + ((50 - list_of_fonts[position_items][2]) / 2)), math.ceil(self.height / 3) + 2))
                position_items = position_items + 1
                text_items = text_items + 1


    #add's the text "Sound" on the screen
    def sound_text(self, texts):
        font = pygame.font.SysFont("arial", 30)
        divided_by = 4
        for i in range(len(texts)):
            caption = font.render(texts[i], 1, (48, 148, 51))
            caption_position = caption.get_rect()
            self.screen.blit(caption, ((self.width / 2 - math.ceil(caption_position[2]) - 100),  self.height / divided_by))
            divided_by -= 1
    # add return button
    def add_return(self):
        pygame.draw.rect(self.screen, (48, 148, 51), pygame.Rect((self.width/2 - 50, math.ceil(7/8 * (self.height - self.distance_border * 2))), (100, 35)))
    # check is the sound is on or off
    def play_sound(self):
        if self.SoundOn == True:
            return True
    # check if game sounds is on or off
    def play_gamesound(self):
        if self.GameSoundOn == True:
            return True
    # adds text to the button
    def add_button_text(self, text):
        fonts = pygame.font.SysFont("arial", 20)
        entered_text = fonts.render(text, 1, (0, 0, 0))
        entered_text_position = entered_text.get_rect()
        x_position = self.width/2 - math.floor(entered_text_position[2]/2)
        y_position = math.ceil(7/8 * (self.height - self.distance_border * 2)) + 4
        self.screen.blit(entered_text, (x_position,y_position ))