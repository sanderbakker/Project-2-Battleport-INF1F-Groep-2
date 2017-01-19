import pygame

pygame.init()

class Show:
	def __init__(self, Game, Player):
		self.display_width = Game.get_display_width()
		self.display_height = Game.get_display_height()

		self.Game = Game
		self.Player = Player
		self.width = 250 #pixels
		self.start = Game.get_display_width() - self.width

		self.card_width = 100
		self.card_height = 150
		self.start_width_card = self.start + ( (self.width - self.card_width) / 2)


		self.draw_sidebar()
		#self.draw_normal_deck()

	def draw_sidebar(self):
		pygame.draw.rect(self.Game.get_screen(), (48,148,51), [self.start, 0, self.width, self.display_height])


	def draw_normal_deck(self):
		self.Game.draw_text('Normal cards', ( (self.start_width_card - 15), 350))
		pygame.draw.rect(self.Game.get_screen(), (255,255,255), [ self.start_width_card, 380, self.card_width, self.card_height])
			

