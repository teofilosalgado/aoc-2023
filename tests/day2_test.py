import unittest

from src.day2 import part1, part2


class MainTest(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(part1("inputs/day2_sample1.txt"), 8)

    def test_part2(self):
        self.assertEqual(part2("inputs/day2_sample1.txt"), 2286)
