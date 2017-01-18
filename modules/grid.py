import pygame
 
WHITE = (255, 255, 255)
# adds some colors 
pygame.init()
width_screen = 600
height = 600 
# Set height and width of the screen


display = ((width_screen, height))
screen = pygame.display.set_mode(display)
#make a display
class Grid: 
    def __init__ (self, x_blocks, y_blocks, opacity_grid):
        self.x = 0 
        self.y = 0
        self.x_blocks = x_blocks    
        self.y_blocks = y_blocks 
        self.opacity_grid = opacity_grid

    def Place_Circle(self, x_ship, y_ship, r_ship):
#first part of placing a "object" on the screen for the coordinates (1, 1)
       if x_ship <= 1: 
          if x_ship == 1 and y_ship == 1:  
                x_ship = ((x_ship * ((self.opacity_grid/self.x_blocks) / 2)))
                print(x_ship)
                y_ship = ((y_ship * ((self.opacity_grid/self.x_blocks) / 2)))
                print(y_ship)
                pygame.draw.circle(screen, (0, 255, 0),
                                       (int(x_ship), int(y_ship)), int(r_ship))
                 
#second part of placing a "object" on the screen for the coordinates (1, n) and (n, 1)
          elif x_ship == 1:  
                x_ship = ((x_ship * ((self.opacity_grid/self.x_blocks) / 2)))
                print(x_ship)
                y_ship = ((y_ship + (y_ship - 1)) * ((self.opacity_grid/self.x_blocks) / 2))
                print(y_ship)
                pygame.draw.circle(screen, (0, 255, 0),
                                       (int(x_ship), int(y_ship)), int(r_ship))
                

#last part of placing a "object" on the screen for the coordinates (n>1, n>1)            
       if x_ship > 1:
        
            x_ship = ((x_ship + (x_ship - 1)) * ((self.opacity_grid/self.x_blocks) / 2))
            print(x_ship)
            y_ship = ((y_ship + (y_ship - 1)) * ((self.opacity_grid/self.x_blocks) / 2))
            print(y_ship)
            #pygame.draw.circle(screen, (0, 255, 0),
            #                       (int(x_ship), int(y_ship)), int(r_ship))
            pygame.draw.rect(screen, (100,200,250), 
                                    pygame.Rect((int(x_ship), int(y_ship)), (20,20)))
                
        
        
 
    def grid(self, width):
#drawing the horizontal part of the grid 
        width = width/self.x_blocks 
        for l in range(int(width)):
            if self.x_blocks > 0:
                if self.x <= opacity_grid: 
                    pygame.draw.line(screen, WHITE, ((self.x + int(width)), self.y), (self.x + int(width), self.opacity_grid), (1))
                    self.x = self.x + int(width)
                    self.x_blocks = self.x_blocks - 1
                else:
                    pygame.draw.line(screen, WHITE, ((self.x + int(width)), self.y), (self.x + int(width), self.opacity_grid), (1))
                    self.x = self.x + int(width)
                    
#drawing the vertical part of the grid                 
        for m in range(int(width)):
            self.x = 0  
            if self.y_blocks > 0:
                if self.y <= opacity_grid:
                    pygame.draw.line(screen, WHITE, (self.x, (self.y + int(width))), (self.opacity_grid, self.y + int(width)), (1))
                    self.y = self.y + int(width)
                    self.y_blocks = self.y_blocks - 1 
                else:
                    pygame.draw.line(screen, WHITE, (self.x, (self.y + int(width))), (self.opacity_grid, self.y + int(width)), (1))
                    self.y = self.y + int(width)

    def Place_Square(self, rect_x, rect_y, number_blocks):
        middle_box = ((self.opacity_grid/number_blocks) / 2)    
        rect_x = ((rect_x * (middle_box)) + middle_box * (rect_x - 2))
        rect_y = ((rect_y * (middle_box)) + middle_box * (rect_y - 2))
        pygame.draw.rect(screen, (100,200,250), pygame.Rect((int(rect_x), int(rect_y)), (number_blocks, number_blocks)))
                
    
opacity_grid = 400
Grid(20, 20, 400).grid(int(opacity_grid))
#Grid(20, 20, opacity_grid).Place(2, 2, 5)



#class Ship:
#    def __init__(self, x, y, r): 
#        self.x = x
#        self.y = y
#        self.r = r
#    def draw(self, screen):
#        pygame.draw.circle(screen, (0, 255, 0),
#                           (int(self.x), int(self.y)), int(self.r))
    

    
                                               
Grid(20, 20, opacity_grid).Place_Square(7, 15, 20)

#filps the screen
pygame.display.flip()
