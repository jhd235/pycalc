import unittest
from calc import msg

class TestStringMethods(unittest.TestCase):

    def test_msg(self):
        self.assertEqual(msg(), 'k')


if __name__ == '__main__':
    unittest.main()