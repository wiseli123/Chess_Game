import pygame
import os
import time
from main import global_vars

var = global_vars()

def draw_board(win, var):
	int_i = 0
	int_j = 0
	for i in range(var["ROWS"] - 1):

		for j in range(var["ROWS"] - 1):
			if int_j % 9 == 0:
				int_j += 2
			else:
				int_j += 1
			if int_j % 2 == 0:
				color = var["WHITE"]
			else:
				color = var["BROWN"]
			x1 = var["DIFF"] + (i * var["SQUARE_LEN"])
			y1 =  var["DIFF"] + (j * var["SQUARE_LEN"])
			pygame.draw.rect(win, color, (x1, y1, var["SQUARE_LEN"], var["SQUARE_LEN"]), 0)
