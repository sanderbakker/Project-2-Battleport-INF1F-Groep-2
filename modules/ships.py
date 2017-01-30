"""Module containing ship classes"""
import pygame, time
pygame.init()

class MainShip:
    """Main class containing the base values & methods"""
    def __init__(self, name, x, y, color = 'red'):
        self.name = name
        self.x = x
        self.y = y
        self.size = 0
        self.health = 0
        self.move_ship = 0
        self.select = False
        self.direction = 0
        self.image = ''

        self.offensive_range = 0
        self.defensive_range = 0
        self.damage = 1
        self.vertical = True

    def set_select(self):
        if(self.select):
            self.select = False
        else:
            self.select = True

    def unset_select(self):
        self.select = False

    def get_select(self): 
        return self.select

    def canGoHere(self, pos, player1, player2):
        for x in player1:

            if not x == self:
                if pos[0] == x.x:
                    if pos[1] >= x.y and pos[1] <= x.y + x.size - 1:
                        print("Could not move ship {} (pos {} {}) because its colliding with ship {} (pos {} {})".format(
                            self.name, self.x, self.y, x.name, x.x, x.y))
                        return False

        for x in player2:
            if not x == self:
                if pos[0] == x.x:
                    if pos[1] >= x.y and pos[1] <= x.y - x.size - 1:
                        print("Could not move ship {} (pos {} {}) because its colliding with ship {} (pos {} {})".format(
                            self.name, self.x, self.y, x.name, x.x, x.y))
                        return False
                # elif pos[1] >= x.y - x.size and pos[1] <= x.y:
                #    return False

        return True


    def movement(self, event, player1, player2):
        """Allows for movement on the grid"""
        # if select:
        #     print("You selected: " + self.name)
        #     print(str(self.move_ship) + " move(s) left for this ship.")

        """Loops through until select returns false"""

        if self.move_ship > 0:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.canGoHere((self.x, self.y - 1), player1, player2):
                    self.y -= 1
                    self.move_ship -= 1
                    self.direction = 1
                elif event.key == pygame.K_LEFT and self.canGoHere((self.x - 1, self.y), player1, player2):
                    self.x -= 1
                    self.move_ship -= 1
                    self.direction = 2
                    #self.select = False
                elif event.key == pygame.K_RIGHT and self.canGoHere((self.x + 1, self.y), player1, player2):
                    self.x += 1
                    self.move_ship -= 1
                    self.direction = 3
                    #self.select = False
                elif event.key == pygame.K_DOWN and self.canGoHere((self.x, self.y + 1), player1, player2):
                    self.y += 1
                    self.move_ship -= 1
                    self.direction = 4
                    #select = False
                elif event.key == pygame.K_l:
                    self.move_ship -= 1
                    self.turn_ship()
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

    def get_damage(self):
        return self.damage

    def add_damage(self, number):
        self.damage += number

    def get_image(self):
        return self.image

    def check_if_vertical(self):
        return self.vertical

    def turn_ship(self):
        if self.vertical:
            self.vertical = False
        else:
            self.vertical = True

class Saltire(MainShip):
    """Furgo Saltire & Santa Bettina class."""
    def __init__(self, name, x, y, color = 'red'):
        super().__init__(name, x, y, color)
        self.name = name
        self.x = x -100
        self.y = y
        self.health = 2
        self.size = 2
        self.move_ship = 100
        self.offensive_range = 2
        self.defensive_range = 3
        self.damage = 1
        if(color == 'red'):
            self.image = "assets/boats/BoatR_1.png"
        else:
            self.image = "assets/boats/BoatB_1.png"        

    def reset(self):
        self.move_ship = 3
        self.offensive_range = 2
        self.defensive_range = 3
        self.damage = 1

class Windsurf(MainShip):
    """Silver Whisper, Windsurf, Sea Spirit & Intensity class"""
    def __init__(self, name, x, y, color = 'red'):
        super().__init__(name, x, y, color)
        self.name = name
        self.x = x -100
        self.y = y
        self.health = 3
        self.size = 3
        self.move_ship = 100
        self.offensive_range = 3
        self.defensive_range = 4
        self.damage = 1
        if(color == 'red'):
            self.image = "assets/boats/BoatR_2.png"        
        else:
            self.image = "assets/boats/BoatB_2.png"

    def reset(self):
        self.move_ship = 100
        self.offensive_range = 3
        self.defensive_range = 4
        self.damage = 1

class Amadea(MainShip):
    """Amadea & Merapi class"""
    def __init__(self, name, x, y, color = 'red'):
        super().__init__(name, x, y, color)
        self.name = name
        self.x = x -100
        self.y = y
        self.health = 4
        self.size = 4
        self.move_ship = 1
        self.offensive_range = 4
        self.defensive_range = 5
        self.damage = 1
        if(color == 'red'):
            self.image = "assets/boats/BoatR_3.png"
        else:
            self.image = "assets/boats/BoatB_3.png"

    def reset(self):
        self.move_ship = 1
        self.offensive_range = 4
        self.defensive_range = 5
        self.damage = 1
