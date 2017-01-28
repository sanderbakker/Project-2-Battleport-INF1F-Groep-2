class Player:
	def __init__(self, id, name):
		self.id   = id
		self.Name = name
		self.Score = 0
		self.saved_normal_cards = []
		self.saved_special_cards = []
		self.saved_ships = []
		self.saved_mines = []

	def get_id(self):
		return self.id

	def set_id(self, id):
		self.id = id

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

	def save_normal_cards(self, cards):
		self.saved_normal_cards = cards

	def save_special_cards(self, cards):
		self.saved_special_cards = cards

	def get_normal_cards(self):
		return self.saved_normal_cards

	def get_special_cards(self):
		return self.saved_special_cards

	def set_ships(self, ships):
		self.saved_ships = ships

	def get_saved_ships(self):
		return self.saved_ships

	def set_mines(self, mines):
		self.saved_mines = mines

	def add_mine(self, mine):
		self.saved_mines.append(mine)

	def delete_mine(self):
		try:
			self.saved_mines.pop(0)
		except IndexError:
			return False

	def get_saved_mines(self):
		return self.saved_mines

class Turn:
	def __init__(self, player, other_player = None):
		self.normal_cards = []
		self.special_cards = []
		self.player = player
		self.other_player = other_player

		self.steps  = 2 

	def get_player(self):
		return self.player

	def set_player(self, player, other_player = None):
		self.player = player
		
		self.set_other_player(other_player)

	def get_other_player(self):
		return self.other_player

	def set_other_player(self, other_player):
		self.other_player = other_player

	# retrieve the normal cards of the player
	def get_normal_cards(self):
		self.normal_cards = self.player.get_normal_cards()
		return self.normal_cards 

	# add a normal card to the player deck
	def add_normal_card(self, card):
		self.normal_cards.append(card)
		self.player.save_normal_cards(self.normal_cards)				
		return self.normal_cards

	def remove_normal_card(self, card):
		self.normal_cards.remove(card)
		self.player.save_normal_cards(self.normal_cards)
		return self.normal_cards

	# retrieve the special cards of the player deck 
	def get_special_cards(self):
		self.special_cards = self.player.get_special_cards()
		return self.special_cards

	# add a special card to the player deck
	def add_special_cards(self, card):
		self.special_cards.append(card)
		self.player.save_special_cards(self.special_cards)				
		return self.special_cards

	def set_ships(self, ships_1, ships_2):
		if(self.player.get_id() == 2):
			return self.player.set_ships(ships_1)
		else:
			return self.player.set_ships(ships_2)

	def get_ships(self):
		return self.player.get_saved_ships()

	def get_selected_ship(self):
		ships = self.player.get_saved_ships()
		for ship in ships:
			if(ship.get_select()):
				return ship

		return None 

	def get_mines(self):
		return self.player.get_saved_mines()

	def add_mine(self, mine):
		self.player.add_mine(mine)

	def delete_mine(self):
		self.player.delete_mine()

	def use_normal_card(self, card):
		card.action(self)
		self.remove_normal_card(card)

	# get turn
	def get_turn(self):
		return self.Turn

	# set turn
	# Turn = bool
	def set_turn(player):
		self.Turn = Turn

	def take_step(self):
		self.steps = self.steps - 1

	def add_steps(self, steps):
		self.steps =  self.steps + steps

	def get_steps(self):
		return self.steps 



