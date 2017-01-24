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

Player1 = player.Player('Frits')
Player2 = player.Player('Henk')


""" display menu screen """
menu_screen = menu.Menu(20, 800, 575)
menu_screen.show()

Turn = player.Turn(Player2)
Turn.add_normal_card(cards.normal_card().Reinforced_hull())
Game = game.Game(800, 575)

field_size = 400

"""Start save logic for ship movement"""
ship_list_player1 = []
ship_list_player2 = []
count = 0

"""Instantiate ships player 1"""
Furgo = ships.Saltire("Furgo Saltire", 0, 0)
Silver = ships.Windsurf("Silver Whisper", 0, 0)
Windsurf = ships.Windsurf("Windsurf", 0, 0)
Merapi = ships.Amadea("Merapi", 0, 0)
ship_list_player1.extend([Furgo, Silver, Windsurf, Merapi])

"""Instantiate ships player 2"""
Santa = ships.Saltire("Santa Betiina", 0, 0)
Sea = ships.Windsurf("Sea Spirit", 0, 0)
Intensity = ships.Windsurf("Intensity", 0, 0)
Amadea = ships.Amadea("Amadea", 0, 0)
ship_list_player2.extend([Santa, Sea, Intensity, Amadea])

while not Game.events():
    # get the current player
    Player = Turn.player

    Game.get_screen().fill((235, 235, 235))

    # show the current player stats ( name and score )
    player_turn.Show(Game, Player)



    # show deck of current player
    deck.Show(Game, Player, Turn)

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
    for i in range(0, ship_list_player1[0].size):
        main_grid.Place_Square(ship_list_player1[0].x, 19 + i)
    for i in range(0, ship_list_player1[1].size):
        main_grid.Place_Square(ship_list_player1[1].x, 18 + i)
    for i in range(0, ship_list_player1[2].size):
        main_grid.Place_Square(ship_list_player1[2].x, 18 + i)
    for i in range(0, ship_list_player1[3].size):
        main_grid.Place_Square(ship_list_player1[3].x, 17 + i)

    """Start ship placement logic (WIP)"""
    if click:
        count += 1
        if count == 1:
            ship_list_player1[0].x = click[0]
            ship_list_player1[0].y = ship_list_player1[0].x
        elif count == 2:
            ship_list_player1[1].x = click[0]
        elif count == 3:
            ship_list_player1[2].x = click[0]
        elif count == 4:
            ship_list_player1[3].x = click[0]
        elif count == 5:
            pass

    """Start ship movement logic (WIP)"""
    press = pygame.key.get_pressed()
    if press[pygame.K_w]:
        ship_list_player1[0].y -= 1
        main_grid.Place_Square(ship_list_player1[0].x, ship_list_player1[0].y)

    # show sidebar
    sidebar.Show(Game, Player, menu_screen)
    Game.update()

# Turn = player.Turn(Player1)
