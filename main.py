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
Game = game.Game(800, 575)

field_size = 400

"""Start save logic for ship movement"""
ship_list = []
if (len(ship_list)) > 0:
    print(str(ship_list))
"""End save logic for ship movement"""

Game.get_screen().fill((235, 235, 235))

while not Game.events():
    # get the current player
    Player = Turn.player
    #Game.get_screen().fill((0, 0, 0))

    # show the current player stats ( name and score )
    player_turn.Show(Game, Player)

    # show sidebar
    sidebar.Show(Game, Player)

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

    """Start ship placement logic"""
    FURGO = ships.Saltire("Furgo Saltire", 2, 0)

    if click:
        FURGO.x = main_grid.Place_Square(click[0], 19)
        FURGO.y = main_grid.Place_Square(click[0], 19 + FURGO.size)
        ship_list.append(FURGO)

    """End ship placement logic"""

    Game.update()

# Turn = player.Turn(Player1)
