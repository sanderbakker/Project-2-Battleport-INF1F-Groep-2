import os, pygame, random

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
		self.image = pygame.image.load(os.path.dirname(os.path.abspath(__file__)) + '/../assets/' + image)

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

	# list containing all cards and velocity of the normal deck
	def __card_list(self):
		card_list = {
			'FMJ_upgrade': 2,
			'Rilfing': 2,
			'Advanced_rifling': 2,
			'Naval_mine': 6,
			'EMP_upgrade': 4,
			'Reinforced_hull': 2,
			'Sonar': 4,
			'Smokescreen': 2,
			'Sabotage': 2,
			'Backup': 2,
			'Extra_fuel_II': 4,
			'Extra_fuel': 2,
			'Rally': 1,
			'Adrenaline_rush': 4,
		}

		return card_list

	def get_random(self):
		card_list = self.__card_list()
		choice_list = []
		for name, velocity in card_list.items():
			for __ in range(velocity):
				choice_list.append(name)

		method = getattr(self, random.choice(choice_list))
		return method()

	# offensive cards 
	def FMJ_upgrade(self):
		self.set_card_offensive()
		self.Card.set_velocity(2)
		self.Card.set_image('Offensive/FMJ_upgrade.jpg')

		return self.Card

	def Rifling(self):
		self.set_card_offensive()
		self.Card.set_velocity(2)
		self.Card.set_image('Offensive/Rifling.jpg')

		return self.Card

	def Advanced_rifling(self):
		self.set_card_offensive()
		self.Card.set_velocity(2)
		self.Card.set_image('Offensive/Adv_rifling.png')

		return self.Card

	def Naval_mine(self):
		self.set_card_offensive()
		self.Card.set_velocity(6)
		self.Card.set_image('Offensive/Naval_mine.jpg')

		return self.Card

	def EMP_upgrade(self):
		self.set_card_offensive()
		self.Card.set_velocity(4)
		self.Card.set_image('Offensive/EMP_upgrade.jpg')

		return self.Card

	# defenisve cards 
	def Reinforced_hull(self):
		self.set_card_defensive()
		self.Card.set_velocity(2)
		self.Card.set_image('Defensive/Reinforced_hull.jpg')

		return self.Card

	def Sonar(self):
		self.set_card_defensive()
		self.Card.set_velocity(4)
		self.Card.set_image('Defensive/Sonar.jpg')

		return self.Card

	def Smokescreen(self):
		self.set_card_defensive()
		self.Card.set_velocity(2)
		self.Card.set_image('Defensive/Smokescreen.jpg')

		return self.Card

	def Sabotage(self):
		self.set_card_defensive()
		self.Card.set_velocity(2)
		self.Card.set_image('Defensive/Sabotage.jpg')

		return self.Card

	# help cards
	def Backup(self):
		self.set_card_help()
		self.Card.set_velocity(2)
		self.Card.set_image('Help/Backup.jpg')

		return self.Card

	def Extra_fuel_II(self):
		self.set_card_help()
		self.Card.set_velocity(4)
		self.Card.set_image('Help/Extra_fuel_II.jpg')

		return self.Card

	def Extra_fuel(self):
		self.set_card_help()
		self.Card.set_velocity(6)
		self.Card.set_image('Help/Extra_fuel.jpg')

		return self.Card

	def Rally(self):
		self.set_card_help()
		self.Card.set_velocity(1)
		self.Card.set_image('Help/Rally.jpg')

		return self.Card

	def Adrenaline_rush(self):
		self.set_card_help()
		self.Card.set_velocity(4)
		self.Card.set_image('Help/Adrenaline_rush.jpg')

		return self.Card


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




