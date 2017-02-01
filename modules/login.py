import pygame
import sys
pygame.init()

class PlayerName():
    # inits the game
    def __init__(self):
        self.width = 800
        self.height = 575
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.name1 = ""
        self.Player1 = ""
        self.distance_border = 20
        self.draw_frame()
        self.name(400, 50)
    # draws a frame
    def draw_frame(self):
        pygame.draw.rect(self.screen, (204, 0, 0),
                         pygame.Rect((self.distance_border, self.distance_border),
                                     ((self.width - self.distance_border * 2),
                                      (self.height - self.distance_border * 2))))
    # gets the name of player 1 and blit's it on the screen
    def name(self, x, y):
        font = pygame.font.SysFont("Arial", 30)
        while not False:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if pygame.key.get_pressed():
                        if event.key == pygame.K_BACKSPACE:
                            self.name1 = self.name1[:-1]
                        elif event.key == pygame.K_ESCAPE:
                            self.name1 = ""
                        elif event.key == pygame.K_SPACE:
                            self.name1 = self.name1
                        elif event.key == pygame.K_RETURN:
                            self.Player1 = self.name1
                            return True
                        else:

                            self.name1 = self.name1 + event.unicode

                elif event.type == pygame.QUIT:
                    sys.exit()



            #self.screen.fill((212, 212, 212))
            username_1 = font.render(self.name1, 1, (255, 255, 255))
            username_1_position = username_1.get_rect()

            ask = font.render("Player 1, enter your username", 1 , (255,255,255))
            ask_position = ask.get_rect()
            pygame.draw.rect(self.screen, (233, 80, 80), pygame.Rect(self.width/2 - (x/2), self.height/2 - (y/2), 400, 50))
            self.screen.blit(ask, (self.width /2 -  (ask_position[2]/2), self.height/2 - (ask_position[3]/2) - 45))
            if username_1_position[2] <= (x - 15):
                self.screen.blit(username_1, (self.width / 2 - (username_1_position[2] / 2), self.height / 2 - (ask_position[3] / 2)))
            else:
                self.name1 = ""
                self.screen.blit(username_1,
                                 (self.width / 2 - (username_1_position[2] / 2), self.height / 2 - (ask_position[3] / 2)))
            pygame.display.flip()
    # returns the name of player 1
    def get_name(self):
        return self.Player1
# class for the name of player 2
class PlayerName2():
    def __init__(self):
        self.width = 800
        self.height = 575
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.name2 = ""
        self.Player2 = ""
        self.distance_border = 20
        self.draw_frame()
        self.name(400, 50)
    # draws a frame
    def draw_frame(self):
        pygame.draw.rect(self.screen, (51, 102, 204),
                         pygame.Rect((self.distance_border, self.distance_border),
                                     ((self.width - self.distance_border * 2),
                                      (self.height - self.distance_border * 2))))
    # gets the name of player 2 and blit's it on the screen
    def name(self, x, y):
        font = pygame.font.SysFont("arial", 30)
        while not False:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if pygame.key.get_pressed():
                        if event.key == pygame.K_BACKSPACE:
                            self.name2 = self.name2[:-1]
                        elif event.key == pygame.K_ESCAPE:
                            self.name2 = ""
                        elif event.key == pygame.K_SPACE:
                            self.name2 = self.name2
                        elif event.key == pygame.K_RETURN:
                            self.Player2 = self.name2
                            return True
                        else:
                            self.name2 = self.name2 + event.unicode
                elif event.type == pygame.QUIT:
                    sys.exit()

            username_2 = font.render(self.name2, 1, (255, 255, 255))
            username_2_positon = username_2.get_rect()

            ask = font.render("Player 2, enter your username", 1, (255, 255, 255))
            ask_position = ask.get_rect()
            pygame.draw.rect(self.screen, (51, 153, 255),
                             pygame.Rect(self.width / 2 - (x / 2), self.height / 2 - (y / 2), 400, 50))
            self.screen.blit(ask,
                             (self.width / 2 - (ask_position[2] / 2), self.height / 2 - (ask_position[3] / 2) - 45))
            if username_2_positon[2] <= (x - 15):
                self.screen.blit(username_2,
                                 (self.width / 2 - (username_2_positon[2] / 2), self.height / 2 - (ask_position[3] / 2)))
            else:
                self.name1 = ""
                self.screen.blit(username_2,
                                 (self.width / 2 - (username_2_positon[2] / 2), self.height / 2 - (ask_position[3] / 2)))
            pygame.display.flip()
    # returns the name of player 2
    def get_name(self):
        return self.Player2