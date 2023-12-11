import unittest

from src.day3 import part1


class MainTest(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(part1("inputs/day3_sample1.txt"), 4361)
