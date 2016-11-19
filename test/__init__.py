import unittest
from beautifier import *

"""
Base Structure
"""

class TestEmailMethods(unittest.TestCase):

    def test_username(self, email):
        email = Email(email)
        self.assertEqual(email, 'me')

    def test_domain(self, email):
        self.assertTrue('imsach.in')


if __name__ == '__main__':
    unittest.main()