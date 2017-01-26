import mysql

class highscores:
	def __init__(self):
		#self.get_highscores
		pass

	def get_highscores(self):
		mysql_con = mysql.mysql()
		result = mysql_con.select("SELECT * FROM players ORDER BY score DESC")
		return result



print(highscores().get_highscores())