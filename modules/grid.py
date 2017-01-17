import pygame
 
WHITE = (255, 255, 255)
pygame.init()
width_screen = 600
height = 600 



display = ((width_screen, height))
screen = pygame.display.set_mode(display)
class Grid: 
    def __init__ (self):
        self.x = 0 
        self.y = 0
        #self.width = 0
    #def Place(self, x, y):
        
 
    def grid(self, width, x_blocks, y_blocks):
        width = width/x_blocks 
        #while x < width:
        #    pygame.draw.line(screen, WHITE, ((x + 20), y), (x + 20, height), (1))
        #    x = x + 20 
        #while y < height:
        #    x = 0
        #    pygame.draw.line(screen, WHITE, (x, y + 20), (width, y + 20), (1))
        #    y = y + 20

        for l in range(int(width)):
            if x_blocks > 0:
                if self.x <= opacity_grid: 
                    pygame.draw.line(screen, WHITE, ((self.x + int(width)), self.y), (self.x + int(width), opacity_grid), (1))
                    self.x = self.x + int(width)
                    x_blocks = x_blocks - 1
                else:
                    pygame.draw.line(screen, WHITE, ((self.x + int(width)), self.y), (self.x + int(width), opacity_grid), (1))
                    self.x = self.x + int(width)
        for m in range(int(width)):
            self.x = 0  
            if y_blocks > 0:
                if self.y <= opacity_grid:
                    pygame.draw.line(screen, WHITE, (self.x, (self.y + int(width))), (opacity_grid, self.y + int(width)), (1))
                    self.y = self.y + int(width)
                    y_blocks = y_blocks - 1 
                else:
                    pygame.draw.line(screen, WHITE, (self.x, (self.y + int(width))), (opacity_grid, self.y + int(width)), (1))
                    self.y = self.y + int(width)
    
opacity_grid = 400
Grid().grid(int(opacity_grid), 20, 20)



class Ship:
    def __init__(self, x, y, r): 
        self.x = x
        self.y = y
        self.r = r
    def draw(self, screen):
        pygame.draw.circle(screen, (0, 255, 0),
                           (int(self.x), int(self.y)), int(self.r))


ship = Ship(10, 10, 5)
ship.draw(screen)
pygame.display.flip()





