"""Module containing ship classes"""
import pygame
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

    def damage(self):
        """Lowers health by 1"""
        self.health -= 1

    def placement(self):
        """Allows for placement on the grid"""
        pass

    def movement(self, select):
        """Allows for movement on the grid"""
        if select:
            print("You selected: " + self.name)
            while select:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP:
                            self.y -= 1
                        elif event.key == pygame.K_DOWN:
                            self.y += 1
                        elif event.key == pygame.K_q:
                            select = False

                self.select = select
                print("You selected: " + self.name)

        #if pygame.event.get().key == pygame.K_UP:
        #    self.x += 1
        #print("Hello World!")

    def position(self):
        """Turns ship 180 degrees, allowing for offensive and defensive positioning"""
        self.x = self.x - 1
        self.y = self.y

    def get_select(self):
        return self.select

    def get_health(self):
        return self.health


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
