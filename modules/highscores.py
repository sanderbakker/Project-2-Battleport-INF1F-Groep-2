from modules import mysql
import pygame
import math
import sys
pygame.init()

class Highscores:
    # init for the highscores
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.distance_border = 20
        self.image = pygame.image.load("assets/highscores.png")
        self.add_background()
    # checks if a button is pressed in the highscore screen and returns to the menu
    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Give the signal to quit
                return True
            mouse = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouse[0] > 350 and mouse[0] < 450:
                    if mouse[1] > math.ceil(7 / 8 * (self.height - self.distance_border * 2)) and mouse[1] < math.ceil(
                                            7 / 8 * (self.height - self.distance_border * 2)) + 35:
                        return True
        return False
    # adds text to the button
    def add_button_text(self, text):
        fonts = pygame.font.SysFont("arial", 20)
        entered_text = fonts.render(text, 1, (0, 0, 0))
        entered_text_position = entered_text.get_rect()
        x_position = self.width/2 - math.floor(entered_text_position[2]/2)
        y_position = math.ceil(7/8 * (self.height - self.distance_border * 2)) + 4
        self.screen.blit(entered_text, (x_position,y_position ))
    # displays the highscore screen
    def show(self):
        while not self.process_events():
            #self.draw_frame()
            #self.draw_box()
            self.add_text("Highscores")
            self.get_highscores()
            self.add_return()
            self.add_button_text("Menu")
            pygame.display.flip()
    # draws the frame
    def draw_frame(self):
        pygame.draw.rect(self.screen, (212, 212, 212),
                         pygame.Rect((self.distance_border, self.distance_border),
                                     ((self.width - self.distance_border * 2), (self.height - self.distance_border * 2))))
    # draws a box for the highscores
    def draw_box(self):
        pygame.draw.rect(self.screen, (0,0,0), pygame.Rect((300, 126), (200, 250)))
    # adds a background
    def add_background(self):
        self.screen.blit(self.image, (0,0))
    # add text to the screen
    def add_text(self, text):
        font = pygame.font.SysFont("arial", (math.ceil(self.width/16)))
        caption = font.render(text, 1, (255, 255, 255))
        caption_position= caption.get_rect()
        self.screen.blit(caption, ((self.width/2 - math.ceil(caption_position[2]/2)), 50))
    # gets the highscores
    def get_highscores(self):
        mysql_con = mysql.mysql()
        result = mysql_con.select("SELECT * FROM players ORDER BY score DESC LIMIT 10")
        font = pygame.font.SysFont("arial", 25)
        x = 125
        for player in result:
            score = str((player['score']))
            score_result= font.render(score, 1 ,(255,255,255))
            score_position = score_result.get_rect()
            name = str((player['player_name']))
            name_result = font.render(name, 1, (255, 255, 255))
            name_position = name_result.get_rect()
            self.screen.blit(name_result, ((self.width/2 - 100), x))
            self.screen.blit(score_result, ((self.width/2 + 65), x))
            x = x + 25
        return player
    # add's the return button
    def add_return(self):
        pygame.draw.rect(self.screen, (48, 148, 51), pygame.Rect((self.width/2 - 50, math.ceil(7/8 * (self.height - self.distance_border * 2))), (100, 35)))

