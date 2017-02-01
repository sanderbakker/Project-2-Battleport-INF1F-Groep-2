import pygame, sys, pymysql
from modules import sounds
import time

class Game:
    def __init__(self, width, height):
        pygame.init()

        #lock framerate
        clock = pygame.time.Clock()
        clock.tick(60)

        #Screen parameters
        self.width = width
        self.height = height
        display = ((width, height))
        self.screen = pygame.display.set_mode(display)      

        #Font parameters
        self.font       = "arial"
        self.font_size  = 20
        self.font_color = (124, 124, 124)

        #Grid
        self.grid = 0
        self.grid_pos = 0

    #handle events
    def events(self):
        for event in pygame.event.get():
            self.set_event(event)

            if event.type == pygame.QUIT:
                # Give the signal to quit
                return True

            #if grid exists, check if it is clicked, set grid_pos
            if(self.grid != 0):
                pos = self.grid.process_events(event)
                if(pos):
                    self.grid_pos = pos
                    return

        self.grid_pos = 0
        return False

    # 
    def set_event(self, event):
        self.event = event

    #
    def get_event(self):
        return self.event

    # updates the current screen
    def update(self):
        pygame.display.flip()

    # get the current screen
    def get_screen(self):
        return self.screen  

    # set grid object
    def set_grid(self, grid):
        self.grid = grid 

    # set menu object
    def set_menu(self, menu):
        self.Menu = menu

    def set_deck(self, deck):
        self.deck = deck

    def get_menu(self):
        return self.Menu

    def get_deck(self):
        return self.deck

    # get position of the grid if it's clicked
    def get_grid_click(self):
        return self.grid_pos

    # get the display height  
    def get_display_height(self):  
        return self.height

    # get the display width
    def get_display_width(self):
        return self.width

    """ 
    button generator 
    """
    def button(self, array, text = '', custom_font = None):
        start_x = array['start_x']
        start_y = array['start_y']

        width   = array['width']
        height  = array['height']

        color  = array['color']


        try:
            img = array['image_path']               
            image = pygame.image.load(img)
            self.get_screen().blit(image, (start_x, start_y))
        except KeyError:
            img = None
            pygame.draw.rect(self.get_screen(), color, [start_x, start_y, width, height])

        

        if not custom_font:
            self.set_font('inherit', (255,255,255), 'inherit')

        custom_font = pygame.font.SysFont(self.font, self.font_size)

        text_width, text_height = custom_font.size(text)
        start_text_width = start_x + (width - text_width) / 2
        start_text_height = start_y + (height - text_height) / 2

        self.draw_text(text, (start_text_width, start_text_height))

        self.reset_font()
        event = self.get_event()
        mouse = pygame.mouse.get_pos()
        if mouse[0] >= start_x and mouse[0] <= start_x + width:
            if mouse[1] >= start_y and mouse[1] <= start_y + height:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    sounds.Sounds().click_sound()
                    return True

        return False


    """
     set the font parameters
     font_size = int: size of the font
     font_color = tuple: RGB colors. Example: (255, 0, 0)
    """
    def set_font(self, font_size = "inherit", font_color = "inherit", font = "inherit"):
        if(font_size != "inherit"):
            self.font_size = font_size

        if(font_color != "inherit"):
            self.font_color = font_color

        if(font != "inherit"):
            self.font = font

    # resets font to the default values
    def reset_font(self):
        self.font       = "arial"
        self.font_size  = 20
        self.font_color = (124, 124, 124)
    
    #get current font parameters    
    def get_font(self):
        return {'font_size': self.font_size, 'font_color': self.font_color, 'font': self.font}

    """
     write text to the screen
     text = string: text you want to write
     placement = tuple: placement of text. Example (100,100)
    """
    def draw_text(self, text, placement):
        font_type = pygame.font.SysFont(self.font, self.font_size)
        text = font_type.render(text, 0, self.font_color)
        self.screen.blit(text, placement)


    """ blit something on the screen """
    def blit(self, obj, placement):
        self.screen.blit(obj, placement)


    def explosion_ship_1(self, x, y):
        list_loaded = [pygame.image.load("assets/effects/explosion/explosion_frame_0.png"),
                       pygame.image.load("assets/effects/explosion/explosion_frame_1.png"),
                       pygame.image.load("assets/effects/explosion/explosion_frame_2.png"),
                       pygame.image.load("assets/effects/explosion/explosion_frame_3.png"),
                       pygame.image.load("assets/effects/explosion/explosion_frame_4.png"),
                       pygame.image.load("assets/effects/explosion/explosion_frame_5.png"),
                       pygame.image.load("assets/effects/explosion/explosion_frame_6.png")]
        move_grid = 40
        opacity_grid = 400
        number_of_blocks = 20
        new_x = x * number_of_blocks + move_grid - number_of_blocks
        new_y = y * number_of_blocks + move_grid - number_of_blocks
        for animation in range(len(list_loaded)):
            screen = self.get_screen()
            screen.blit(list_loaded[animation], (new_x, new_y))
            time.sleep(0.12)
            pygame.display.flip()
        new_x_2 = x * number_of_blocks + move_grid - number_of_blocks
        new_y_2 = y * number_of_blocks + move_grid
        for animation in range(len(list_loaded)):
            screen = self.get_screen()
            screen.blit(list_loaded[animation], (new_x_2, new_y_2))
            time.sleep(0.12)
            pygame.display.flip()
    def explosion_ship_2(self, x, y):
        list_loaded = [pygame.image.load("assets/effects/explosion/explosion_frame_0.png"),
                       pygame.image.load("assets/effects/explosion/explosion_frame_1.png"),
                       pygame.image.load("assets/effects/explosion/explosion_frame_2.png"),
                       pygame.image.load("assets/effects/explosion/explosion_frame_3.png"),
                       pygame.image.load("assets/effects/explosion/explosion_frame_4.png"),
                       pygame.image.load("assets/effects/explosion/explosion_frame_5.png"),
                       pygame.image.load("assets/effects/explosion/explosion_frame_6.png")]
        move_grid = 40
        opacity_grid = 400
        number_of_blocks = 20
        new_x = x * number_of_blocks + move_grid - number_of_blocks
        new_y = y * number_of_blocks + move_grid - number_of_blocks
        for animation in range(len(list_loaded)):
            screen = self.get_screen()
            screen.blit(list_loaded[animation], (new_x, new_y))
            time.sleep(0.12)
            pygame.display.flip()
        new_x_3 = x * number_of_blocks + move_grid - number_of_blocks
        new_y_3 = y * number_of_blocks + move_grid + number_of_blocks
        for animation in range(len(list_loaded)):
            screen = self.get_screen()
            screen.blit(list_loaded[animation], (new_x_3, new_y_3))
            time.sleep(0.12)
            pygame.display.flip()
        new_x_2 = x * number_of_blocks + move_grid - number_of_blocks
        new_y_2 = y * number_of_blocks + move_grid
        for animation in range(len(list_loaded)):
            screen = self.get_screen()
            screen.blit(list_loaded[animation], (new_x_2, new_y_2))
            time.sleep(0.12)
            pygame.display.flip()
    def explosion_ship_3(self, x, y):
        list_loaded = [pygame.image.load("assets/effects/explosion/explosion_frame_0.png"),
                       pygame.image.load("assets/effects/explosion/explosion_frame_1.png"),
                       pygame.image.load("assets/effects/explosion/explosion_frame_2.png"),
                       pygame.image.load("assets/effects/explosion/explosion_frame_3.png"),
                       pygame.image.load("assets/effects/explosion/explosion_frame_4.png"),
                       pygame.image.load("assets/effects/explosion/explosion_frame_5.png"),
                       pygame.image.load("assets/effects/explosion/explosion_frame_6.png")]
        move_grid = 40
        opacity_grid = 400
        number_of_blocks = 20
        new_x = x * number_of_blocks + move_grid - number_of_blocks
        new_y = y * number_of_blocks + move_grid - number_of_blocks
        for animation in range(len(list_loaded)):
            screen = self.get_screen()
            screen.blit(list_loaded[animation], (new_x, new_y))
            time.sleep(0.12)
            pygame.display.flip()
        new_x_3 = x * number_of_blocks + move_grid - number_of_blocks
        new_y_3 = y * number_of_blocks + move_grid + number_of_blocks
        for animation in range(len(list_loaded)):
            screen = self.get_screen()
            screen.blit(list_loaded[animation], (new_x_3, new_y_3))
            time.sleep(0.12)
            pygame.display.flip()
        new_x_2 = x * number_of_blocks + move_grid - number_of_blocks
        new_y_2 = y * number_of_blocks + move_grid
        for animation in range(len(list_loaded)):
            screen = self.get_screen()
            screen.blit(list_loaded[animation], (new_x_2, new_y_2))
            time.sleep(0.12)
            pygame.display.flip()
        new_x_4 = x * number_of_blocks + move_grid - number_of_blocks
        new_y_4 = y * number_of_blocks + move_grid + (number_of_blocks * 2)
        for animation in range(len(list_loaded)):
            screen = self.get_screen()
            screen.blit(list_loaded[animation], (new_x_4, new_y_4))
            time.sleep(0.12)
            pygame.display.flip()