import pygame
import math
import time
from modules import cards
from modules import sounds
from modules import settings

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
		self.start_width_card = (self.start - 20) + ( (self.width - self.card_width) / 2)

		self.draw_sidebar()
		self.draw_toolbar()
		self.draw_skip_turn()	
		#self.set_ship()
		#self.draw_steps_left()
		self.show_instructions()
		self.show_menu()
		#self.draw_normal_deck()

	def draw_sidebar(self):
		#pygame.draw.rect(self.Game.get_screen(), (self.sidebar_color), [self.start, 0, self.width, self.display_height])
		scr = pygame.image.load("assets/card_table.png")
		self.Game.get_screen().blit(scr, (self.start, 60))

	def draw_toolbar(self):
		width_block = self.toolbar_width_block
		heigth_block = self.toolbar_height_block

		top = pygame.image.load("assets/sidebar_up.png")
		button = pygame.image.load("assets/button.png")

		#pygame.draw.rect(self.Game.get_screen(), (self.toolbar_color), [self.start,0, self.width, self.toolbar_height])
		self.Game.get_screen().blit(top, (self.start, 0))

		y_coordinate = heigth_block/2
		x_coordinate = self.start + ((self.width - (width_block * 2)) / 4)
		while x_coordinate < self.display_width:
			self.Game.get_screen().blit(button, (x_coordinate, y_coordinate))
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
		button = self.Game.button({'image_path': 'assets/button_end_turn.png' ,'color': (211,211,211), 'start_x': self.start + 5, 'start_y': 65, 'width': self.width - 10, 'height': 40}, 'End turn')
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
		self.Game.get_screen().blit(card.get_wiki(), (self.start + 65, (320)))

		button = self.Game.button({'image_path': 'assets/button_use_card.png', 'color': (211,211,211), 'start_x': self.start + 65, 'start_y': 280 + 220, 'width': 127, 'height': 40}, 'Use Card')

		if(button):
			self.Turn.use_normal_card(card)


	def set_ship(self, ship):
		#ship = self.Turn.get_selected_ship()
		self.start = self.start + 20
		self.Game.set_font('inherit', (130,130,130), 'inherit')
		self.Game.draw_text(str(ship.get_name()), (self.start + 90, 120))
		image = pygame.image.load(ship.get_image())
		rotated_image = pygame.transform.rotate(image, 90)
		self.Game.get_screen().blit(rotated_image, (self.start, 120))		
		if(ship.check_if_dead()):
			self.Game.draw_text('This ship is Destroyed!', (self.start, 145))
		else:
			self.Game.draw_text('H: ' + str(ship.get_health()) + ' | M: ' + str(ship.get_moves()) + ' | A_L: ' + str(ship.get_attack_count()), (self.start, 140))
			self.Game.draw_text('O: ' + str(ship.get_offensive_range()) + ' | D: ' + str(ship.get_defensive_range()) + ' | A: ' + str(ship.get_damage()), (self.start, 160))
		self.Game.draw_text('___________________', (self.start, 170))

	def draw_attackable_ships(self, ships):
		selected_ship = self.Turn.get_selected_ship()
		if(selected_ship.check_if_dead()):
			return False
		elif(selected_ship.get_deactivated()):
			self.Game.draw_text('This ship is Deactivated!', (self.start, 250))
			return False


		y_start = 200

		for ship in ships:
			self.Game.set_font('inherit', (130,130,130), 'inherit')
			image = pygame.image.load(ship.get_image())
			rotated_image = pygame.transform.rotate(image, 90)
			self.Game.get_screen().blit(rotated_image, (self.start, y_start))			

			if ship.check_if_dead():
				self.Game.draw_text('Destroyed!', (self.start + 101, y_start))
			else:
				self.Game.draw_text('H: ' + str(ship.get_health()), (self.start + 95, y_start))	

			if(selected_ship.get_attack_count() > 0 and not ship.check_if_dead()):
				self.Game.set_font(12, (255,255,255), 'inherit')
				button = self.Game.button({'image_path': 'assets/button_attack.png', 'color': (211,211,211), 'start_x': self.start + 140, 'start_y': y_start, 'width': 60, 'height': 20}, 'Attack', True)

				if(button) and selected_ship.get_attack_count() > 0:
					damage = selected_ship.get_damage()
					ship.take_damage(damage)
					if ship.check_if_dead():
						self.Game.explosion(ship.x, ship.y)

					if(selected_ship.get_deactivate()):
						ship.set_deactivated()

					selected_ship.subtract_attack_count(1)
					if(self.Player.get_id() == 1):
						sounds.Sounds().attack_blue()
					else:
						sounds.Sounds().attack_red()

					time.sleep(0.15)			

			y_start += 30

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
					chk = settings.Settings(800, 575).play_sound()
					if chk == True:
						sounds.Sounds().click_sound()
						time.sleep(0.2)
					self.Menu.show()

class Sounds:
    def fire_shot(self):
        fire_shot = pygame.mixer.Sound("assets/sounds/fire_shot.wav")
        pygame.mixer.Sound.play(fire_shot)		
			

