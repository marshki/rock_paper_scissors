#from nose.tools import *
from unittest import mock
from unittest.mock import patch
import io
import unittest

def foo():
    """Foo.
    """
    print("Something")
    
@patch('sys.stdout', new_callable=io.StringIO)
def test_foo_one(mock_stdout):
    foo()
    assert mock_stdout.getvalue() == 'Something\n'

test_foo_one()
