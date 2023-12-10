import unittest

from src.day1 import main


class MainTest(unittest.TestCase):
    def test_sample1(self):
        self.assertEqual(main("inputs/day1_sample1.txt"), 142)
