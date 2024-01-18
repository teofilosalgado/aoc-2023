import unittest

from src.day4 import part1


class MainTest(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(part1("inputs/day4_sample1.txt"), 13)
