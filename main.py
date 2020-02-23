import sys
import pygame
from pygame.locals import *

FPS = 60 # frame rate for updating game window
GAMECLOCK = pygame.time.Clock()
WINDOWWIDTH = 1600 # Width of game window
WINDOWHEIGHT = 900 # Height of game window
GAMETITLE = 'Monopoly' # Title of game window

HBOXNUM = 3
VBOXNUM = 3
BOXWIDTH = 125
BOXHEIGHT = 150

pygame.init()
window = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
pygame.display.set_caption(GAMETITLE)
window.fill((0,0,0))
font_obj = pygame.font.Font('GenYoGothicTW-Regular.ttf', 20)

# Define Color
WHITE = (255,255,255)
BLACK = (0,0,0)

# Game Images
IMAGES = {
	'arrest' : pygame.image.load('images/arrest.jpg'),
	'jail' : pygame.image.load('images/jail.jpg'),
	'confucius_temple' : pygame.image.load('images/confucius_temple.jpg'),
	'tainan_art_museum' : pygame.image.load('images/tainan_art_museum.jpg'),
	'chihkan_tower' : pygame.image.load('images/chihkan_tower.jpg'),
	'anping_castle' : pygame.image.load('images/anping_castle.jpg')
}

def main():
	game_map = SetGameMap(HBOXNUM,VBOXNUM)
	
	#########################################################################
	# Fill content into game map
	#########################################################################

	confucius_temple = pygame.transform.scale(IMAGES['confucius_temple'],(BOXWIDTH,BOXHEIGHT))
	confucius_temple_rect = confucius_temple.get_rect()
	confucius_temple_rect.left = game_map[1][0]
	confucius_temple_rect.top = game_map[1][1]
	window.blit(confucius_temple,confucius_temple_rect)

	jail = pygame.transform.scale(IMAGES['jail'],(BOXWIDTH,BOXHEIGHT))
	jail_rect = jail.get_rect()
	jail_rect.left = game_map[2][0]
	jail_rect.top = game_map[2][1]
	window.blit(jail,jail_rect)

	tainan_art_museum = pygame.transform.scale(IMAGES['tainan_art_museum'],(BOXWIDTH,BOXHEIGHT))
	tainan_art_museum_rect = tainan_art_museum.get_rect()
	tainan_art_museum_rect.left = game_map[3][0]
	tainan_art_museum_rect.top = game_map[3][1]
	window.blit(tainan_art_museum,tainan_art_museum_rect)

	chihkan_tower = pygame.transform.scale(IMAGES['chihkan_tower'],(BOXWIDTH,BOXHEIGHT))
	chihkan_tower_rect = chihkan_tower.get_rect()
	chihkan_tower_rect.left = game_map[5][0]
	chihkan_tower_rect.top = game_map[5][1]
	window.blit(chihkan_tower,chihkan_tower_rect)

	arrest = pygame.transform.scale(IMAGES['arrest'],(BOXWIDTH,BOXHEIGHT))
	arrest_rect = arrest.get_rect()
	arrest_rect.left = game_map[6][0]
	arrest_rect.top = game_map[6][1]
	window.blit(arrest,arrest_rect)

	anping_castle = pygame.transform.scale(IMAGES['anping_castle'],(BOXWIDTH,BOXHEIGHT))
	anping_castle_rect = arrest.get_rect()
	anping_castle_rect.left = game_map[7][0]
	anping_castle_rect.top = game_map[7][1]
	window.blit(anping_castle,anping_castle_rect)

	######################################################################### 

	while True:
		pygame.display.update()
		GAMECLOCK.tick(FPS)

		for event in pygame.event.get():
			if event.type == QUIT:
				terminate()


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
		game_map[i] = [start_left - i*BOXWIDTH,start_height,BOXWIDTH,BOXHEIGHT]

		pygame.draw.rect(window,WHITE,[end_left + i*BOXWIDTH,end_height,BOXWIDTH,BOXHEIGHT],3)
		text = font_obj.render(str(i + h_box + v_box - 2),True,WHITE,(0,0,0,0))
		text_rect = text.get_rect()
		text_rect.center = (end_left + i*BOXWIDTH + BOXWIDTH/2,end_height + BOXHEIGHT/2)
		window.blit(text,text_rect)
		game_map[i + h_box + v_box - 2] = [end_left + i*BOXWIDTH,end_height,BOXWIDTH,BOXHEIGHT]

	# Draw vertical boxes on map
	for i in range(1,v_box - 1):
		pygame.draw.rect(window,WHITE,[start_left,start_height - i*BOXHEIGHT,BOXWIDTH,BOXHEIGHT],3)
		text = font_obj.render(str(h_box*2 + (v_box - 2)*2 - i),True,WHITE,(0,0,0,0))
		text_rect = text.get_rect()
		text_rect.center = (start_left + BOXWIDTH/2,start_height - i*BOXHEIGHT + BOXHEIGHT/2)
		window.blit(text,text_rect)
		game_map[h_box*2 + (v_box - 2)*2 - i] = [start_left,start_height - i*BOXHEIGHT,BOXWIDTH,BOXHEIGHT]

		pygame.draw.rect(window,WHITE,[end_left,start_height - i*BOXHEIGHT,BOXWIDTH,BOXHEIGHT],3)
		text = font_obj.render(str(h_box + i - 1),True,WHITE,(0,0,0,0))
		text_rect = text.get_rect()
		text_rect.center = (end_left + BOXWIDTH/2,start_height - i*BOXHEIGHT + BOXHEIGHT/2)
		window.blit(text,text_rect)
		game_map[h_box + i - 1] = [end_left,start_height - i*BOXHEIGHT,BOXWIDTH,BOXHEIGHT]

	return game_map


def terminate():
	pygame.quit()
	sys.exit()


if __name__ == '__main__':
	main()