import unittest
from math_quiz import function_number, function_operator, function_math_problem


class TestMathGame(unittest.TestCase):

    def test_function_number(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = function_number(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val, f"{rand_num} is out of range")

    def test_function_operator(self):
        # Test if the returned operator is one of the specified choices
        valid_operators = ['+', '-', '*']
        for _ in range(1000):  # Test a large number of random values
          operator = function_operator()
          self.assertIn(operator, valid_operators, f"Unexpected operator: {operator}")

        

    def test_function_math_problem(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (11, 3, '-', '11 - 3', 8),
                (5, 3, '*', '5 * 3', 15),
                (11, 5, '+', '11 + 5', 16),
                (8, 2, '-', '8 - 2', 6),
                (4, 4, '*', '4 * 4', 16)
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
             problem, answer = function_math_problem(num1, num2, operator)   
             self.assertEqual(problem, expected_problem, f"Expected problem: {expected_problem}, got: {problem}")
             self.assertEqual(answer, expected_answer, f"Expected answer: {expected_answer}, got: {answer}")   

if __name__ == "__main__":
    unittest.main()
