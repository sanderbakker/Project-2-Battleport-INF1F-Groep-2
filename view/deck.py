import pygame

pygame.init()

class Show:
	def __init__(self, Game, Player, Turn, Sidebar = ''):
		self.Game 	= Game
		self.Player = Player
		self.Turn 	= Turn
		self.Sidebar= Sidebar

		self.display_height = Game.get_display_height()		

		self.card_width = 60
		self.card_height = 100
		self.card_spacing = 25
		self.margin_top = self.display_height - self.card_height - 10

		self.normal_cards = self.Turn.get_normal_cards()

		self.draw_cards(6, 25)

	def draw_cards(self, i, offset):
		for card in self.normal_cards:
			self.Game.blit(card.get_image(), (offset, self.margin_top))
			self.card_hover(offset, card)
			self.card_click(offset, card)

			if(card.get_clicked()):
				self.show_card_info(card)

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

	def card_hover(self, offset, card):
		mouse = pygame.mouse.get_pos()
		if mouse[0] >= offset and mouse[0] <= (offset + self.card_width):
			if mouse[1] >= self.margin_top and mouse[1] <= (self.margin_top + self.card_height):
				self.Sidebar.set_wiki(card)

	def show_card_info(self, card):
		self.Sidebar.set_wiki(card)

	def card_click(self, offset, card):
		mouse = pygame.mouse.get_pos()
		event = self.Game.get_event()
		if event.type == pygame.MOUSEBUTTONDOWN:
			if mouse[0] >= offset and mouse[0] <= (offset + self.card_width):
				if mouse[1] >= self.margin_top and mouse[1] <= (self.margin_top + self.card_height):
					for cards in self.normal_cards:
						cards.unset_clicked()

					card.set_clicked()







