import pygame
 
WHITE = (255, 255, 255)
pygame.init()
width_screen = 600
height = 600 



display = ((width_screen, height))
screen = pygame.display.set_mode(display)

def grid(width, x_blocks, y_blocks):
    y = 0 
    x = 0 
    width = width/x_blocks 


    for l in range(int(width)):
        if x_blocks > 0:
            if x <= opacity_grid: 
                pygame.draw.line(screen, WHITE, ((x + int(width)), y), (x + int(width), opacity_grid), (1))
                x = x + int(width)
                x_blocks = x_blocks - 1
            else:
                pygame.draw.line(screen, WHITE, ((x + int(width)), y), (x + int(width), opacity_grid), (1))
                x = x + int(width)
    for m in range(int(width)):
        x = 0  
        if y_blocks > 0:
            if y <= opacity_grid:
                pygame.draw.line(screen, WHITE, (x, (y + int(width))), (opacity_grid, y + int(width)), (1))
                y = y + int(width)
                y_blocks = y_blocks - 1 
            else:
                pygame.draw.line(screen, WHITE, (x, (y + int(width))), (opacity_grid, y + int(width)), (1))
                y = y + int(width)
    
opacity_grid = 400
grid(int(opacity_grid), 20, 20)
pygame.display.flip()


