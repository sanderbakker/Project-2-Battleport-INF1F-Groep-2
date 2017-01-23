import pygame
import math
WHITE = (255 ,255 ,255)
pygame.init()
width_screen = 800
height = 575

# Set height and width of the screen


class Menu:
    def __init__(self, distance_border, width_screen, height):
        self.distance_border = distance_border
        self.width_screen = width_screen
        self.height = height
        self.display = ((width_screen, height))
        self.screen = pygame.display.set_mode(self.display)
        self.check_menu = True
        self.game_quited = False
    def draw_frame(self):
        pygame.draw.rect(self.screen, (212, 212, 212),
                         pygame.Rect((self.distance_border, self.distance_border),
                                     ((self.width_screen - self.distance_border * 2), (self.height - self.distance_border * 2))))

    def add_logo(self):
        size_image = 280
        radius_image = 280/2

        img = pygame.image.load("logo.png")
        self.screen.blit(img, (self.width_screen/2 - radius_image, self.width_screen*(1/16)))

    def add_help(self, position):
        help_img = pygame.image.load("help.png")

        help_positon_x = self.width_screen - self.distance_border - position
        pygame.draw.rect(self.screen, (212, 212, 212),
                         pygame.Rect((help_positon_x, self.distance_border),(position, position)))
        self.screen.blit(help_img, (help_positon_x, self.distance_border))


    def draw_button(self, width_blocks, number_blocks):
        # calculates the remaining space after the blocks are added
        space_left_with_blocks = self.width_screen - (width_blocks * number_blocks)
        # space left after space_left_with_block - distance_border
        space_left = space_left_with_blocks - (self.distance_border * 2)
        # distance between border and first block
        distance_between = space_left / (number_blocks + 1)
        # space between the blocks
        space_between = width_blocks + distance_between
        # start point of the blocks
        start_point = distance_between + self.distance_border
        # end point of the blocks
        end_point = self.width_screen - int(start_point + width_blocks)
        x = start_point
        # draws the blocks on the screen
        while x <= end_point:
            pygame.draw.rect(self.screen, (48, 148, 51),
                             pygame.Rect((x, ((self.height - self.distance_border * 2) * (7 / 8))), (width_blocks, 35)))

            x = x + space_between
        #formula by Gerard Bakker
        x = start_point
        fonts = pygame.font.SysFont("arial", 20)
        start = fonts.render("Start", 1, (0, 0, 0))
        stop = fonts.render("Stop", 1, (0, 0, 0))
        highscores = fonts.render("Highscores", 1, (0, 0, 0))
        stop_position = (stop.get_rect())
        start_position = (start.get_rect())
        highscores_position = (highscores.get_rect())
        list_of_fonts = [start_position, stop_position, highscores_position]
        list_of_text = [stop, start, highscores]

        text_items = 0
        for position_items in range(number_blocks):
            self.screen.blit(list_of_text[text_items], (math.ceil(x + ((width_blocks - list_of_fonts[position_items][2]) /2)), ((self.height - self.distance_border * 2) * (7 / 8) + 5)))
            x = x + space_between
            position_items = position_items + 1
            text_items = text_items+ 1

    def program(self):
        while not self.process_events() or self.check_menu:
            menu = Menu(20, 800, 575)
            menu.draw_frame()
            menu.add_logo()
            menu.add_help(40)
            menu.draw_button(100, 3)
            pygame.display.flip()

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Give the signal to quit
                return True
            mouse = pygame.mouse.get_pos()
            #print(self.check_menu)
            if (mouse[1] >= 470 and mouse[1] <= 505):
                if (mouse[0] >= 135 and mouse[0] <= 235):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.check_menu = False
                        self.game_quited = True
                        return True
                elif (mouse[0] >= 350 and mouse[0] <= 450):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.check_menu = False
                        return True
                elif (mouse[0] >= 565 and mouse[0] <= 656):
                    pass

        return False

    def game_quited(self):
        return self.game_quited




Menu(20, 800, 575).program()