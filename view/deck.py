import pygame

pygame.init()

class Show:
	def __init__(self, Game, Player, Turn):
		self.Game = Game
		self.Player = Player
		self.Turn = Turn

		self.card_width = 60
		self.card_height = 100
		self.card_spacing = 25

		self.normal_cards = self.Turn.get_normal_cards()
		self.display_height = Game.get_display_height()
		
		self.draw_cards(6, 25)

	def draw_cards(self, i, offset):
		for card in self.normal_cards:
			self.Game.draw_text(card,(offset, ( (self.display_height - self.card_height) - 10)))

			offset = offset + self.card_width + self.card_spacing
			i = i - 1

		self.draw_empty_card(i,offset)

	def draw_empty_card(self, i, offset):
		i = i - 1 

		if(i < 0):
			return 
		else:
			card = pygame.draw.rect(self.Game.get_screen(), (196, 196, 196), [ offset, ( (self.display_height - self.card_height) - 10), self.card_width, self.card_height])

		return self.draw_empty_card(i, (offset + self.card_width + self.card_spacing))
