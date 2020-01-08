"""Unittest class.
"""

import unittest
from unittest import mock

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
    def test_quitting():
        """Placeholder.
        """
        with mock.patch('builtins.input', return_value="yes"):
            assert yes_or_no() == "Quitter!"

        with mock.patch('builtins.input', return_value="no"):
            assert yes_or_no() == "Awesome!"

if __name__ == '__main__':
    unittest.main()
