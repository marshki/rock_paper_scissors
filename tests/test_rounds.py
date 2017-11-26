#!/usr/bin/env python
""" 
Unit tests 
""" 

import unittest 
from rounds import rounds

class Testing(unittest.TestCase): 
	def test_rounds(self):
		self.assertTrue(rounds(), int)
unittest.main()
