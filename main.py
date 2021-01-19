import pygame
import os
import board

#Constants
def global_vars():
	return {
	"SCREEN_SIZE": 800, 
	"DIS_SIZE": 860,
	"DISPLAY": (869, 860),
	"SQUARE_LEN": 800 // 8,
	"BROWN": (100, 40, 0),
	"BLACK": (0, 0, 0),
	"WHITE": (255, 255, 255),
	"YELLOW": (255, 255, 0),
	"ROWS": 9,
	"DIFF": (860 - 800) // 2,
	"IMAGES": {},
	}

def init(var):
	pygame.init()
	win = pygame.display.set_mode(var["DISPLAY"])
	pygame.display.set_caption("CHESS")
	clock = pygame.time.Clock()
	return win, clock

def loop():
	run = True
	var = global_vars()
	win, clock = init(var)
	brd = board.draw_board(win, var)
	pygame.display.update()
	while run:
		var
		for event in pygame.event.get():
			
			if event.type == pygame.QUIT:
				run = False
	pygame.display.flip()

if __name__ == "__main__": loop()
