import sys
import pygame
from pygame.locals import *
from ui import *

FPS = 60 # frame rate for updating game window
GAMECLOCK = pygame.time.Clock()
WINDOWWIDTH = 1600 # Width of game window
WINDOWHEIGHT = 900 # Height of game window
GAMETITLE = 'Monopoly' # Title of game window

# Information of game map
HBOXNUM = 3
VBOXNUM = 3
BOXWIDTH = 125
BOXHEIGHT = 150

# Game setting
pygame.init()
window = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
pygame.display.set_caption(GAMETITLE)
window.fill((0,0,0))
font_obj = pygame.font.Font('GenYoGothicTW-Regular.ttf', 20)

# UI Setting
BTNWIDTH = 150
BTNHEIGHT = 150

# Define Color
WHITE = (255,255,255)
BLACK = (0,0,0)

# Game Images
IMAGES = {
	'start' : pygame.image.load('images/start.jpg'),
	'arrest' : pygame.image.load('images/arrest.jpg'),
	'jail' : pygame.image.load('images/jail.jpg'),
	'parking' : pygame.image.load('images/parking.jpg'),
	'confucius_temple' : pygame.image.load('images/confucius_temple.jpg'),
	'tainan_art_museum' : pygame.image.load('images/tainan_art_museum.jpg'),
	'chihkan_tower' : pygame.image.load('images/chihkan_tower.jpg'),
	'anping_castle' : pygame.image.load('images/anping_castle.jpg')
}

UI_IMAGES = {
	'go_btn_up' : pygame.image.load('images/go_btn_up.jpg').convert_alpha(),
	'go_btn_down' : pygame.image.load('images/go_btn_down.jpg').convert_alpha()
}


def main():
	game_map = SetGameMap(HBOXNUM,VBOXNUM) # Setup game map
	
	##################################################################################################################################################################################
	# Fill content into game map
	##################################################################################################################################################################################

	SetMapContent(pygame.transform.scale(IMAGES['start'],(BOXWIDTH,BOXHEIGHT)),game_map[0])
	SetMapContent(pygame.transform.scale(IMAGES['confucius_temple'],(BOXWIDTH,BOXHEIGHT)),game_map[1])
	SetMapContent(pygame.transform.scale(IMAGES['jail'],(BOXWIDTH,BOXHEIGHT)),game_map[2])
	SetMapContent(pygame.transform.scale(IMAGES['tainan_art_museum'],(BOXWIDTH,BOXHEIGHT)),game_map[3])
	SetMapContent(pygame.transform.scale(IMAGES['parking'],(BOXWIDTH,BOXHEIGHT)),game_map[4])
	SetMapContent(pygame.transform.scale(IMAGES['chihkan_tower'],(BOXWIDTH,BOXHEIGHT)),game_map[5])
	SetMapContent(pygame.transform.scale(IMAGES['arrest'],(BOXWIDTH,BOXHEIGHT)),game_map[6])
	SetMapContent(pygame.transform.scale(IMAGES['anping_castle'],(BOXWIDTH,BOXHEIGHT)),game_map[7])

	##################################################################################################################################################################################

	##################################################################################################################################################################################
	# Setup Game GUI
	##################################################################################################################################################################################

	ui_list = []
	go_btn = Button(pygame.transform.scale(UI_IMAGES['go_btn_up'],(BTNWIDTH,BTNHEIGHT)),pygame.transform.scale(UI_IMAGES['go_btn_down'],(BTNWIDTH,BTNHEIGHT)),(1350,700))
	ui_list.append(go_btn)

	##################################################################################################################################################################################

	##################################################################################################################################################################################
	# Game loop
	##################################################################################################################################################################################

	while True:
		DrawGUI(ui_list)

		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				if go_btn.isHover():
					print('button down')
			elif event.type == QUIT:
				terminate()

		pygame.display.update()
		GAMECLOCK.tick(FPS)

	##################################################################################################################################################################################


def SetGameMap(h_box,v_box):
	start_left = WINDOWWIDTH/2 + (h_box/2 - 1)*BOXWIDTH
	start_height = WINDOWHEIGHT/2 + (v_box/2 - 1)*BOXHEIGHT
	end_left = WINDOWWIDTH/2 - (h_box/2)*BOXWIDTH
	end_height = WINDOWHEIGHT/2 - (v_box/2)*BOXHEIGHT
	game_map = [None]*(h_box*2 + (v_box - 2)*2)

	# Draw horizontal boxes on map
	for i in range(h_box):
		pygame.draw.rect(window,WHITE,[start_left - i*BOXWIDTH,start_height,BOXWIDTH,BOXHEIGHT],3)
		text = font_obj.render(str(i),True,WHITE,(0,0,0,0))
		text_rect = text.get_rect()
		text_rect.center = (start_left - i*BOXWIDTH + BOXWIDTH/2,start_height + BOXHEIGHT/2)
		window.blit(text,text_rect)
		game_map[i] = [start_left - i*BOXWIDTH,start_height]

		pygame.draw.rect(window,WHITE,[end_left + i*BOXWIDTH,end_height,BOXWIDTH,BOXHEIGHT],3)
		text = font_obj.render(str(i + h_box + v_box - 2),True,WHITE,(0,0,0,0))
		text_rect = text.get_rect()
		text_rect.center = (end_left + i*BOXWIDTH + BOXWIDTH/2,end_height + BOXHEIGHT/2)
		window.blit(text,text_rect)
		game_map[i + h_box + v_box - 2] = [end_left + i*BOXWIDTH,end_height]

	# Draw vertical boxes on map
	for i in range(1,v_box - 1):
		pygame.draw.rect(window,WHITE,[start_left,start_height - i*BOXHEIGHT,BOXWIDTH,BOXHEIGHT],3)
		text = font_obj.render(str(h_box*2 + (v_box - 2)*2 - i),True,WHITE,(0,0,0,0))
		text_rect = text.get_rect()
		text_rect.center = (start_left + BOXWIDTH/2,start_height - i*BOXHEIGHT + BOXHEIGHT/2)
		window.blit(text,text_rect)
		game_map[h_box*2 + (v_box - 2)*2 - i] = [start_left,start_height - i*BOXHEIGHT]

		pygame.draw.rect(window,WHITE,[end_left,start_height - i*BOXHEIGHT,BOXWIDTH,BOXHEIGHT],3)
		text = font_obj.render(str(h_box + i - 1),True,WHITE,(0,0,0,0))
		text_rect = text.get_rect()
		text_rect.center = (end_left + BOXWIDTH/2,start_height - i*BOXHEIGHT + BOXHEIGHT/2)
		window.blit(text,text_rect)
		game_map[h_box + i - 1] = [end_left,start_height - i*BOXHEIGHT]

	return game_map


def SetMapContent(image,pos):
	rect = image.get_rect()
	rect.left = pos[0]
	rect.top = pos[1]
	window.blit(image,rect)
	return


def DrawGUI(ui_list):
	for ui in ui_list:
		ui.render(window)
	return


def terminate():
	pygame.quit()
	sys.exit()


if __name__ == '__main__':
	main()