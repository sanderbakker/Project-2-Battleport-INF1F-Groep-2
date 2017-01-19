"""

Play the game by running this file.

"""

# Import the required modules 
import pygame, sys, pymysql

# Import all files stated in the __all__ variable in modules/__init__.py
from modules import *

from view import *
import game

Player1 = player.Player('Frits')
Player2 = player.Player('Henk')

Turn = player.Turn(Player2)
Game = game.Game(800, 550)

field_size = 400 

while not Game.events():
	# get the current player
	Player = Turn.player

	# show the current player stats ( name and score )
	player_turn.Show(Game, Player)	

	main_grid = grid.Grid(Game.get_screen(), 20, 20, field_size, 50)
	main_grid.Place_Square(10, 20)
	Game.set_grid(main_grid)
	click = Game.get_grid_click()
	if(click):
		main_grid.Place_Square(click[0], click[1])

	Game.update()

	#Turn = player.Turn(Player1)





