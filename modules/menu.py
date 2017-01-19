import pygame 
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
        img = pygame.image.load("logo.png")
        screen.blit(img, ((self.distance_border + (width_screen - 380) / 2), (self.distance_border + (width_screen - (width_screen - 100)) / 2)))

def process_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Give the signal to quit
            return True

    return False

def draw_button():
    pygame.draw.rect(screen, (48, 148, 51), pygame.Rect((103, 479), (100, 35)))
    pygame.draw.rect(screen, (48, 148, 51), pygame.Rect((356, 479), (100, 35)))
    pygame.draw.rect(screen, (48, 148, 51), pygame.Rect((610, 479), (100, 35)))
def program():
    while not process_events():
        Menu(20).draw_frame()
        Menu(20).add_logo()
        draw_button()
        pygame.display.flip()


program()