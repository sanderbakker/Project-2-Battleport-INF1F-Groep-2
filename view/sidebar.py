import pygame

pygame.init()

class Show:
	def __init__(self, Game, Player, Menu):
		self.display_width = Game.get_display_width()
		self.display_height = Game.get_display_height()

		self.Game 	= Game
		self.Player = Player
		self.Menu 	= Menu

		""" sidebar """
		self.width = 250 #pixels
		self.start = Game.get_display_width() - self.width
		self.sidebar_color = (48,148,51)

		""" toolbar """
		self.toolbar_height = 60
		self.toolbar_color  = (42,129,44)

		self.card_width = 100
		self.card_height = 150
		self.start_width_card = self.start + ( (self.width - self.card_width) / 2)


		self.draw_sidebar()
		self.draw_toolbar()
		#self.draw_normal_deck()

	def draw_sidebar(self):
		pygame.draw.rect(self.Game.get_screen(), (self.sidebar_color), [self.start, 0, self.width, self.display_height])

	def draw_toolbar(self):
		pygame.draw.rect(self.Game.get_screen(), (self.toolbar_color), [self.start, 0, self.width, self.toolbar_height])

	def draw_normal_deck(self):
		self.Game.draw_text('Normal cards', ( (self.start_width_card - 15), 350))
		pygame.draw.rect(self.Game.get_screen(), (255,255,255), [ self.start_width_card, 380, self.card_width, self.card_height])
			

