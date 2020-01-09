# pylint: disable=W0613,W0622

"""Unittest class.
"""

import unittest
from unittest.mock import patch

def yes_or_no():
    """Placeholder.
    """
    answer = input("Do you want to quit? > ")
    if answer == "yes":
        return "Quitter!"
    elif answer == "no":
        return "Awesome!"
    else:
        return "BANG!"

class YesNo(unittest.TestCase):
    """Placeholder.
    """
    @patch('builtins.input', return_value="yes")
    def test_quitting(self, input):
        """Placeholder.
        """
        self.assertEqual(yes_or_no(), "Quitter!")

    @patch('builtins.input', return_value="no")
    def test_no(self, input):
        """Placeholder.
        """
        self.assertEqual(yes_or_no(), "Awesome!")

if __name__ == '__main__':
    unittest.main()
