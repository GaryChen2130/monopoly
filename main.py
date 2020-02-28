import sys
import random
import pygame
from pygame.locals import *
from game_class import *

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
font_obj = pygame.font.Font('GenYoGothicTW-Regular.ttf', 20)
JAIL_POS = 2
BUILDLIMIT = 4

# UI Size
BTNWIDTH = 150
BTNHEIGHT = 150
ARROWWIDTH = 50
ARROWHEIGHT = 125
DICEWIDTH = 100
DICEHEIGHT = 100
BUILDINGWIDTH = 30
BUILDINGHEIGHT = 30
BLANKWIDTH = 60
BLANKHEIGHT = 60

# Define Color
WHITE = (255,255,255)
BLACK = (0,0,0)

# Game Images
IMAGES = {
	'start' : pygame.transform.scale(pygame.image.load('images/start.jpg'),(BOXWIDTH,BOXHEIGHT)),
	'arrest' : pygame.transform.scale(pygame.image.load('images/arrest.jpg'),(BOXWIDTH,BOXHEIGHT)),
	'jail' : pygame.transform.scale(pygame.image.load('images/jail.jpg'),(BOXWIDTH,BOXHEIGHT)),
	'parking' : pygame.transform.scale(pygame.image.load('images/parking.jpg'),(BOXWIDTH,BOXHEIGHT)),
	'confucius_temple' : pygame.transform.scale(pygame.image.load('images/confucius_temple.jpg'),(BOXWIDTH,BOXHEIGHT)),
	'tainan_art_museum' : pygame.transform.scale(pygame.image.load('images/tainan_art_museum.jpg'),(BOXWIDTH,BOXHEIGHT)),
	'chihkan_tower' : pygame.transform.scale(pygame.image.load('images/chihkan_tower.jpg'),(BOXWIDTH,BOXHEIGHT)),
	'anping_castle' : pygame.transform.scale(pygame.image.load('images/anping_castle.jpg'),(BOXWIDTH,BOXHEIGHT))
}

UI_IMAGES = {
	'go_btn_down' : pygame.transform.scale(pygame.image.load('images/go_btn_down.jpg'),(BTNWIDTH,BTNHEIGHT)),
	'go_btn_up' : pygame.transform.scale(pygame.image.load('images/go_btn_up.jpg'),(BTNWIDTH,BTNHEIGHT)),
	'arrow_up1' : pygame.transform.scale(pygame.image.load('images/arrow_up1.jpg'),(ARROWWIDTH,ARROWHEIGHT)),
	'arrow_down1' : pygame.transform.scale(pygame.image.load('images/arrow_down1.jpg'),(ARROWWIDTH,ARROWHEIGHT)),
	'arrow_left1' : pygame.transform.scale(pygame.image.load('images/arrow_left1.jpg'),(ARROWHEIGHT,ARROWWIDTH)),
	'arrow_right1' : pygame.transform.scale(pygame.image.load('images/arrow_right1.jpg'),(ARROWHEIGHT,ARROWWIDTH)),
	'arrow_up2' : pygame.transform.scale(pygame.image.load('images/arrow_up2.jpg'),(ARROWWIDTH,ARROWHEIGHT)),
	'arrow_down2' : pygame.transform.scale(pygame.image.load('images/arrow_down2.jpg'),(ARROWWIDTH,ARROWHEIGHT)),
	'arrow_left2' : pygame.transform.scale(pygame.image.load('images/arrow_left2.jpg'),(ARROWHEIGHT,ARROWWIDTH)),
	'arrow_right2' : pygame.transform.scale(pygame.image.load('images/arrow_right2.jpg'),(ARROWHEIGHT,ARROWWIDTH)),
	'dice1' : pygame.transform.scale(pygame.image.load('images/dice1.jpeg'),(DICEWIDTH,DICEHEIGHT)),
	'dice2' : pygame.transform.scale(pygame.image.load('images/dice2.jpeg'),(DICEWIDTH,DICEHEIGHT)),
	'dice3' : pygame.transform.scale(pygame.image.load('images/dice3.jpeg'),(DICEWIDTH,DICEHEIGHT)),
	'dice4' : pygame.transform.scale(pygame.image.load('images/dice4.jpeg'),(DICEWIDTH,DICEHEIGHT)),
	'dice5' : pygame.transform.scale(pygame.image.load('images/dice5.jpeg'),(DICEWIDTH,DICEHEIGHT)),
	'dice6' : pygame.transform.scale(pygame.image.load('images/dice6.jpeg'),(DICEWIDTH,DICEHEIGHT)),
	'building1' : pygame.transform.scale(pygame.image.load('images/building1.png'),(BUILDINGWIDTH,BUILDINGHEIGHT)),
	'building2' : pygame.transform.scale(pygame.image.load('images/building2.png'),(BUILDINGWIDTH,BUILDINGHEIGHT))
}

FUNCTION = {
	'start' : 0,
	'arrest' : 1,
	'jail' : 2,
	'parking' : 3,
	'estate' : 4
}

DIRECT = {
	'_left' : 0,
	'_right' : 1,
	'_up' : 2,
	'_down' : 3
}


def main():
	map_surface, map_pos, game_map, building_pos, arrow_pos, arrow_dir = SetGameMap(HBOXNUM,VBOXNUM) # Setup game map
	blank_pos = [map_pos[0] - 60,map_pos[1] - 60,map_pos[2] + 120,map_pos[3] + 120]
	#blank_surface = pygame.Surface((blank_pos[2],blank_pos[3]), pygame.SRCALPHA) # for drawing buildings
	#blank_surface.fill((255,255,255))
	BOXNUM = len(game_map)
	
	##################################################################################################################################################################################
	# Fill content into game map
	##################################################################################################################################################################################

	location_list = []
	location_list.append(Location(0,IMAGES['start'],game_map[0],FUNCTION['start'],-1,-1,-1))
	location_list.append(Location(1,IMAGES['confucius_temple'],game_map[1],FUNCTION['estate'],1200,1000,500))
	location_list.append(Location(2,IMAGES['jail'],game_map[2],FUNCTION['jail'],-1,-1,-1)) # Has to match JAIL_POS
	location_list.append(Location(3,IMAGES['tainan_art_museum'],game_map[3],FUNCTION['estate'],1400,1000,600))
	location_list.append(Location(4,IMAGES['parking'],game_map[4],FUNCTION['parking'],-1,-1,-1))
	location_list.append(Location(5,IMAGES['chihkan_tower'],game_map[5],FUNCTION['estate'],1800,1600,800))
	location_list.append(Location(6,IMAGES['arrest'],game_map[6],FUNCTION['arrest'],-1,-1,-1))
	location_list.append(Location(7,IMAGES['anping_castle'],game_map[7],FUNCTION['estate'],2200,2000,1000))

	for location in location_list:
		location.render(map_surface)

	##################################################################################################################################################################################

	##################################################################################################################################################################################
	# Setup Game UI
	##################################################################################################################################################################################

	ui_list = []
	go_btn = Button(UI_IMAGES['go_btn_up'],UI_IMAGES['go_btn_down'],(1350,700))
	ui_list.append(go_btn)
	step = 1 # Initial dice point

	players = []
	players.append(Player(1))
	players.append(Player(2))
	player_turn = 1
	PLAYERNUM = len(players)

	offset = []
	for i in range(PLAYERNUM):
		offset.append([(0,(ARROWWIDTH + 10)*i),(0,(ARROWWIDTH + 10)*i),((ARROWWIDTH + 10)*i,0),((ARROWWIDTH + 10)*i,0)])

	building_offset = []
	for i in range(BUILDLIMIT):
		building_offset.append([(0,(BUILDINGHEIGHT + 5)*i),(0,(BUILDINGHEIGHT + 5)*i),((BUILDINGWIDTH + 5)*i,0),((BUILDINGWIDTH + 5)*i,0)])

	##################################################################################################################################################################################

	##################################################################################################################################################################################
	# Game loop
	##################################################################################################################################################################################

	print(building_pos)
	while True:
		window.fill((0,0,0))
		pygame.draw.rect(window,WHITE,blank_pos,0)
		#window.blit(blank_surface,(blank_pos[0],blank_pos[1]))
		window.blit(map_surface,(map_pos[0],map_pos[1])) # Draw game map
		window.blit(UI_IMAGES['dice' + str(step)],(1200,725))
		DrawGUI(ui_list) # Draw GUI
		DrawPlayer(players,arrow_pos,arrow_dir,offset)
		DrawBuildings(location_list,building_pos,building_offset,arrow_dir)

		for event in pygame.event.get():

			if event.type == pygame.MOUSEBUTTONDOWN:
			
				if go_btn.isHover():
					player_cur = players[player_turn - 1]
					player_turn += 1
					if player_turn == len(players): player_turn = 0

					# Judge if player is in jail
					if player_cur.freeze_turn > 0:
						player_cur.freeze_turn -= 1
						print('player' + str(player_cur.player_num) + ' is in jail!')
						continue

					step = random.randint(1,6)
					player_cur.Move(step,BOXNUM)
					
					# Execute loaction effect
					location = location_list[player_cur.pos]
					#print('player position: ' + str(player_cur.pos))
					#print('location function: ' + str(location.func))
					if location.func == FUNCTION['arrest']:
						# Redraw game window
						window.fill((0,0,0))
						pygame.draw.rect(window,WHITE,blank_pos,0)
						window.blit(map_surface,(map_pos[0],map_pos[1])) # Draw game map
						window.blit(UI_IMAGES['dice' + str(step)],(1200,725))
						DrawGUI(ui_list) # Draw GUI
						DrawPlayer(players,arrow_pos,arrow_dir,offset)
						DrawBuildings(location_list,building_pos,building_offset,arrow_dir)

						player_cur.Transport(JAIL_POS)
						player_cur.freeze_turn = 2
						print('player' + str(player_cur.player_num) + ' is arrested!')
						pygame.display.update()
						GAMECLOCK.tick(2)

					elif location.func == FUNCTION['estate']:
						# Redraw game window
						window.fill((0,0,0))
						pygame.draw.rect(window,WHITE,blank_pos,0)
						window.blit(map_surface,(map_pos[0],map_pos[1])) # Draw game map
						window.blit(UI_IMAGES['dice' + str(step)],(1200,725))
						DrawGUI(ui_list) # Draw GUI
						DrawPlayer(players,arrow_pos,arrow_dir,offset)
						DrawBuildings(location_list,building_pos,building_offset,arrow_dir)
						pygame.display.update()

						if (location.owner == -1) and (player_cur.money >= location.cost):
							purchase = input('Do you want to purchase this place? (y/n)')
							if purchase == 'y':
								player_cur.money -= location.cost
								location.owner = player_cur.player_num
								location.buildings += 1
								print('player' + str(player_cur.player_num) + ' has: ' + str(player_cur.money))

						elif (location.owner > 0) and (location.owner != player_cur.player_num) and (players[location.owner - 1].freeze_turn == 0):
							if location.tolls > player_cur.money:
								print('player' + str(player_cur.player_num) + ' goes bankrupt!')
								terminate()

							tolls = location.tolls
							player_cur.money -= tolls
							players[location.owner - 1].money += tolls
							print('player' + str(player_cur.player_num) + ' pays ' + str(tolls) + ' dollars to player' + str(location.owner))
							print('player' + str(player_cur.player_num) + ' has: ' + str(player_cur.money))
							print('player' + str(location.owner) + ' has: ' + str(players[location.owner - 1].money))

						elif (location.owner == player_cur.player_num) and (player_cur.money >= location.extend_cost) and (location.buildings < BUILDLIMIT):
							purchase = input('Do you want to build extend building at this place? (y/n)')
							if purchase == 'y':
								player_cur.money -= location.extend_cost
								location.buildings += 1
								location.tolls *= location.buildings
								print('player' + str(player_cur.player_num) + ' has: ' + str(player_cur.money))

			elif event.type == QUIT:
				terminate()

		pygame.display.update()
		GAMECLOCK.tick(FPS)

	##################################################################################################################################################################################


def SetGameMap(h_box,v_box):
	map_left = WINDOWWIDTH/2 - (h_box/2)*BOXWIDTH
	map_right = WINDOWWIDTH/2 + (h_box/2)*BOXWIDTH
	map_top = WINDOWHEIGHT/2 - (v_box/2)*BOXHEIGHT
	map_bottom = WINDOWHEIGHT/2 + (v_box/2)*BOXHEIGHT

	map_width = map_right - map_left
	map_height = map_bottom - map_top
	map_surface = pygame.Surface((map_width,map_height), pygame.SRCALPHA)

	start_left = map_width - BOXWIDTH
	start_height = map_height - BOXHEIGHT
	end_left = 0
	end_height = 0
	game_map = [None]*(h_box*2 + (v_box - 2)*2)
	building_pos = [None]*(h_box*2 + (v_box - 2)*2)
	arrow_pos = [None]*(h_box*2 + (v_box - 2)*2)
	arrow_dir = [None]*(h_box*2 + (v_box - 2)*2)

	# Draw horizontal boxes on map
	for i in range(h_box):
		rect_left = start_left - i*BOXWIDTH
		rect_top = start_height
		pygame.draw.rect(map_surface,WHITE,[rect_left,rect_top,BOXWIDTH,BOXHEIGHT],3)
		text = font_obj.render(str(i),True,WHITE,(0,0,0,0))
		text_rect = text.get_rect()
		text_rect.center = (rect_left + BOXWIDTH/2,rect_top + BOXHEIGHT/2)
		map_surface.blit(text,text_rect)
		game_map[i] = [rect_left, rect_top]
		building_pos[i] = [rect_left + map_left, rect_top + map_top + BOXHEIGHT]
		arrow_pos[i] = [rect_left + map_left, rect_top + map_top + BOXHEIGHT + BLANKHEIGHT]
		arrow_dir[i] = '_down'

		rect_left = end_left + i*BOXWIDTH
		rect_top = end_height
		pygame.draw.rect(map_surface,WHITE,[rect_left,rect_top,BOXWIDTH,BOXHEIGHT],3)
		text = font_obj.render(str(i + h_box + v_box - 2),True,WHITE,(0,0,0,0))
		text_rect = text.get_rect()
		text_rect.center = (rect_left + BOXWIDTH/2,rect_top + BOXHEIGHT/2)
		map_surface.blit(text,text_rect)
		game_map[i + h_box + v_box - 2] = [rect_left,rect_top]
		building_pos[i + h_box + v_box - 2] = [rect_left + map_left, rect_top + map_top - BUILDINGHEIGHT]
		arrow_pos[i + h_box + v_box - 2] = [rect_left + map_left, rect_top + map_top - ARROWHEIGHT - BLANKHEIGHT]
		arrow_dir[i + h_box + v_box - 2] = '_up'

	# Draw vertical boxes on map
	for i in range(1,v_box - 1):
		rect_left = start_left
		rect_top = start_height - i*BOXHEIGHT
		pygame.draw.rect(map_surface,WHITE,[rect_left,rect_top,BOXWIDTH,BOXHEIGHT],3)
		text = font_obj.render(str(h_box*2 + (v_box - 2)*2 - i),True,WHITE,(0,0,0,0))
		text_rect = text.get_rect()
		text_rect.center = (rect_left + BOXWIDTH/2,rect_top + BOXHEIGHT/2)
		map_surface.blit(text,text_rect)
		game_map[h_box*2 + (v_box - 2)*2 - i] = [rect_left,rect_top]
		building_pos[h_box*2 + (v_box - 2)*2 - i] = [rect_left + map_left + BOXWIDTH, rect_top + map_top]
		arrow_pos[h_box*2 + (v_box - 2)*2 - i] = [rect_left + map_left + BOXWIDTH + BLANKWIDTH, rect_top + map_top]
		arrow_dir[h_box*2 + (v_box - 2)*2 - i] = '_right'

		rect_left = end_left
		rect_top = start_height - i*BOXHEIGHT
		pygame.draw.rect(map_surface,WHITE,[rect_left,rect_top,BOXWIDTH,BOXHEIGHT],3)
		text = font_obj.render(str(h_box + i - 1),True,WHITE,(0,0,0,0))
		text_rect = text.get_rect()
		text_rect.center = (rect_left + BOXWIDTH/2,rect_top + BOXHEIGHT/2)
		map_surface.blit(text,text_rect)
		game_map[h_box + i - 1] = [rect_left,rect_top]
		building_pos[h_box + i - 1] = [rect_left + map_left - BUILDINGWIDTH, rect_top + map_top]
		arrow_pos[h_box + i - 1] = [rect_left + map_left - ARROWHEIGHT - BLANKWIDTH, rect_top + map_top]
		arrow_dir[h_box + i - 1] = '_left'

	return map_surface, (map_left, map_top, map_width, map_height), game_map, building_pos, arrow_pos, arrow_dir


def DrawGUI(ui_list):
	for ui in ui_list:
		ui.render(window)
	return


def DrawPlayer(player_list,arrow_pos,arrow_dir,offset):
	for player in player_list:
		pos_x = arrow_pos[player.pos][0] + offset[player.player_num - 1][DIRECT[arrow_dir[player.pos]]][0]
		pos_y = arrow_pos[player.pos][1] + offset[player.player_num - 1][DIRECT[arrow_dir[player.pos]]][1]
		player.render(window,UI_IMAGES['arrow' + arrow_dir[player.pos] + str(player.player_num)],(pos_x,pos_y))
	return


def DrawBuildings(location_list,building_pos,building_offset,arrow_dir):
	for location in location_list:
		for i in range(location.buildings):
			pos_x = building_pos[location.num][0] + building_offset[i][DIRECT[arrow_dir[location.num]]][0]
			pos_y = building_pos[location.num][1] + building_offset[i][DIRECT[arrow_dir[location.num]]][1]
			window.blit(UI_IMAGES['building' + str(location.owner)],(pos_x,pos_y))


def terminate():
	pygame.quit()
	sys.exit()


if __name__ == '__main__':
	main()