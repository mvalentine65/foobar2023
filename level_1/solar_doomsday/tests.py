import unittest
from solution import solution

class TestSolution(unittest.TestCase):
    
    def test_case_1(self):
        expected = [9, 1, 1, 1]
        found = solution(12)
        self.assertEqual(expected, found)

    def test_case_2(self):
        expected = [15129,169,25,1]
        found = solution(15324)
        self.assertEqual(expected, found)


if __name__ == "__main__":
    unittest.main()

