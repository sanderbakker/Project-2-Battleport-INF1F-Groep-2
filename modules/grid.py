import pygame, math
import random
from modules import ships
WHITE = (124, 124, 124)
# adds some colors 
pygame.init()

class Grid: 
    def __init__ (self, options):
        screen = options['screen']

        self.screen = options['screen']
        self.number_of_blocks = options['x_blocks']
        self.x = 0
        self.y = 0
        self.x_blocks = options['x_blocks']    
        self.y_blocks = options['y_blocks']
        self.opacity_grid = options['opacity_grid']
        self.move_grid = options['move_grid']
        #self.random_x = random.randint(1 ,20)
        #self.random_y = random.randint(1, 20)
        self.ship_count0 = 0
        self.ship_count2 = 0
        self.ship_count3 = 0
        self.ship_count1 = 0
        try:
            background_color = options['background_color']
            self.set_grid_color(options['background_color'])
        except KeyError:
            pass


        self.draw_grid()

    def draw_grid(self):
        screen = self.screen
        #drawing the horizontal part of the grid 
        opacity_grid = self.opacity_grid + self.move_grid
        width = self.opacity_grid/self.x_blocks 
        pygame.draw.line(screen, WHITE, (self.move_grid, self.move_grid), (self.move_grid, opacity_grid), (1))
        pygame.draw.line(screen, WHITE, (self.move_grid, self.move_grid), (opacity_grid, self.move_grid), (1))
        for l in range(int(width)):
            if self.x_blocks > 0:
                if self.x <= opacity_grid + self.move_grid: 
                    pygame.draw.line(screen, WHITE, ((self.x + int(width) + self.move_grid), self.y + self.move_grid), (self.x + int(width) + self.move_grid, self.opacity_grid + self.move_grid), (1))
                    self.x = self.x + int(width)
                    self.x_blocks = self.x_blocks - 1
                #else:
                #    pygame.draw.line(screen, WHITE, ((self.x + int(width)), self.y + self.move_grid), (self.x + int(width), self.opacity_grid + self.move_grid), (1))
                #    self.x = self.x + int(width)
                 
#drawing the vertical part of the grid                 
        for m in range(int(width)):
            self.x = 0  
            if self.y_blocks > 0:
                if self.y <= opacity_grid + self.move_grid:
                    pygame.draw.line(screen, WHITE, (self.x + self.move_grid, (self.y + int(width + self.move_grid))), (self.opacity_grid + self.move_grid, self.y + int(width) + self.move_grid), (1))
                    self.y = self.y + int(width)
                    self.y_blocks = self.y_blocks - 1 
                #else:
                #    pygame.draw.line(screen, WHITE, (self.x + self.move_grid, (self.y + int(width))), (self.opacity_grid + self.move_grid, self.y + int(width)), (1))
                #    self.y = self.y + int(width)

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

         
    def Place_Player_1(self, ship_number, ship):
        screen = self.screen
        transparant = (235, 235, 235, 0)
        middle_box = ((self.opacity_grid/self.number_of_blocks) / 2)
        rect_x = ((ship.x * (middle_box)) + middle_box * (ship.x - 2)) + self.move_grid
        rect_y = ((ship.y * (middle_box)) + middle_box * (ship.y - 2)) + self.move_grid
        #rect = pygame.draw.rect(screen, (51, 102, 204),
        #                 pygame.Rect((int(rect_x), int(rect_y)), (self.number_of_blocks, self.number_of_blocks)))
        if ship_number == 0:
            while self.ship_count0 < 1:
                if ship.check_if_vertical() == False:
                    pygame.draw.rect(screen, transparant,
                                     pygame.Rect((int(rect_x) + 1, int(rect_y) + 1 ),
                                                 (ship.size * self.number_of_blocks - 1, self.number_of_blocks -1)))
                    image = pygame.image.load(ship.get_image())
                    new_image = pygame.transform.rotate(image, 90)
                    screen.blit(new_image, (rect_x, rect_y))
                    self.ship_count0 += 1
                else:
                    pygame.draw.rect(screen, transparant,
                                     pygame.Rect((int(rect_x) + 1, int(rect_y) + 1),
                                                 (self.number_of_blocks - 1, ship.size * self.number_of_blocks - 1)))
                    image = pygame.image.load(ship.get_image())
                    screen.blit(image, (rect_x, rect_y))
                    self.ship_count0 += 1
        elif ship_number == 1:
            while self.ship_count1 < 1:
                if ship.check_if_vertical() == False:
                    pygame.draw.rect(screen, transparant,
                                     pygame.Rect((int(rect_x) + 1, int(rect_y) + 1),
                                                 (ship.size * self.number_of_blocks - 1, self.number_of_blocks -1 )))
                    image = pygame.image.load(ship.get_image())
                    new_image = pygame.transform.rotate(image, 90)
                    screen.blit(new_image, (rect_x, rect_y))
                    self.ship_count1 += 1
                else:
                    pygame.draw.rect(screen, transparant,
                                     pygame.Rect((int(rect_x) + 1, int(rect_y) + 1),
                                                 (self.number_of_blocks- 1, ship.size *self.number_of_blocks -1 )))
                    image = pygame.image.load(ship.get_image())
                    screen.blit(image, (rect_x, rect_y))
                    self.ship_count1 += 1
        elif ship_number == 2:
            while self.ship_count2 < 1:
                if ship.check_if_vertical() == False:
                    pygame.draw.rect(screen, transparant,
                                     pygame.Rect((int(rect_x) +1, int(rect_y) + 1),
                                                 (ship.size * self.number_of_blocks - 1, self.number_of_blocks -1)))
                    image = pygame.image.load(ship.get_image())
                    new_image = pygame.transform.rotate(image, 90)
                    screen.blit(new_image, (rect_x, rect_y))
                    self.ship_count2 += 2
                else:
                    pygame.draw.rect(screen, transparant,
                                     pygame.Rect((int(rect_x) + 1, int(rect_y) + 1),
                                                 (self.number_of_blocks - 1, ship.size *self.number_of_blocks -1)))
                    image = pygame.image.load(ship.get_image())
                    screen.blit(image, (rect_x, rect_y))
                    self.ship_count2 += 2
        elif ship_number == 3:
            while self.ship_count3 < 1:
                if ship.check_if_vertical() == False:
                    pygame.draw.rect(screen, transparant,
                                     pygame.Rect((int(rect_x) + 1 , int(rect_y) + 1),
                                                 (ship.size * self.number_of_blocks -1 , self.number_of_blocks -1 )))
                    image = pygame.image.load(ship.get_image())
                    new_image = pygame.transform.rotate(image, 90)
                    screen.blit(new_image, (rect_x, rect_y))
                    self.ship_count3 += 1
                else:
                    pygame.draw.rect(screen, transparant,
                                     pygame.Rect((int(rect_x) + 1, int(rect_y) + 1),
                                                 (self.number_of_blocks - 1, ship.size * self.number_of_blocks - 1)))
                    image = pygame.image.load(ship.get_image())
                    screen.blit(image, (rect_x, rect_y))
                    self.ship_count3 += 1


    def Place_Mine(self, rect_x, rect_y):
        screen = self.screen

        middle_box = ((self.opacity_grid / self.number_of_blocks) / 2)
        rect_x = ((rect_x * (middle_box)) + middle_box * (rect_x - 2)) + self.move_grid
        rect_y = ((rect_y * (middle_box)) + middle_box * (rect_y - 2)) + self.move_grid
        pygame.draw.rect(screen, (235, 235, 235),
                         pygame.Rect((int(rect_x) + 1 , int(rect_y) + 1 ), (self.number_of_blocks - 1, self.number_of_blocks - 1)))
        image = pygame.image.load("assets/mine.png")
        screen.blit(image, (rect_x, rect_y))
    def Turn_Ship(self, rect_x, rect_y, ship_number):
        middle_box = ((self.opacity_grid / self.number_of_blocks) / 2)
        rect_x = ((rect_x * (middle_box)) + middle_box * (rect_x - 2)) + self.move_grid
        rect_y = ((rect_y * (middle_box)) + middle_box * (rect_y - 2)) + self.move_grid
        pygame.draw.rect(self.screen, (128, 128, 128),pygame.Rect( (rect_x, rect_y), (40, 20) ))

    def Place_Player_2(self, ship_number, ship):
        screen = self.screen
        transparant = (235, 235, 235, 0)
        middle_box = ((self.opacity_grid / self.number_of_blocks) / 2)
        rect_x = ((ship.x * (middle_box)) + middle_box * (ship.x - 2)) + self.move_grid
        rect_y = ((ship.y * (middle_box)) + middle_box * (ship.y - 2)) + self.move_grid

        if ship_number == 0:
            while self.ship_count0 < 1:
                if ship.check_if_vertical() == False:
                    pygame.draw.rect(screen, transparant,
                                     pygame.Rect((int(rect_x) + 1, int(rect_y) + 1),
                                                 (2*self.number_of_blocks - 1, self.number_of_blocks -1)))
                    image = pygame.image.load(ship.get_image())
                    new_image = pygame.transform.rotate(image, 90)
                    screen.blit(new_image, (rect_x, rect_y))
                    self.ship_count0 += 1
                else:
                    pygame.draw.rect(screen, transparant,
                                     pygame.Rect((int(rect_x)+ 1, int(rect_y) + 1),
                                                 (self.number_of_blocks - 1, 2*self.number_of_blocks -1)))
                    image = pygame.image.load(ship.get_image())
                    screen.blit(image, (rect_x, rect_y))
                    self.ship_count0 += 1
        elif ship_number == 1:
            while self.ship_count1 < 1:
                if ship.check_if_vertical() == False:
                    pygame.draw.rect(screen, transparant,
                                     pygame.Rect((int(rect_x) + 1, int(rect_y) + 1),
                                                 (3 * self.number_of_blocks -1 , self.number_of_blocks -1)))
                    image = pygame.image.load(ship.get_image())
                    new_image = pygame.transform.rotate(image, 90)
                    screen.blit(new_image, (rect_x, rect_y))
                    self.ship_count1 += 1
                else:
                    pygame.draw.rect(screen, transparant,
                                     pygame.Rect((int(rect_x) + 1, int(rect_y) + 1),
                                                 (self.number_of_blocks - 1, 3* self.number_of_blocks -1)))
                    image = pygame.image.load(ship.get_image())
                    screen.blit(image, (rect_x, rect_y))
                    self.ship_count1 += 1
        elif ship_number == 2:
            while self.ship_count2 < 1:
                if ship.check_if_vertical() == False:
                    pygame.draw.rect(screen, transparant,
                                     pygame.Rect((int(rect_x)+ 1 , int(rect_y)+ 1),
                                                 (3 * self.number_of_blocks -1 , self.number_of_blocks -1)))
                    image = pygame.image.load(ship.get_image())
                    new_image = pygame.transform.rotate(image, 90)
                    screen.blit(new_image, (rect_x, rect_y))
                    self.ship_count2 += 1
                else:
                    pygame.draw.rect(screen, transparant,
                                     pygame.Rect((int(rect_x)+ 1, int(rect_y)+ 1),
                                                 (self.number_of_blocks - 1, 3* self.number_of_blocks-1)))
                    image = pygame.image.load(ship.get_image())
                    screen.blit(image, (rect_x, rect_y))
                    self.ship_count2 += 1
        elif ship_number == 3:
            while self.ship_count3 < 1:
                if ship.check_if_vertical() == False:
                    pygame.draw.rect(screen, transparant,
                                     pygame.Rect((int(rect_x) + 1, int(rect_y) + 1),
                                                 (4 * self.number_of_blocks - 1, self.number_of_blocks- 1)))
                    image = pygame.image.load(ship.get_image())
                    new_image = pygame.transform.rotate(image, 90)
                    screen.blit(new_image, (rect_x, rect_y))
                    self.ship_count3 += 1
                else:
                    pygame.draw.rect(screen, transparant,
                                     pygame.Rect((int(rect_x)+ 1, int(rect_y) + 1),
                                                 (self.number_of_blocks - 1, 4 * self.number_of_blocks- 1)))
                    image = pygame.image.load(ship.get_image())
                    screen.blit(image, (rect_x, rect_y))
                    self.ship_count3 += 1

    def set_grid_color(self, color):
        screen = self.screen
        pygame.draw.rect(screen, (color), pygame.Rect((self.move_grid, (self.move_grid)), (self.opacity_grid, self.opacity_grid)))

    def process_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos
            if pos[0] > self.move_grid and pos[1] > self.move_grid:
                if pos[0] < self.move_grid + (self.opacity_grid) and pos[1] < self.move_grid + (self.opacity_grid):
                    newpos = (int(math.floor((pos[0] - self.move_grid) / 20) + 1), int(math.floor((pos[1] - self.move_grid)/ 20) + 1))
                    return newpos

        return False
    
    def get_random_x(self):
        return random.randint(1, 20)

    def get_random_y(self):
        return random.randint(1, 20)

    def reset_ship_counts(self):
        self.ship_count2 = 0
        self.ship_count1 = 0
        self.ship_count0 = 0
        self.ship_count3 = 0


    def return_ship(self):
        image = pygame.image.load("assets/boats/BoatB_3.png")
        return image
