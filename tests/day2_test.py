import unittest

from src.day2 import part1


class MainTest(unittest.TestCase):
    def test_sample1(self):
        self.assertEqual(part1("inputs/day2_sample1.txt"), 8)
