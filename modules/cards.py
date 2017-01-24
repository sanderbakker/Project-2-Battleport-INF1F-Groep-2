import os, pygame

class card:
	def __init__(self):
		self.stack 		= ''
		self.card_type 	= ''
		self.velocity	= 0
		self.image 		= ''

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

	def set_image(self, image):
		self.image = pygame.image.load(os.path.dirname(os.path.abspath(__file__)) + '/../assets/defensive/' + image)

	def get_image(self):
		return self.image

class normal_card:
	def __init__(self):
		self.Card = card()
		# set the stack to normal
		self.Card.set_stack('normal')

	def set_card_offensive(self):
		self.Card.set_card_type('offensive')

	def set_card_defensive(self):
		self.Card.set_card_type('defensive')

	def set_card_help(self):
		self.Card.set_card_type('help')

	# offensive cards 
	def FMJ_upgrade():
		self.set_card_offensive()
		self.Card.set_velocity(2)

	def Rifling():
		self.set_card_offensive()
		self.Card.set_velocity(2)

	def Advanced_rifling():
		self.set_card_offensive()
		self.Card.set_velocity(2)

	def Naval_mine():
		self.set_card_offensive()
		self.Card.set_velocity(6)

	def EMP_upgrade():
		self.set_card_offensive()
		self.Card.set_velocity(4)

	# defenisve cards 
	def Reinforced_hull(self):
		self.set_card_defensive()
		self.Card.set_velocity(2)
		self.Card.set_image('Reinforced_hull.jpg')

		return self.Card

	def Sonar(self):
		self.set_card_defensive()
		self.Card.set_velocity(4)
		self.Card.set_image('Sonar.jpg')

	def Smokescreen(self):
		self.set_card_defensive()
		self.Card.set_velocity(2)
		self.Card.set_image('Smokescreen.jpg')

	def Sabotage(self):
		self.set_card_defensive()
		self.Card.set_velocity(2)
		self.Card.set_image('Sabotage.jpg')

	# help cards
	def Backup(self):
		self.set_card_help()
		self.Card.set_velocity(2)

	def Extra_fuel_II(self):
		self.set_card_help()
		self.Card.set_velocity(4)

	def Extra_fuel(self):
		self.set_card_help()
		self.Card.set_velocity(6)

	def Rally(self):
		self.set_card_help()
		self.Card.set_velocity(1)

	def Adreline_rush(self):
		self.set_card_help()
		self.Card.set_velocity(4)


class special_card:
	def __init__(card):
		# set the stack to special
		self.Card.set_stack('special')

	def set_card_special(self):
		set_card_type('special')

	def Repair(self):
		set_card_special()
		self.Card.set_velocity(2)

	def Flak_armor(self):
		set_card_special()
		self.Card.set_velocity(2)

	def Hack_intel(self):
		set_card_special()
		self.Card.set_velocity(1)

	def Far_sight(self):
		set_card_special()
		self.Card.set_velocity(1)

	def Aluminum_hull(self):
		set_card_special()
		self.Card.set_velocity(1)

	def Jack_sparrow(self):
		set_card_special()
		self.Card.set_velocity(1)




