from unittest import TestCase
import calculator


class Test(TestCase):
    def test_add(self):
        # tests for the add() function
        self.assertEqual(calculator.add(6, 4), 10, 'Error when adding two positive numbers')
        self.assertEqual(calculator.add(6, -4), 2)
        self.assertEqual(calculator.add(-6, 4), -2)
        self.assertEqual(calculator.add(-6, -4), -10)

    def test_divide(self):
        self.assertRaises(ValueError, calculator.divide, 5, 0)

    def test_multiply(self):
        # tests for the add() function
        self.assertEqual(calculator.multiply(6, 4), 24)
        self.assertEqual(calculator.multiply(6, -4), -24)
        self.assertEqual(calculator.multiply(-6, 4), -24)
        self.assertEqual(calculator.multiply(-6, -4), 24)

    def test_subtract(self):
        # tests for the add() function
        self.assertEqual(calculator.subtract(6, 4), 2)
        self.assertEqual(calculator.subtract(6, -4), 10)
        self.assertEqual(calculator.subtract(-6, 4), -10)
        self.assertEqual(calculator.subtract(-6, -4), -2)
