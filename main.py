"""

Play the game by running this file.

"""

# Import the required modules 
import pygame, sys, pymysql, time

# Import all files stated in the __all__ variable in modules/__init__.py
from modules import *

from view import *
import game

"""Sets window title"""
pygame.display.set_caption("Battleport")
Player1 = player.Player(1, login.PlayerName().get_name())
Player2 = player.Player(2, login.PlayerName2().get_name())
Players = {1: Player1, 2: Player2}


""" display menu screen """
menu_screen = menu.Menu(20, 800, 575)
menu_screen.show()
sidebar_screen = ''
Mine_x = mine.Mine().get_random_x()
Mine_y = mine.Mine().get_random_y()
Game = game.Game(800, 575)
Game.set_menu(menu_screen)

Turn = player.Turn(Player1)
press = pygame.key.get_pressed()

field_size = 400

"""Start save logic for ship movement"""
ship_list_player1 = []
ship_list_player2 = []
count = 0
p1_count, p2_count, count = 0, 0, 0

"""Instantiate ships player 1"""
Furgo = ships.Saltire("Furgo Saltire", 0, 0)
Silver = ships.Windsurf("Silver Whisper", 0, 0)
Windsurf = ships.Windsurf("Windsurf", 0, 0)
Merapi = ships.Amadea("Merapi", 0, 0)
ship_list_player1.extend([Furgo, Silver, Windsurf, Merapi])
ship_list_player1[0].y, ship_list_player1[1].y, ship_list_player1[2].y, ship_list_player1[3].y = 19, 18, 18, 17

"""Instantiate ships player 2"""
Santa = ships.Saltire("Santa Betiina", 0, 0)
Sea = ships.Windsurf("Sea Spirit", 0, 0)
Intensity = ships.Windsurf("Intensity", 0, 0)
Amadea = ships.Amadea("Amadea", 0, 0)
ship_list_player2.extend([Santa, Sea, Intensity, Amadea])
ship_list_player2[0].y, ship_list_player2[1].y, ship_list_player2[2].y, ship_list_player2[3].y = 2, 3, 3, 4

Player1.set_ships(ship_list_player1)
Player2.set_ships(ship_list_player2)

while not Game.events():
    # get the current player    
    Player = Turn.player
    Turn.set_ships(ship_list_player1, ship_list_player2)

    Game.get_screen().fill((235, 235, 235))

    # show the current player stats ( name and score )
    player_turn.Show(Game, Player)

    # show sidebar
    sidebar_screen = sidebar.Show(Game, Players, Turn, menu_screen)

    # show deck of current player
    deck.Show(Game, Player, Turn, sidebar_screen)

    main_grid = grid.Grid({
        'screen': Game.get_screen(),
        'x_blocks': 20,
        'y_blocks': 20,
        'opacity_grid': field_size,
        'move_grid': 50,
        #'background_color': (0, 255, 0)
    })
    main_grid.Place_Mine(Mine_x, Mine_y)
    Game.set_grid(main_grid)
    click = Game.get_grid_click()

    """"Loads ships from array (WIP)"""
    for i in range(0, len(ship_list_player1)):
        for x in range(0, ship_list_player1[i].size):
            main_grid.Place_Player_1(ship_list_player1[i].x, ship_list_player1[i].y + x)

    for i in range(0, len(ship_list_player2)):
        for x in range(0, ship_list_player2[i].size):
            main_grid.Place_Player_2(ship_list_player2[i].x, ship_list_player2[i].y - x)

    """Start ship placement/game logic (WIP)"""
    if click:
        count += 1
        if count == 1:
            Turn = player.Turn(Player1)
            Turn.add_normal_card(cards.normal_card().get_random())
            Turn.add_normal_card(cards.normal_card().get_random())
        if count == 2:
            Turn = player.Turn(Player2)
            Turn.add_normal_card(cards.normal_card().get_random())
            Turn.add_normal_card(cards.normal_card().get_random())
        if count % 2 != 0 and count < 9:
            Turn = player.Turn(Player1)
            if click[0] == ship_list_player1[0].x:
                print("Invalid placement, try again.")
                count -= 1
            elif click[0] == ship_list_player1[1].x:
                print("Invalid placement, try again.")
                count -= 1
            elif click[0] == ship_list_player1[2].x:
                print("Invalid placement, try again.")
                count -= 1
            elif click[0] == ship_list_player1[3].x:
                print("Invalid placement, try again.")
                count -= 1
            else:
                ship_list_player1[p1_count].x = click[0]
                p1_count += 1

        elif count % 2 == 0 and count < 9:
            Turn = player.Turn(Player2)
            if click[0] == ship_list_player2[0].x:
                print("Invalid placement, try again.")
                count -= 1
            elif click[0] == ship_list_player2[1].x:
                print("Invalid placement, try again.")
                count -= 1
            elif click[0] == ship_list_player2[2].x:
                print("Invalid placement, try again.")
                count -= 1
            elif click[0] == ship_list_player2[3].x:
                print("Invalid placement, try again.")
                count -= 1
            else:
                ship_list_player2[p2_count].x = click[0]
                p2_count += 1
        elif count >= 9:
            """Ship movement logic"""
            for i in range(0, len(ship_list_player1)):
                if click[0] == ship_list_player1[i].x:
                    for ship_player1 in ship_list_player1:
                        ship_player1.unset_select()

                    ship_list_player1[i].set_select()
                    time.sleep(0.15)

                    """Collision testing (WIP)"""
                    for x in range(0, len(ship_list_player1)):
                        if ship_list_player1[i].x == ship_list_player1[0].x:
                            if ship_list_player1[i].direction == 2:
                                ship_list_player1[i].x += 1
                            if ship_list_player1[i].direction == 3:
                                ship_list_player1[i].x -= 1

    for ship_player1 in ship_list_player1:
        if ship_player1.get_select():
            sidebar_screen.set_ship(ship_player1)
            ship_player1.movement(Game.get_event())

    """Card logic"""
    """
    for i in range(0, len(ship_list_player1)):
        if click[0] == ship_list_player1[i].x:
            ship_list_player1[i].health -= 1
            print(str(ship_list_player1[i].health) + " lost 1HP!")
    """
    sidebar_screen.show_instructions()
    Game.update()

# Turn = player.Turn(Player1)
