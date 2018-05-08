import unittest
from calculator import do_math

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = do_math()

    def test_add(self):
        print("test_add")
        operand = self.calculator.do_math('+')
        self.assertEqual(5)

    def test_multiply(self):
        print("test_multiply")
        operand = self.calculator.do_math('*')
        self.assertEqual(9)

    def test_subtract(self):
        print("test_subtract")
        operand = self.calculator.do_math('-')
        self.assertEqual(10)

    def test_divide(self):
        print("test_divide")
        operand = self.calculator.do_math('/')
        self.assertEqual(22)

    def tearDown(self):
        print("TEAR DOWN")

if __name__ == '__main__':
    unittest.main()
