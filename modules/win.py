import pygame, pymysql, sys
from modules import player
from modules import mysql
pygame.init()

class win_screen:
	def __init__(self, width, height, Winner = None, Loser = None):
		self.width = width
		self.height = height
		self.screen = pygame.display.set_mode((self.width, self.height))
		self.Winner = Winner
		self.Loser 	= Loser
		self.distance_border = 20
		self.show()
		self.draw_winner()

	def process_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				# Give the signal to quit
				return True
		return False

	def draw_frame(self):
		pygame.draw.rect(self.screen, (212, 212, 212),
						 pygame.Rect((self.distance_border, self.distance_border),
									 ((self.width - self.distance_border * 2),
									  (self.height - self.distance_border * 2))))
	def show(self):
		while not self.process_events():
			self.draw_frame()
			self.draw_winner()
			self.get_highscores()
			pygame.display.flip()

	def draw_winner(self):
		font_type = pygame.font.SysFont('Arial', 50)
		text = font_type.render(self.Winner.get_name() + ' WON!', 0, (0,0,0))
		text_width, text_height = font_type.size(self.Winner.get_name() + ' WON!')
		start_width = (self.width - text_width ) / 2
		start_height = (self.height - text_height) / 8
		self.screen.blit(text, (start_width, start_height))
	def get_name(self):
		return self.Winner

	def get_highscores(self):
		mysql_con = mysql.mysql()
		result = mysql_con.select("SELECT * FROM players ORDER BY score DESC LIMIT 10")
		font = pygame.font.SysFont("arial", 25)
		x = 125
		for player in result:
			score = str((player['score']))
			score_result = font.render(score, 1, (255, 255, 255))
			name = str((player['player_name']))
			name_result = font.render(name, 1, (48, 148, 51))
			self.screen.blit(name_result, ((self.width / 2 - 100), x))
			self.screen.blit(score_result, ((self.width / 2 + 65), x))
			x = x + 25
		return player

player1 = player.Player(1, "Sander")
player2 = player.Player(2, "Lennart")
win_screen(800, 575, player1, player2)