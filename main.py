"""

Play the game by running this file.

"""

# Import the required modules 
import pygame, sys, pymysql

# Import all files stated in the __all__ variable in modules/__init__.py
from modules import *

from view import *
import game

"""Sets window title"""
pygame.display.set_caption("Battleport")
ship_1_0 = 0
ship_1_1 = 0
ship_1_2 = 0
ship_1_3 = 0
ship_2_0 = 0
ship_2_1 = 0
ship_2_2 = 0
ship_2_3 = 0
Player1 = player.Player(login.PlayerName().get_name())
Player2 = player.Player(login.PlayerName2().get_name())


""" display menu screen """
menu_screen = menu.Menu(20, 800, 575)
menu_screen.show()
sidebar_screen = ''

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

while not Game.events():
    # get the current player    
    Player = Turn.player   

    Game.get_screen().fill((235, 235, 235))

    # show the current player stats ( name and score )
    player_turn.Show(Game, Player)

    # show sidebar
    sidebar_screen = sidebar.Show(Game, Player, Turn, menu_screen) 

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

    Game.set_grid(main_grid)
    click = Game.get_grid_click()

    """"Loads ships from array (WIP)"""
    for i in range(0, len(ship_list_player1)):
        for x in range(0, ship_list_player1[i].size):
            main_grid.Place_Square(ship_list_player1[i].x, ship_list_player1[i].y + x)

    for i in range(0, len(ship_list_player2)):
        for x in range(0, ship_list_player2[i].size):
            main_grid.Place_Square(ship_list_player2[i].x, ship_list_player2[i].y - x)

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
            if ship_1_0 < 3:
                if click[0] == ship_list_player1[0].x:
                    if click[1] == ship_list_player1[0].y:
                        ship_list_player1[0].y -= 1
                        ship_1_0 = ship_1_0 + 1
                        print(ship_list_player1[0].name + " moved forward!")
            elif ship_1_1 < 2:
                if click[0] == ship_list_player1[1].x:
                    if click[1] == ship_list_player1[1].y:
                        ship_list_player1[1].y -= 1
                        ship_1_1 = ship_1_1 + 1
                        print(ship_list_player1[1].name + " moved forward!")
            elif ship_1_2 < 2:
                if click[0] == ship_list_player1[2].x:
                    if click[1] == ship_list_player1[2].y:
                        ship_list_player1[2].y -= 1
                        ship_1_2 = ship_1_2 + 1
                        print(ship_list_player1[0].name + " moved forward!")
            for i in range(0, len(ship_list_player2)):
                if click[0] == ship_list_player2[i].x:
                    if click[1] == ship_list_player2[i].y:
                        ship_list_player2[i].y += 1
                        print(ship_list_player2[i].name + " moved forward!")

    sidebar_screen.show_instructions()
    Game.update()

# Turn = player.Turn(Player1)
