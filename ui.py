import pygame
from pygame.locals import *

class Button:
	def __init__(self,btn_up,btn_down,pos):
		self.image_up = btn_up
		self.image_down = btn_down
		self.pos = pos

	def isHover(self):
		pos_x, pos_y = self.pos
		mouse_x, mouse_y = pygame.mouse.get_pos()
		width, height = self.image_up.get_size()
		if (mouse_x >= pos_x) and (mouse_x <= pos_x + width) and (mouse_y >= pos_y) and (mouse_y <= pos_y + height): return True
		return False

	def render(self,window):
		if self.isHover():
			window.blit(self.image_down,self.pos)
		else:
			window.blit(self.image_up,self.pos)
		return
