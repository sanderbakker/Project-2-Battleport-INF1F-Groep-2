import os, pygame, random
from modules import mine

class card:
	def __init__(self):
		self.stack 		= ''
		self.card_type 	= ''
		self.velocity	= 0
		self.image 		= ''
		self.clicked = False 
		self.name 		= ''


	def action(self, Turn):
		return action(self, Turn)

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

	def set_wiki(self, wiki):
		self.wiki = pygame.image.load(os.path.dirname(os.path.abspath(__file__)) + '/../assets/wiki/' + wiki)

	def get_wiki(self):
		return self.wiki

	def set_name(self, name):
		self.name = name

	def get_name(self):
		return self.name

	def unset_clicked(self):
		self.clicked = False

	def set_clicked(self):
		self.clicked = True

	def get_clicked(self):
		return self.clicked 		

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
			'Rifling': 2,
			'Advanced_rifling': 2,
			'Naval_mine': 6,
			'EMP_upgrade': 4,
			'Reinforced_hull': 2,
			'Sonar': 4,
			#'Smokescreen': 2,
			#'Sabotage': 2,
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
		self.Card.set_wiki('FMJ_upgrade_wiki.jpg')
		self.Card.set_name('FMJ_upgrade')

		return self.Card

	def Rifling(self):
		self.set_card_offensive()
		self.Card.set_velocity(2)
		self.Card.set_image('Offensive/Rifling.jpg')
		self.Card.set_wiki('Rifling_wiki.jpg')
		self.Card.set_name('Rifling')

		return self.Card

	def Advanced_rifling(self):
		self.set_card_offensive()
		self.Card.set_velocity(2)
		self.Card.set_image('Offensive/Adv_rifling.png')
		self.Card.set_wiki('Adv_rifling_wiki.jpg')
		self.Card.set_name('Advanced_rifling')

		return self.Card

	def Naval_mine(self):
		self.set_card_offensive()
		self.Card.set_velocity(6)
		self.Card.set_image('Offensive/Naval_mine.jpg')
		self.Card.set_wiki('Naval_mine_wiki.jpg')
		self.Card.set_name('Naval_mine')

		return self.Card

	def EMP_upgrade(self):
		self.set_card_offensive()
		self.Card.set_velocity(4)
		self.Card.set_image('Offensive/EMP_upgrade.jpg')
		self.Card.set_wiki('EMP_upgrade_wiki.jpg')
		self.Card.set_name('EMP_upgrade')

		return self.Card

	# defenisve cards 
	def Reinforced_hull(self):
		self.set_card_defensive()
		self.Card.set_velocity(2)
		self.Card.set_image('Defensive/Reinforced_hull.jpg')
		self.Card.set_wiki('Reinforced_hull_wiki.jpg')
		self.Card.set_name('Reinforced_hull')

		return self.Card

	def Sonar(self):
		self.set_card_defensive()
		self.Card.set_velocity(4)
		self.Card.set_image('Defensive/Sonar.jpg')
		self.Card.set_wiki('Sonar_wiki.jpg')
		self.Card.set_name('Sonar')

		return self.Card

	def Smokescreen(self):
		self.set_card_defensive()
		self.Card.set_velocity(2)
		self.Card.set_image('Defensive/Smokescreen.jpg')
		self.Card.set_wiki('Smokescreen_wiki.jpg')
		self.Card.set_name('Smokescreen_wiki')

		return self.Card

	def Sabotage(self):
		self.set_card_defensive()
		self.Card.set_velocity(2)
		self.Card.set_image('Defensive/Sabotage.jpg')
		self.Card.set_wiki('Sabotage_wiki.jpg')
		self.Card.set_name('Sabotage_wiki')

		return self.Card

	# help cards
	def Backup(self):
		self.set_card_help()
		self.Card.set_velocity(2)
		self.Card.set_image('Help/Backup.jpg')
		self.Card.set_wiki('Backup_wiki.jpg')
		self.Card.set_name('Backup')

		return self.Card

	def Extra_fuel_II(self):
		self.set_card_help()
		self.Card.set_velocity(4)
		self.Card.set_image('Help/Extra_fuel_II.jpg')
		self.Card.set_wiki('Extra_fuel_2_wiki.jpg')
		self.Card.set_name('Extra_fuel_II')

		return self.Card

	def Extra_fuel(self):
		self.set_card_help()
		self.Card.set_velocity(6)
		self.Card.set_image('Help/Extra_fuel.jpg')
		self.Card.set_wiki('Extra_fuel_wiki.jpg')
		self.Card.set_name('Extra_fuel')

		return self.Card

	def Rally(self):
		self.set_card_help()
		self.Card.set_velocity(1)
		self.Card.set_image('Help/Rally.jpg')
		self.Card.set_wiki('Rally_wiki.jpg')
		self.Card.set_name('Rally')

		return self.Card

	def Adrenaline_rush(self):
		self.set_card_help()
		self.Card.set_velocity(4)
		self.Card.set_image('Help/Adrenaline_rush.jpg')
		self.Card.set_wiki('Adrenaline_rush_wiki.jpg')
		self.Card.set_name('Adrenaline_rush')

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

class action:
	def __init__(self, Card, Turn):
		self.Card = Card
		self.Turn = Turn
		
		method_name = 'use_' + Card.get_name()
		method = getattr(self, method_name)
		return method()

	def use_Extra_fuel(self):
		self.Turn.get_selected_ship().add_moves(1)

	def use_Extra_fuel_II(self):
		self.Turn.get_selected_ship().add_moves(2)

	def use_Reinforced_hull(self):
		self.Turn.get_selected_ship().add_health(1)

	def use_Backup(self):
		self.Turn.add_normal_card(normal_card().get_random())
		self.Turn.add_normal_card(normal_card().get_random())

	def use_Naval_mine(self):
		x = mine.Mine().get_random_x()
		y = mine.Mine().get_random_y()

		self.Turn.add_mine((x,y))
	
	def use_Sonar(self):
		self.Turn.get_other_player().delete_mine()

	def use_Rally(self):
		for ship in self.Turn.get_ships():
			ship.add_moves(1)

	def use_Rifling(self):
		self.Turn.get_selected_ship().add_range(1)

	def use_Advanced_rifling(self):
		self.Turn.get_selected_ship().add_range(2)

	def use_FMJ_upgrade(self):
		self.Turn.get_selected_ship().add_damage(1)






