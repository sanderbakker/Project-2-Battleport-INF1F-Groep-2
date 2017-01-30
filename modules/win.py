import pygame, pymysql, sys

pygame.init()

class win_screen:
	def __init__(self, width, height, Winner = None, Loser = None):
		self.width = width
		self.height = height
		self.screen = pygame.display.set_mode((self.width, self.height))
		self.Winner = Winner
		self.Loser 	= Loser

		self.show()
		self.draw_winner()

	def process_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				# Give the signal to quit
				return True
		return False

	def show(self):
		while not self.process_events():
			self.screen.fill((235, 235, 235))
			self.draw_winner()
			pygame.display.flip()

	def draw_winner(self):
		font_type = pygame.font.SysFont('Arial', 50)
		text = font_type.render(self.Winner.get_name() + ' WON!', 0, (0,0,0))
		text_width, text_height = font_type.size(self.Winner.get_name() + ' WON!')
		start_width = (self.width - text_width ) / 2
		start_height = (self.height - text_height) / 4
		self.screen.blit(text, (start_width, start_height))
