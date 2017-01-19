import pygame

pygame.init()

class Show:
	def __init__(self, Game, Player):
		self.Game = Game
		self.Player = Player

		self.card_width = 60
		self.card_height = 100
		self.card_spacing = 25

		self.display_height = Game.get_display_height()

		i = 6
		
		self.draw_empty_card(i, 25)

	def draw_empty_card(self, i, offset):
		i = i - 1 

		if(i < 0):
			return 
		else: 
			card = pygame.draw.rect(self.Game.get_screen(), (196, 196, 196), [ offset, ( (self.display_height - self.card_height) - 10), self.card_width, self.card_height])
			return self.draw_empty_card(i, (offset + self.card_width + self.card_spacing))
