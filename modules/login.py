import pygame
pygame.init()

class PlayerName():
    def __init__(self):
        self.width = 800
        self.height = 575
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.name1 = ""
        self.Player1 = ""
        self.name2 = ""
        self.Player2 = ""
    def name(self, x, y, count):

        #password = ""
        font = pygame.font.SysFont("arial", 30)

        while not False:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if pygame.key.get_pressed():
                        if event.key == pygame.K_BACKSPACE:
                            if count == 0:
                                self.name1 = self.name1[:-1]
                            else:
                                self.name2 = self.name2[:-1]
                        elif event.key == pygame.K_ESCAPE:
                            if count == 0:
                                self.name1 = ""
                            else:
                                self.name2 = ""
                        elif event.key == pygame.K_SPACE:
                            if count == 0:
                                self.name1 = self.name1
                            else:
                                self.name2 = self.name2
                        elif event.key == pygame.K_RETURN:
                            self.set_name()
                            if count < 1:
                                PlayerName().name(400,50, count = count + 1)

                                return True
                            else:
                                return True
                        #elif event.key == pygame.K_RETURN:
                        #    if event.key == pygame.K_BACKSPACE:
                        #        password = password[:-1]
                        #    elif event.key == pygame.K_SPACE:
                        #        password = password
                        #    else:
                        #        password = password + event.unicode
                        else:
                            if count == 0:
                                self.name1 = self.name1 + event.unicode
                            else:
                                self.name2 = self.name2 + event.unicode

                elif event.type == pygame.QUIT:
                    return True


            self.screen.fill((212, 212, 212))
            text = font.render(self.name1, 1, (255, 255, 255))
            text2 = font.render(self.name2, 1, (255,255,255))




            ask = font.render("Enter your username", 1 , (255,255,255))
            ask_position = ask.get_rect()
            pygame.draw.rect(self.screen, (100, 100, 100), pygame.Rect(self.width/2 - (x/2), self.height/2 - (y/2), 400, 50))
            self.screen.blit(text, (self.width /2 -  (ask_position[2]/2) - 80, self.height/2 - (ask_position[3]/2)))
            self.screen.blit(text2,
                             (self.width / 2 - (ask_position[2] / 2) - 80, self.height / 2 - (ask_position[3] / 2)))
            self.screen.blit(ask, (self.width /2 -  (ask_position[2]/2) - 80, self.height/2 - (ask_position[3]/2) - 45))
            #text2 = font.render(password, 1, (100, 100, 100))
            #screen.blit(text2,(100, 100))
            pygame.display.flip()
    def set_name(self):
        self.Player1 = self.name1
        self.Player2 = self.name2

        
PlayerName().name(400 , 50, 0)