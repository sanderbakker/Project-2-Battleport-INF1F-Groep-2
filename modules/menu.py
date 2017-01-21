import pygame 
WHITE = (255 ,255 ,255)
pygame.init()
width_screen = 400
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
        img = pygame.image.load("logo.png")
        screen.blit(img, ((self.distance_border + (width_screen/ 2), (self.distance_border + (width_screen - (width_screen - 100)) / 2))))

def process_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Give the signal to quit
            return True

    return False
distance_border = 20
def draw_button(width_blocks, number_blocks):
    space_left_with_blocks = width_screen - (width_blocks * number_blocks)
    space_left = space_left_with_blocks - (distance_border * 2)
    distance_between = space_left/(number_blocks+1)
    space_between = width_blocks + distance_between
    start_point = distance_between + distance_border
    end_point = width_screen - int(start_point + width_blocks)
    x = start_point

    while x <= end_point:
        pygame.draw.rect(screen, (48, 148, 51), pygame.Rect((x, 479), (width_blocks, 35)))
        x = x + space_between

def program():
    while not process_events():
        Menu(20).draw_frame()
        #Menu(20).add_logo()
        draw_button(50, 3)
        pygame.display.flip()


program()