from unittest import TestCase
from main import solution
from test import INPUT, OUTPUT

class Test(TestCase):
    def test_solution(self):
        for idx in range(len(INPUT)):
            self.assertEqual(solution(INPUT[idx]), OUTPUT[idx])