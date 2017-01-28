"""Module containing ship classes"""
import pygame, time
pygame.init()


class MainShip:
    """Main class containing the base values & methods"""
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.size = 0
        self.health = 0
        self.move_ship = 0
        self.select = False
        self.direction = 0

        self.offensive_range = 0
        self.defensive_range = 0

    def damage(self):
        """Lowers health by 1"""
        self.health -= 1

    def set_select(self):
        if(self.select):
            self.select = False
        else:
            self.select = True

    def unset_select(self):
        self.select = False

    def get_select(self): 
        return self.select

    def movement(self, event):
        """Allows for movement on the grid"""
        # if select:
        #     print("You selected: " + self.name)
        #     print(str(self.move_ship) + " move(s) left for this ship.")

        """Loops through until select returns false"""

        if self.move_ship > 0:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.y -= 1
                    self.move_ship -= 1
                    self.direction = 1
                elif event.key == pygame.K_LEFT:
                    self.x -= 1
                    self.move_ship -= 1
                    self.direction = 2
                    #self.select = False
                elif event.key == pygame.K_RIGHT:
                    self.x += 1
                    self.move_ship -= 1
                    self.direction = 3
                    #self.select = False
                elif event.key == pygame.K_DOWN:
                    self.y += 1
                    self.move_ship -= 1
                    self.direction = 4
                    #select = False


                time.sleep(0.15)

    def position(self):
        """Turns ship 180 degrees, allowing for offensive and defensive positioning"""
        self.x = self.x - 1
        self.y = self.y

    def get_health(self):
        return self.health

    def add_health(self, health):
        self.health += health

    def get_moves(self):
        return self.move_ship

    def add_moves(self, moves):
        self.move_ship += moves

    def get_name(self):
        return self.name

    def get_offensive_range(self):
        return self.offensive_range

    def add_offensive_range(self, number):
        self.offensive_range += number

    def get_defensive_range(self):
        return self.defensive_range

    def add_defensive_range(self, number):
        self.defensive_range += number

    def add_range(self, number):
        self.add_offensive_range(number)
        self.add_defensive_range(number) 

class Saltire(MainShip):
    """Furgo Saltire & Santa Bettina class."""
    def __init__(self, name, x, y):
        super().__init__(name, x, y)
        self.name = name
        self.x = y
        self.y = y
        self.health = 2
        self.size = 2
        self.move_ship = 3
        self.offensive_range = 2
        self.defensive_range = 3

class Windsurf(MainShip):
    """Silver Whisper, Windsurf, Sea Spirit & Intensity class"""
    def __init__(self, name, x, y):
        super().__init__(name, x, y)
        self.name = name
        self.x = x
        self.y = y
        self.health = 3
        self.size = 3
        self.move_ship = 2
        self.offensive_range = 2
        self.defensive_range = 3

class Amadea(MainShip):
    """Amadea & Merapi class"""
    def __init__(self, name, x, y):
        super().__init__(name, x, y)
        self.name = name
        self.x = x
        self.y = y
        self.health = 4
        self.size = 4
        self.move_ship = 1
        self.offensive_range = 4
        self.defensive_range = 5
