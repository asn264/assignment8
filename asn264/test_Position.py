from unittest import TestCase
from Position import *

pos = Position(10)

class PositionTest(TestCase):

	#Raise an error when nshares is not 1000,100, 10 or 1
	def test_valid_position(self):
		self.assertRaises(InvalidPositionError, Position, 12)

	#Ensure n_flips functions flips the coin exactly n_shares number of times
	def test_num_flips(self):
		self.assertEqual(len(pos.n_flips()),pos.nshares)


