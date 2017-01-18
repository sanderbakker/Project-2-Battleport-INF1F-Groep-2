class Player:
	def __init__(self, name):
		self.Name = name
		self.Score = 0

	# retrieves the players username.
	def get_name(self):
		return self.Name

	# retrieves the players score
	def get_score(self):
		return self.Score

	"""
	 number = int: value which will be added to the current score of the player
	 method = lambda: which determines what to do (add, substract, etc)
	 return = new score
	"""
	def __edit_score(self, number, method):
		if (isinstance(number, int)):
			self.Score = method(self.Score, number)
			return self.Score
		else:
			raise ValueError('editScore requires a int() as input')

	# add score to the current player. 
	def add_score(self, number):
		return self.__edit_score(number, lambda x, y: x + y)

	# substract score from the current player.
	def subtract_score(self, number): 
		return self.__edit_score(number, lambda x, y: x - y)


class Turn:
	def __init__(self, player):
		self.normalCards = []
		self.specialCards = []
		self.player = player		

	def get_player():
		return self.player

	# retrieve the normal cards of the player
	def get_normal_cards():
		return self.normalCards 

	# add a normal card to the player deck
	def add_normal_card(card):
		self.normalCards = self.normalCards.append(card)
		return self.normalCards

	# retrieve the special cards of the player deck 
	def get_special_cards():
		return self.specialCards

	# add a special card to the player deck
	def add_special_cards():
		self.specialCards = self.specialCards.append(card)
		return self.specialCards

	# get turn
	def get_turn(self):
		return self.Turn

	# set turn
	# Turn = bool
	def set_turn(player):
		self.Turn = Turn		


