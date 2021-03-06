"""Module containing ship classes"""
import pygame, time
from random import randint
from modules import sounds
from modules import animation
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

        self.deactivate = False
        self.deactivate = True

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

    def get_deactivate(self):
        return self.deactivate

    def set_deactivate(self):
        self.deactivate = True

    def unset_deactivate(self):
        self.deactivate = False

    def get_deactivated(self):
        return self.deactivated

    def set_deactivated(self):
        self.deactivated = True

    def unset_deactivated(self):
        self.deactivated = False

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
            if ship == self:
                continue

            full_ship = []
            if(ship.check_if_vertical()):
                for i in range(ship.get_size()):
                    full_ship.append((ship.x, p(ship.y, i)))
            else:
                for i in range(ship.get_size()):
                    full_ship.append((p(ship.x, i), ship.y))

            if(get_ship):
                ship_list.append({
                    'ship': ship,
                    'coords': full_ship
                    })
            else:
                ship_list.append(full_ship)

        return ship_list

    def get_ship(self):
        full_ship = []
        for i in range(self.get_size()):
            if(self.check_if_vertical()):
                full_ship.append((self.x, self.y + i))
            else:
                full_ship.append((self.x + i, self.y))

        return full_ship

    def check_colsion(self, player1, player2):

        ships_player_1 = self.get_ship_list_cords(player1, lambda x, y: x + y, False)
        ships_player_2 = self.get_ship_list_cords(player2, lambda x, y: x + y, False)

        ship = self.get_ship()

        for ship_player_1 in ships_player_1:
            if(set(ship_player_1).intersection(set(ship))):
                return True

        for ship_player_2 in ships_player_2:
            if(set(ship_player_2).intersection(set(ship))):
                return True 

        return False


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

        chkgame = sounds.sounds.check_gamesound()
        """Allows for movement on the grid"""
        # if select:
        #     print("You selected: " + self.name)
        #     print(str(self.move_ship) + " move(s) left for this ship.")
        if(Other_player):
            mines = Other_player.get_mines() 
        """Loops through until select returns false"""

        if self.move_ship > 0:
            if self.vertical == True and not self.dead and not self.deactivated:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        if chkgame == True:
                            sounds.Sounds().waves()
                        self.y -= 1
                        self.move_ship -= 1
                        self.direction = 1
                        if(self.check_colsion(player1, player2) or self.y < 1):
                            self.y +=1
                            self.move_ship += 1
                        time.sleep(0.15)                            
                    elif event.key == pygame.K_LEFT:
                        if chkgame == True:
                            sounds.Sounds().waves()
                        self.x -= 1
                        self.move_ship -= 1
                        self.direction = 2
                        if(self.check_colsion(player1, player2) or self.x < 1):
                            self.x += 1
                            self.move_ship += 1

                        time.sleep(0.15)                            
                    elif event.key == pygame.K_RIGHT:
                        if chkgame == True:
                            sounds.Sounds().waves()
                        self.x += 1
                        self.move_ship -= 1
                        self.direction = 3
                        if(self.check_colsion(player1, player2) or self.x > 20):
                            self.x -= 1
                            self.move_ship += 1

                        time.sleep(0.15)                            
                    elif event.key == pygame.K_DOWN:
                        if chkgame == True:
                            sounds.Sounds().waves()
                        self.y += 1
                        self.move_ship -= 1
                        self.direction = 4
                        if(self.check_colsion(player1, player2) or self.y > (21 - self.get_size())):
                            self.y -= 1
                            self.move_ship += 1

                        time.sleep(0.15)                            
                    elif event.key == pygame.K_l:
                        if player1.get_id() == 1:
                            if chkgame == True:
                                sounds.Sounds().turn_defensive_red()
                        else:
                            if chkgame == True:
                                sounds.Sounds().turn_defensive_blue()
                        self.move_ship -= 1
                        self.turn_ship()
                        if(self.check_colsion(player1, player2) or self.x > (21 - self.get_size())):
                            self.move_ship += 1
                            self.turn_ship()                        
                        time.sleep(0.15)
            elif self.vertical == False and not self.dead:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_l:
                        if player1.get_id() == 1:
                            if chkgame == True:
                                sounds.Sounds().turn_offensive_red()
                        else:
                            if chkgame == True:
                                sounds.Sounds().turn_offensive_blue()
                        self.move_ship -= 1
                        self.turn_ship()
                        if(self.check_colsion(player1, player2)):
                            self.move_ship += 1
                            self.turn_ship()

                        time.sleep(0.15)

            # check if ship hits a mine
            ship = self.get_ship()
            for mine in mines:
                if(set([mine]).intersection(set(ship))):
                    Other_player.delete_mine(mine)
                    dead = self.take_damage(1)
                    if(dead):
                        return dead
                    if chkgame == True:
                        sounds.Sounds().biem()

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
            return self.dead

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
        self.ship_number = 1
        if(color == 'red'):
            self.image = "assets/boats/BoatR_1.png"
        else:
            self.image = "assets/boats/BoatB_1.png"

        self.dead_image = "assets/boats/BoatG_1.png"
        self.dead       = False        
        self.deactivate = False
        self.deactivated = False
    def get_ship_number(self):
        return self.ship_number
    def reset(self):
        self.move_ship = 3
        self.offensive_range = 2
        self.defensive_range = 3
        self.damage = 1
        self.attack_count = 1
        self.unset_deactivate()
        self.unset_deactivated()

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
        self.ship_number = 2
        if(color == 'red'):
            self.image = "assets/boats/BoatR_2.png"        
        else:
            self.image = "assets/boats/BoatB_2.png"

        self.dead_image = "assets/boats/BoatG_2.png"
        self.dead       = False
        self.deactivate = False
        self.deactivated = False        

    def reset(self):
        self.move_ship = 2
        self.offensive_range = 3
        self.defensive_range = 4
        self.damage = 1
        self.attack_count = 1
        self.unset_deactivate()
        self.unset_deactivated()

class Amadea(MainShip):
    """Amadea & Merapi class"""
    def __init__(self, name, x, y, color = 'red'):
        super().__init__(name, x, y, color)
        self.name = name
        self.x = x - 100
        self.y = y
        self.health = 4
        self.size = 4
        self.move_ship = 1
        self.offensive_range = 4
        self.defensive_range = 5
        self.damage = 1
        self.attack_count = 1
        self.ship_number = 3
        if(color == 'red'):
            self.image = "assets/boats/BoatR_3.png"
        else:
            self.image = "assets/boats/BoatB_3.png"

        self.dead_image = "assets/boats/BoatG_3.png"
        self.dead       = False
        self.deactivate = False
        self.deactivated = False

    def reset(self):
        self.move_ship = 1
        self.offensive_range = 4
        self.defensive_range = 5
        self.damage = 1
        self.attack_count = 1
        self.unset_deactivate()
        self.unset_deactivated()

