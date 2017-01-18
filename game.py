import pygame, sys, pymysql

class Game:
	def __init__(self, width, height):
		pygame.init()

		#lock framerate
		clock = pygame.time.Clock()
		clock.tick(60)

		#Screen parameters
		self.width = width
		self.height = height
		display = ((width, height))
		self.screen = pygame.display.set_mode(display)		

		#Font parameters
		self.font 		= "arial"
		self.font_size  = 20
		self.font_color = (255, 255, 255)

	#handle X button
	def quit(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
            # Give the signal to quit
				return True

		return False

	#updates the current screen
	def update(self):
		pygame.display.flip()

	def get_screen(self):
		return self.screen	

	"""
	 set the font parameters
	 font_size = int: size of the font
	 font_color = tuple: RGB colors. Example: (255, 0, 0)
	"""
	def set_font(self, font_size = "inherit", font_color = "inherit", font = "inherit"):
		if(font_size != "inherit"):
			self.font_size = font_size

		if(font_color != "inherit"):
			self.font_color = font_color

		if(font != "inherit"):
			self.font = font

	# resets font to the default values
	def reset_font(self):
		self.font 		= "arial"
		self.font_size  = 20
		self.font_color = (255, 255, 255)
	
	#get current font parameters	
	def get_font(self):
		return {'font_size': self.font_size, 'font_color': self.font_color, 'font': self.font}

	"""
	 write text to the screen
	 text = string: text you want to write
	 placement = tuple: placement of text. Example (100,100)
	"""
	def draw_text(self, text, placement):
		font_type = pygame.font.SysFont(self.font, self.font_size)
		text = font_type.render(text, 1, self.font_color)
		self.screen.blit(text, placement)
