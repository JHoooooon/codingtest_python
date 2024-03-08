import unittest
import main
from test import INPUT, OUTPUT

class Test(unittest.TestCase):
    def test_solution(self):
        for idx in range(len(INPUT)):
            self.assertEqual(main.solution(INPUT[idx]), OUTPUT[idx])