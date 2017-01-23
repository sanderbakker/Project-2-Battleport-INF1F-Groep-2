class card:
	def __init__():
		self.stack 		= ''
		self.card_type 	= ''
		self.velocity	= 0

	def set_stack(self, stack):
		self.stack = stack

	def get_stack(self, stack):
		return self.stack

	def set_card_type(self, card_type):
		self.card_type = card_type

	def get_card_type(self):
		return self.card_type

	def set_velocity(self, velocity):
		self.velocity = velocity

	def get_velocity(self):
		return self.velocity


class normal_card:
	def __init__(card):
		# set the stack to normal
		card.set_stack('normal')

	def set_card_offensive(self):
		card.set_card_type('offensive')

	def set_card_defensive(self):
		card.set_card_type('defensive')

	def set_card_help(self)
		card.set_card_type('help')

	# offensive cards 
	def FMJ_upgrade():
		self.set_card_offensive()
		card.set_velocity(2)

	def Rifling():
		self.set_card_offensive()
		card.set_velocity(2)

	def Advanced_rifling():
		self.set_card_offensive()
		card.set_velocity(2)

	def Naval_mine():
		self.set_card_offensive()
		card.set_velocity(6)

	def EMP_upgrade():
		self.set_card_offensive()
		card.set_velocity(4)

	# defenisve cards 
	def Reinforced_hull(self):
		self.set_card_defensive():
		card.set_velocity(2)

	def Sonar(self):
		self.set_card_defensive()
		card.set_velocity(4)

	def Smokescreen(self):
		self.set_card_defensive()
		card.set_velocity(2)

	def Sabotage(self):
		self.set_card_defensive()
		card.set_velocity(2)

	# help cards
	def Backup(self):
		self.set_card_help()
		card.set_velocity(2)

	def Extra_fuel_II(self):
		self.set_card_help()
		card.set_velocity(4)

	def Extra_fuel(self):
		self.set_card_help()
		card.set_velocity(6)

	def Rally(self):
		self.set_card_help()
		card.set_velocity(1)

	def Adreline_rush(self):
		self.set_card_help()
		card.set_velocity(4)


class special_card:
	def __init__(card):
		# set the stack to special
		card.set_stack('special')

	def set_card_special(self):
		set_card_type('special')

	def Repair(self):
		set_card_special()
		card.set_velocity(2)

	def Flak_armor(self):
		set_card_special()
		card.set_velocity(2)

	def Hack_intel(self):
		set_card_special()
		card.set_velocity(1)

	def Far_sight(self):
		set_card_special()
		card.set_velocity(1)

	def Aluminum_hull(self):
		set_card_special()
		card.set_velocity(1)

	def Jack_sparrow(self)
		set_card_special()
		card.set_velocity(1)




