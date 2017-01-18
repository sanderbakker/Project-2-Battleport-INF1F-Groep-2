"""

Play the game by running this file.

"""

# Import the required modules 
import pygame, sys, pymysql

# Import all files stated in the __all__ variable in modules/__init__.py
from modules import *

Player1 = player.Player('Test persoon')

print(Player1.get_name())

class Game:

	def __init__(self):
		pygame.init()
		width_screen = 600
		height = 600 

		display = ((width_screen, height))
		self.screen = pygame.display.set_mode(display)		

	def update(self):
		pygame.display.flip()

	def draw_name_player(self, player_name):
		test_font = pygame.font.SysFont("monospace", 15)
		score_text = test_font.render(player_name, 1, (0, 255, 0))
		self.screen.blit(score_text, (16, 16))

Game = Game()

while True: 
	Game.draw_name_player(Player1.get_name())

	opacity_grid = 400
	grid.Grid().grid(int(opacity_grid), 20, 20)

	Game.update()





