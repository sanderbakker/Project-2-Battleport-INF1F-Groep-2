from modules import mysql
import pygame
import math
import sys
pygame.init()

class Highscores:
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
            self.draw_box()
            self.add_text("Highscores")
            self.get_highscores()
            pygame.display.flip()

    def draw_frame(self):
        pygame.draw.rect(self.screen, (212, 212, 212),
                         pygame.Rect((self.distance_border, self.distance_border),
                                     ((self.width - self.distance_border * 2), (self.height - self.distance_border * 2))))
    def draw_box(self):
        pygame.draw.rect(self.screen, (0,0,0), pygame.Rect((300, 126), (200, 250)))
    def add_background(self):
        self.screen.blit(self.image, (0,0))

    def add_text(self, text):
        font = pygame.font.SysFont("arial", (math.ceil(self.width/16)))
        caption = font.render(text, 1, (255, 255, 255))
        caption_position= caption.get_rect()
        self.screen.blit(caption, ((self.width/2 - math.ceil(caption_position[2]/2)), 50))

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


