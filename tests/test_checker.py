import unittest
from cc_checker import main

class TestCreditCardChecker(unittest.TestCase):
    def test_valid_card(self):
        self.assertTrue(main("4532015112830366"))  # Valid Visa

    def test_invalid_card(self):
        self.assertFalse(main("1234567890123456"))  # Invalid number

    def test_short_length(self):
        with self.assertRaises(ValueError):
            main("123")

    def test_non_digit_input(self):
        with self.assertRaises(ValueError):
            main("abcd1234")
    
    def test_valid_mastercard(self):
        # Mastercard usually starts with 5
        self.assertTrue(main("5500000000000004"))

    def test_valid_discover(self):
        # Discover cards start with 6
        self.assertTrue(main("6011000990139424"))

    def test_all_zeros(self):
        # All zeros should fail validation
        self.assertFalse(main("0000000000000000"))

    def test_number_with_spaces(self):
        # Spaces should cause ValueError as per current implementation
        with self.assertRaises(ValueError):
            main("4532 0151 1283 0366")

    def test_number_with_dashes(self):
        # Dashes should also raise ValueError currently
        with self.assertRaises(ValueError):
            main("4532-0151-1283-0366")

    def test_minimum_length_valid(self):
        # Exactly 16 digits valid card
        self.assertTrue(main("4000056655665556"))  # Visa test number

    def test_minimum_length_invalid(self):
        # Exactly 16 digits but invalid
        self.assertFalse(main("4000056655665555"))

if __name__ == '__main__':
    unittest.main()
