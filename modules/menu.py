import pygame
import math
WHITE = (255 ,255 ,255)
pygame.init()
width_screen = 800
height = 575

# Set height and width of the screen
display = ((width_screen, height))
screen = pygame.display.set_mode(display)

class Menu:
    def __init__(self, distance_border):
        self.distance_border = distance_border

    def draw_frame(self):
        pygame.draw.rect(screen, (212, 212, 212),
                         pygame.Rect((self.distance_border, self.distance_border),
                                     ((width_screen - self.distance_border * 2), (height - self.distance_border * 2))))

    def add_logo(self):
        size_image = 280
        radius_image = 280/2

        img = pygame.image.load("logo.png")
        screen.blit(img, (width_screen/2 - radius_image, width_screen*(1/16)))

    def add_help(self, position):
        help_img = pygame.image.load("help.png")

        help_positon_x = width_screen - self.distance_border - position
        pygame.draw.rect(screen, (212, 212, 212),
                         pygame.Rect((help_positon_x, self.distance_border),(position, position)))
        screen.blit(help_img, (help_positon_x, self.distance_border))


    def draw_button(self, width_blocks, number_blocks):
        # calculates the remaining space after the blocks are added
        space_left_with_blocks = width_screen - (width_blocks * number_blocks)
        # space left after space_left_with_block - distance_border
        space_left = space_left_with_blocks - (self.distance_border * 2)
        # distance between border and first block
        distance_between = space_left / (number_blocks + 1)
        # space between the blocks
        space_between = width_blocks + distance_between
        # start point of the blocks
        start_point = distance_between + self.distance_border
        # end point of the blocks
        end_point = width_screen - int(start_point + width_blocks)
        x = start_point
        # draws the blocks on the screen
        while x <= end_point:
            pygame.draw.rect(screen, (48, 148, 51),
                             pygame.Rect((x, ((height - self.distance_border * 2) * (7 / 8))), (width_blocks, 35)))

            x = x + space_between
        #formula by Gerard Bakker
        x = start_point
        fonts = pygame.font.SysFont("arial", 20)
        start = fonts.render("Start", 1, (0, 0, 0))
        stop = fonts.render("Stop", 1, (0, 0, 0))
        highscores = fonts.render("Highscores", 1, (0, 0, 0))
        stop_position = (stop.get_rect())  # 34, 24
        start_position = (start.get_rect())
        highscores_position = (highscores.get_rect())
        screen.blit(start, (math.ceil(x + ((width_blocks - start_position[2]) /2)), ((height - self.distance_border * 2) * (7 / 8) + 5)))
        x = x + space_between
        screen.blit(stop, (math.ceil(x + ((width_blocks - stop_position[2]) /2)), ((height - self.distance_border * 2) * (7 / 8) + 5)))
        x = x + space_between
        screen.blit(highscores, (math.floor(x + ((width_blocks - highscores_position[2]) /2)), ((height - self.distance_border * 2) * (7 / 8) + 5)))
    def render_font(self, text):
        pass

    def menu_font(self):
        pass

def process_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Give the signal to quit
            return True

    return False
distance_border = 20


def program():
    while not process_events():
        Menu(20).draw_frame()
        Menu(20).add_logo()
        Menu(20).add_help(40)
        Menu(20).draw_button(100, 3)

        pygame.display.flip()


program()