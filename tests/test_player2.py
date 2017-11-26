#!/usr/bin/env python
""" 
Unit tests 
""" 

import unittest 
from player2 import player2 

class Testing(unittest.TestCase): 
	def test_player2(self):
		self.assertTrue(player2(), "r")
		self.assertTrue(player2(), "p")
		self.assertTrue(player2(), "s")

unittest.main()
