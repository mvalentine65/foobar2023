import unittest
from solution import solution

class TestSolution(unittest.TestCase):

    def test_example_1_power_of_two(self):
        self.assertEqual(solution(4), 2)

    def test_example_2_one_off_power_of_two(self):
        self.assertEqual(solution(15), 5)

    def test_10_needs_to_add(self):
        self.assertEqual(solution(10), 4)

    def test_6_reduces_to_3(self):
        self.assertEqual(solution(6), 3)
if __name__ == "__main__":
    unittest.main()
