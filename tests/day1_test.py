import unittest

from src.day1 import part1, part2


class MainTest(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(part1("inputs/day1_sample1.txt"), 142)

    def test_part2(self):
        self.assertEqual(part2("inputs/day1_sample2.txt"), 281)
