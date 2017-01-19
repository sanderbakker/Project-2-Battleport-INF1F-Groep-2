import pygame, sys, pymysql

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
        self.font_color = (255, 255, 255)

        #Grid
        self.grid = 0
        self.grid_pos = 0

    #handle events
    def events(self):
        for event in pygame.event.get():
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

    # updates the current screen
    def update(self):
        pygame.display.flip()

    # get the current screen
    def get_screen(self):
        return self.screen  

    # set grid object
    def set_grid(self, grid):
        self.grid = grid 

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
        self.font_color = (255, 255, 255)
    
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
