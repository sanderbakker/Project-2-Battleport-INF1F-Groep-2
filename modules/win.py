import math, pygame, pymysql, sys
from modules import player
from modules import mysql
from modules import menu

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

	def add_button_text(self, text):
		fonts = pygame.font.SysFont("arial", 20)
		entered_text = fonts.render(text, 1, (0, 0, 0))
		entered_text_position = entered_text.get_rect()
		x_position = self.width / 2 - math.floor(entered_text_position[2] / 2)
		y_position = math.ceil(7 / 8 * (self.height - self.distance_border * 2)) + 4
		self.screen.blit(entered_text, (x_position, y_position))

	def process_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			mouse = pygame.mouse.get_pos()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if mouse[0] > 350 and mouse[0] < 450:
					if mouse[1] > math.ceil(7 / 8 * (self.height - self.distance_border * 2)) and mouse[1] < math.ceil(
											7 / 8 * (self.height - self.distance_border * 2)) + 35:
						sys.exit()
		return False

	def draw_frame(self):
		pygame.draw.rect(self.screen, (212, 212, 212),
						 pygame.Rect((self.distance_border, self.distance_border),
									 ((self.width - self.distance_border * 2),
									  (self.height - self.distance_border * 2))))
	def show(self):
		self.add_or_update_highscores()
		while not self.process_events():
			self.draw_frame()
			self.draw_winner()
			self.get_highscores()
			self.add_return()
			self.add_button_text("Exit")
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
	def get_score(self):
		mysql_con = mysql.mysql()
		name = self.Winner.get_name()
		score = mysql_con.select('SELECT score FROM players WHERE player_name = "' + str(name) + '"')
		new_score = score[0].get("score") + 1
		return new_score

	def get_players(self):
		mysql_con = mysql.mysql()
		player_name = mysql_con.select(("SELECT player_name FROM players"))
		name_list = []
		for i in range(len(player_name)):
			name_list.append(player_name[i].get("player_name"))
		return name_list

	def update_highscores(self):
		score = int(self.get_score())
		name = self.Winner.get_name()
		mysql_con = mysql.mysql()
		result = mysql_con.update('UPDATE players SET score= "' + str(score) + '" WHERE player_name = "' + str(name) + '"')
		#('UPDATE players SET score= "' + str(score) + '" WHERE player_name = "' + str(name) + '"')

	def add_or_update_highscores(self):
		mysql_con = mysql.mysql()
		#check_player = mysql_con.select("SELECT player_name FROM players LIMIT 10")
		name = self.Winner.get_name()
		if name not in self.get_players():
			mysql_con.insert('INSERT INTO players(player_name, score) VALUES("' + str(name) + '", 1)')
		else:

			self.update_highscores()




	def add_return(self):
		pygame.draw.rect(self.screen, (48, 148, 51), pygame.Rect(
			(self.width / 2 - 50, math.ceil(7 / 8 * (self.height - self.distance_border * 2))), (100, 35)))

#player1 = player.Player(1, "Tim")
#player2 = player.Player(2, "Lennart")
#win_screen(800, 575, player1, player2)