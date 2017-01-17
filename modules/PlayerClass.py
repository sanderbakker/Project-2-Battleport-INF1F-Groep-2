class Player:
	def __init__(self, name):
		self.Name = name
		self.Score = 0

	# retrieves the players username.
	def getName(self):
		return self.Name

	# retrieves the players score
	def getScore(self):
		return self.Score

	# number = int value which will be added to the current score of the player
	# method = lambda which determines what to do (add, substract, etc)
	# return = new score
	def __editScore(self, number, method):
		if (isinstance(number, int)):
			self.Score = method(self.Score, number)
			return self.Score
		else:
			raise ValueError('editScore requires a int() as input')

	# add score to the current player. 
	def addScore(self, number):
		return self.__editScore(number, lambda x, y: x + y)

	# substract score from the current player.
	def substractScore(self, number): 
		return self.__editScore(number, lambda x,y: x - y)

