"""Module containing ship classes"""
import pygame, time
from random import randint
pygame.init()
pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)

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
        self.dead_image = ''
        self.attack_count = 0

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

    def get_size(self):
        return self.size

    def canGoHere(self, pos, list_player1, list_player2):

        for ship in list_player1:
            if not ship == self:
                if self.vertical:
                    if pos[0] == ship.x:
                        if pos[1] >= ship.y - (self.get_size() - 1) and pos[1] <= ship.y + ship.size - 1:
                            return False
                else:
                    if pos[1] == ship.y:
                        if pos[0] >= ship.x - (self.get_size() - 1) and pos[0] <= ship.x + ship.size - 1:
                            print(
                                "Could not move ship {} (pos {} {}) because its colliding with ship {} (pos {} {})".format(
                                    self.name, self.x, self.y, ship.name, ship.x, ship.y))
                            return False

        for ship in list_player2:
            if not ship == self:
                if self.vertical:
                    if pos[0] == ship.x:
                        if pos[1] >= ship.y - (self.get_size() - 1) and pos[1] <= ship.y + ship.size - 1:
                            return False
                else:
                    if pos[1] == ship.y:
                        if pos[0] >= ship.x - (self.get_size() - 1) and pos[0] <= ship.x + ship.size - 1:
                            print(
                                "Could not move ship {} (pos {} {}) because its colliding with ship {} (pos {} {})".format(
                                    self.name, self.x, self.y, ship.name, ship.x, ship.y))
                            return False
                    elif pos[0] == ship.x:
                        if pos[1] >= ship.y - (self.get_size() - 1) and pos[0] <= ship.y + ship.size - 1:
                            print(
                                "Could not move ship {} (pos {} {}) because its colliding with ship {} (pos {} {})".format(
                                    self.name, self.x, self.y, ship.name, ship.x, ship.y))
                            return False

        return True

    def get_ship_list_cords(self, Player, p, get_ship = False):
        ship_list = []
        try:
            ships = Player.get_saved_ships()
        except AttributeError:
            ships = [Player]

        for ship in ships:

            full_ship = []
            for i in range(ship.get_size()):
                full_ship.append((ship.x, p(ship.y, i)))

            if(get_ship):
                ship_list.append({
                    'ship': ship,
                    'coords': full_ship
                    })
            else:
                ship_list.append(full_ship)

        return ship_list

    def get_ship(self, ship, p):
        full_ship = []
        for i in range(ship.get_size()):
            full_ship.append((ship.x, p(ship.y, i)))

        return full_ship

    def locate_enemy_ships(self, Turn, Enemy):
        Player = Turn.get_player()
        if self.check_if_vertical():
            ship_range = self.offensive_range
        else:
            ship_range = self.defensive_range

        enemy_ship_list = self.get_ship_list_cords(Enemy, lambda x, y: x + y, True)

        ship_range_cords = []

        for i in range(ship_range + 1):
            if(self.check_if_vertical()):
                # top
                ship_range_cords.append((self.x, self.y - i))
                # bottom
                ship_range_cords.append((self.x, (self.y + self.size) + i))    
            else:
                # top 
                ship_range_cords.append((self.x - i, self.y))
                # bottom
                ship_range_cords.append(((self.x + self.size) + i, self.y))

            for a in range(self.size):
                if(self.check_if_vertical()):
                    # left 
                    ship_range_cords.append((self.x - i, self.y + a))
                    # right
                    ship_range_cords.append((self.x + i, self.y + a))
                else:
                    # left 
                    ship_range_cords.append((self.x + a, self.y - i))
                    # right
                    ship_range_cords.append((self.x + a, self.y - i))              

        ships_in_range = []
        for enemy_ship in enemy_ship_list:
           if(set(enemy_ship['coords']).intersection(set(ship_range_cords))):
                ships_in_range.append(enemy_ship['ship'])

        return ships_in_range


    def movement(self, event, player1, player2, Other_player = None):
        """Allows for movement on the grid"""
        # if select:
        #     print("You selected: " + self.name)
        #     print(str(self.move_ship) + " move(s) left for this ship.")
        if(Other_player):
            mines = Other_player.get_mines() 
        """Loops through until select returns false"""

        if self.move_ship > 0:
            if self.vertical == True and not self.dead:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and self.canGoHere((self.x, self.y - 1), player1, player2):
                        Sounds().waves()
                        self.y -= 1
                        self.move_ship -= 1
                        self.direction = 1

                    elif event.key == pygame.K_LEFT and self.canGoHere((self.x - 1, self.y), player1, player2):
                        Sounds().waves()
                        self.x -= 1
                        self.move_ship -= 1
                        self.direction = 2
                        #self.select = False
                    elif event.key == pygame.K_RIGHT and self.canGoHere((self.x + 1, self.y), player1, player2):
                        Sounds().waves()
                        self.x += 1
                        self.move_ship -= 1
                        self.direction = 3
                        #self.select = False
                    elif event.key == pygame.K_DOWN and self.canGoHere((self.x, self.y + 1), player1, player2):
                        Sounds().waves()
                        self.y += 1
                        self.move_ship -= 1
                        self.direction = 4
                        #select = False
                    elif event.key == pygame.K_l:
                        Sounds().waves()
                        self.move_ship -= 1
                        self.turn_ship()


                    # check if ship hits a mine
                    ship = self.get_ship_list_cords(self, lambda x, y: x + y, True)                    
                    for mine in mines:
                        if(set([mine]).intersection(set(ship[0]['coords']))):
                            Other_player.delete_mine(mine)
                            ship[0]['ship'].take_damage(1)
                            print('biem')

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

    def take_damage(self, number):
        self.health -= number
        if(self.health <= 0):
            self.image = self.dead_image
            self.dead  = True

    def check_if_dead(self):
        return self.dead

    def add_attack_count(self, number):
        self.attack_count += number

    def subtract_attack_count(self, number):
        self.attack_count -= number

    def get_attack_count(self):
        return self.attack_count

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
        self.move_ship = 3
        self.offensive_range = 2
        self.defensive_range = 3
        self.damage = 1
        self.attack_count = 1
        if(color == 'red'):
            self.image = "assets/boats/BoatR_1.png"
        else:
            self.image = "assets/boats/BoatB_1.png"

        self.dead_image = "assets/boats/BoatG_1.png"
        self.dead       = False        

    def reset(self):
        self.move_ship = 300
        self.offensive_range = 2
        self.defensive_range = 3
        self.damage = 1
        self.attack_count = 1

class Windsurf(MainShip):
    """Silver Whisper, Windsurf, Sea Spirit & Intensity class"""
    def __init__(self, name, x, y, color = 'red'):
        super().__init__(name, x, y, color)
        self.name = name
        self.x = x - 100
        self.y = y
        self.health = 3
        self.size = 3
        self.move_ship = 2
        self.offensive_range = 3
        self.defensive_range = 4
        self.damage = 1
        self.attack_count = 1
        if(color == 'red'):
            self.image = "assets/boats/BoatR_2.png"        
        else:
            self.image = "assets/boats/BoatB_2.png"

        self.dead_image = "assets/boats/BoatG_2.png"
        self.dead       = False

    def reset(self):
        self.move_ship = 200
        self.offensive_range = 3
        self.defensive_range = 4
        self.damage = 1
        self.attack_count = 1

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
        self.attack_count = 1
        if(color == 'red'):
            self.image = "assets/boats/BoatR_3.png"
        else:
            self.image = "assets/boats/BoatB_3.png"

        self.dead_image = "assets/boats/BoatG_3.png"
        self.dead       = False

    def reset(self):
        self.move_ship = 100
        self.offensive_range = 4
        self.defensive_range = 5
        self.damage = 1
        self.attack_count = 1

class Sounds:
    def waves(self):
        waves = pygame.mixer.Sound("assets/sounds/waves.wav")
        pygame.mixer.Sound.play(waves)