#!/usr/bin/env python
"""
Unit tests
"""

import unittest
from player1 import player1

class Testing(unittest.TestCase):
	def test_player1(self):
		self.assertTrue(player1(), "r")
		self.assertTrue(player1(), "p")
		self.assertTrue(player1(), "s")
		self.assertTrue(player1(), "q")

unittest.main()
