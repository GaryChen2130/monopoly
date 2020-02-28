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
	def __init__(self,num):
		self.player_num = num
		self.asset = []
		self.money = 15000
		self.pos = 0
		self.freeze_turn = 0

	def render(self,window,image,pos):
		window.blit(image,pos)
		return

	def Move(self,step,limit):
		self.pos += step
		while self.pos >= limit:
			self.money += 3000
			print('player' + str(self.player_num) + ' gets 3000 dollars! total money: ' + str(self.money))
			self.pos -= limit
		return

	def Transport(self,pos):
		self.pos = pos
		return


class Location:
	def __init__(self,image,pos,func,cost,extend_cost,tolls):
		self.image = image
		self.pos = pos
		self.func = func
		self.cost = cost
		self.extend_cost = extend_cost
		self.tolls = tolls
		self.owner = -1
		self.buildings = 0

	def render(self,surface):
		surface.blit(self.image,self.pos)
		return

