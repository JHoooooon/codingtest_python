import unittest
from test import INPUT, OUTPUT
# from main import solution
from solution import solution

class Test(unittest.TestCase):
    
    def test_runs(self):
        for idx in range(len(INPUT)):
            self.assertEqual(solution(INPUT[idx][0], INPUT[idx][1], INPUT[idx][2]), OUTPUT[idx])
