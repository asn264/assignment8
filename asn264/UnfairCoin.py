#! /data/anaconda/bin/python

import numpy as np

class UnfairCoin(object):
	'''Represents a coin with 51-49 heads to tails odds'''
	
	def __init__(self):
		self.heads = 1
		self.tails = 0

	def flip(self):
	
	        '''Flip according to unfair weights.'''
		val = np.random.randint(0, 100)
		if val <= 50:
			return self.heads
		else: 
			return self.tails
