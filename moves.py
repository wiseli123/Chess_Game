# from main import global_vars
import pygame
import os
import numpy as np

def visualize(options):
	for opt in options:
		row, column = opt[0] - 1, opt[1] - 1
		grid = np.zeros((8, 8))
		grid[row, column] = 1
	print(grid)

class Moves:

	def __init__(self, board, pos):
		self.board = board
		# self.vars = global_vars()
		self.options = []
		row, column = pos
		self.row = row
		self.column = column
	

	def pawn(self, pos):
		if self.row == 7: self.options.append((self.row - 2, self.column))
		for i in range(-1, 2):
			self.options.append((self.row - 1, self.column + i))
		return self.options
	
	def king(self):
		for i in range(-1, 2):
			for j in range(-1, 2):
				if i or j:
					self.options.append((self.row + i, self.column + j))
		return self.options
	
	def rook(self):
		
		for i in range(1, 9):
				self.options.append((self.row, i))
				self.options.append((i, self.column))
		visualize(self.options)
		return self.options  # still return the initial position
	
	def bishop(self):
		for i in range(-1, 2, 2):
			for j in range(1, 9):
				self.options.append((self.row + j * i, self.column))
		# visualize(self.options)
		return self.options


board = 7
inst = Moves(board, (7, 3))
print(inst.rook())

