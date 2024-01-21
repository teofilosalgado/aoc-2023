import unittest

from src.day5 import part1


class MainTest(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(part1("inputs/day5_sample1.txt"), 35)
