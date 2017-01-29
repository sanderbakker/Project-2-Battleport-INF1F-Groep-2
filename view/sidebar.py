import pygame
import math
import time
from modules import cards

pygame.init()
class Show:
	def __init__(self, Game, Players, Turn, Menu):
		self.display_width = Game.get_display_width()
		self.display_height = Game.get_display_height()

		self.Game 	= Game
		self.Player = Turn.get_player()
		self.Players = Players
		if(self.Player.get_id() == 1):
			self.Other_player = Players[2]
		else:
			self.Other_player = Players[1]

		self.Menu 	= Menu
		self.Turn 	= Turn

		""" sidebar """
		self.width = 250 #pixels
		self.start = Game.get_display_width() - self.width
		self.sidebar_color = (48,148,51)

		""" toolbar """
		self.toolbar_height = 60
		self.toolbar_color  = (42,129,44)
		self.toolbar_width_block = 75
		self.toolbar_height_block = 30

		""" card """
		self.card_width = 100
		self.card_height = 150
		self.start_width_card = self.start + ( (self.width - self.card_width) / 2)

		self.draw_sidebar()
		self.draw_toolbar()
		self.draw_skip_turn()	
		#self.set_ship()
		#self.draw_steps_left()
		self.show_instructions()
		self.show_menu()
		#self.draw_normal_deck()

	def draw_sidebar(self):
		pygame.draw.rect(self.Game.get_screen(), (self.sidebar_color), [self.start, 0, self.width, self.display_height])

	def draw_toolbar(self):
		width_block = self.toolbar_width_block
		heigth_block = self.toolbar_height_block

		pygame.draw.rect(self.Game.get_screen(), (self.toolbar_color), [self.start, 0, self.width, self.toolbar_height])

		y_coordinate = heigth_block/2
		x_coordinate = self.start + ((self.width - (width_block * 2)) / 4)
		while x_coordinate < self.display_width:
			pygame.draw.rect(self.Game.get_screen(), (211, 211, 211), [x_coordinate, y_coordinate, width_block, heigth_block])
			x_coordinate = (x_coordinate + width_block + ((self.width - (width_block * 2)) /2))

		##TEXT
		x = self.start + ((self.width - (width_block * 2)) / 4)
		fonts = pygame.font.SysFont("arial", 20)
		menu = fonts.render("Menu", 1, (0, 0, 0))
		help = fonts.render("Help", 1, (0, 0, 0))
		menu_position = (menu.get_rect())
		help_position = (help.get_rect())

		list_of_fonts = [menu_position, help_position]
		list_of_text = [menu, help]
		text_items = 0

		for position_items in range(2):
			self.Game.get_screen().blit(list_of_text[text_items], (
			math.floor(x + ((width_block - list_of_fonts[position_items][2]) / 2)),
			((y_coordinate + 2))))
			x = (x + width_block + ((self.width - (width_block * 2)) /2))
			position_items = position_items + 1
			text_items = text_items + 1


	def draw_skip_turn(self):
		button = self.Game.button({'color': (211,211,211), 'start_x': self.start + 5, 'start_y': 65, 'width': self.width - 10, 'height': 40}, 'End turn')
		if(button):
			self.Turn.add_normal_card(cards.normal_card().get_random())

			# reset ship movement and powerups
			for ship in self.Turn.get_ships():
				ship.reset()

			self.Turn.set_player(self.Other_player, self.Player)
			time.sleep(0.25)

	def draw_steps_left(self):
		self.Game.set_font(25, (0,0,0))
		self.Game.draw_text('Moves left: ' + str(self.Turn.get_steps()), (self.start, 100))

	def show_instructions(self):

		mouse = pygame.mouse.get_pos()
		if mouse[1] >= 15 and mouse[1] <= 45:
			if mouse[0] >= 700 and mouse[0] <= 775:
				image = pygame.image.load("assets/help.jpg")
				self.Game.get_screen().blit(image, (0, 0))

	def draw_normal_deck(self):
		self.Game.draw_text('Normal cards', ( (self.start_width_card - 15), 350))
		pygame.draw.rect(self.Game.get_screen(), (255,255,255), [ self.start_width_card, 380, self.card_width, self.card_height])

	def set_wiki(self, card):
		self.Game.get_screen().blit(card.get_wiki(), (self.start + 65, (280)))

		button = self.Game.button({'color': (211,211,211), 'start_x': self.start + 65, 'start_y': 280 + 220, 'width': 127, 'height': 40}, 'Use Card')

		if(button):
			self.Turn.use_normal_card(card)


	def set_ship(self, ship):
		#ship = self.Turn.get_selected_ship()
		self.Game.set_font('inherit', (0,0,0), 'inherit')
		self.Game.draw_text(str(ship.get_name()), (self.start, 120))
		self.Game.draw_text('Health: ' + str(ship.get_health()) + ' | Moves left: ' + str(ship.get_moves()), (self.start, 140))
		self.Game.draw_text('O: ' + str(ship.get_offensive_range()) + ' | D: ' + str(ship.get_defensive_range()) + ' | A: ' + str(ship.get_damage()), (self.start, 160))

	def set_placing_ship(self, ship):
		if not ship:
			self.placing_ship = False
			return 

		self.Game.set_font('inherit', (0,0,0), 'inherit')
		self.Game.draw_text(ship.get_name(), (self.start + 80, 180))
		image = pygame.image.load(ship.get_image())
		self.Game.get_screen().blit(image, (self.start + 100, 200))
		self.placing_ship = True
			 									
	def show_menu(self):
		event = self.Game.get_event()
		mouse = pygame.mouse.get_pos()
		if mouse[1] >= 15 and mouse[1] <= 45:
			if mouse[0] >= 575 and mouse[0] <= 650:
				if event.type == pygame.MOUSEBUTTONDOWN:
					self.Menu.show()		
			

