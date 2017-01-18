"""

Play the game by running this file.

"""

# Import the required modules 
import pygame, sys, pymysql

# Import all files stated in the __all__ variable in modules/__init__.py
from modules import *
import game

Player1 = player.Player('Frits')
Player2 = player.Player('Henk')

Game = game.Game(600, 600) 

while not Game.quit():
	Game.reset_font()
	Game.draw_text("Turn: " , (100,10))
	Game.set_font("inherit", (255, 0, 0))
	Game.draw_text(Player1.get_name(), (150, 10))

	opacity_grid = 400
	field = grid.Grid(Game.get_screen(), 20, 20, opacity_grid, 100)
	field.Place_Square(20, 20)

	Game.update()





