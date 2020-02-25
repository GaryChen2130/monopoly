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


class Player:
	def __init__(self,num,arrow_left,arrow_right,arrow_up,arrow_down):
		self.player_num = num
		self.image_left = arrow_left
		self.image_right = arrow_right
		self.image_up = arrow_up
		self.image_down = arrow_down
		self.asset = []
		self.money = 15000
		self.pos = 0

	def render(self,window,image,pos):
		window.blit(image,pos)
		return

	def Move(self,step,limit):
		self.pos += step
		print('pos:' + str(self.pos))
		while self.pos >= limit:
			self.pos -= limit
		return

