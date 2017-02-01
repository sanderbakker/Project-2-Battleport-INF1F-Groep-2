class Show:
	def __init__(self, Game, Player):	
		Game.reset_font()
		Game.draw_text("Turn: " , (150,10))
		if(Player.get_color() == 'red'):
			Game.set_font("inherit", (255, 0, 0))
		else:
			Game.set_font("inherit", (0, 0, 255))

		Game.draw_text(str(Player.get_name()), (200, 10))
		Game.reset_font()
