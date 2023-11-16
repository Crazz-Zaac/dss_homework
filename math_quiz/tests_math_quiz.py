import unittest
from math_quiz import generate_random_number, randomize_operator, operate


class TestMathGame(unittest.TestCase):

    def test_function_A(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generate_random_number(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_function_B(self):
        # Test if symbols generated are within the specific symbols +, -, * or not

        # operator validation
        valid_operators = ['+', '-', '*']

        # testing for multiple calls
        for _ in range(50):
            res = randomize_operator()
            self.assertIn(res, valid_operators)


    def test_function_C(self):
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (3, 9, '*', '3 * 9', 27),
            (25, 4, '-', '25 - 4', 21),
            (16, 4, '*', '16 * 4', 64),
            (8, 10, '-', '8 - 10', -2),
            (15, 2, '+', '15 + 2', 17),
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            prob, output = operate(num1, num2, operator)
            self.assertEqual(prob, expected_problem)
            self.assertEqual(output, expected_answer)


if __name__ == "__main__":
    unittest.main()
