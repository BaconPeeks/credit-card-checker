# Credit Card Validator Using the Luhn Algorithm

This project implements a simple Python function to validate credit card numbers using the **Luhn algorithm**, a widely used checksum formula for verifying identification numbers such as credit card numbers.

---

## Features

- Validates that input is a numeric string of at least 16 digits.
- Applies the Luhn algorithm to determine if the credit card number is valid.
- Supports detection of common card types through starting digit (Visa, Mastercard, Discover) — easily extendable.
- Raises meaningful exceptions for invalid inputs to ensure robust error handling.

---

## How It Works

The Luhn algorithm works as follows:

1. Starting from the rightmost digit (excluding the check digit), every second digit is doubled.
2. If doubling results in a number greater than 9, subtract 9 from it.
3. Sum all the digits (both doubled and untouched).
4. If the total modulo 10 equals 0, the card number is valid.

---

## Usage

```python
from credit_card_validator import check_cc

try:
    valid = check_cc("4532015112830366")  # Example Visa number
    print("Valid card number!" if valid else "Invalid card number.")
except ValueError as e:
    print(f"Input error: {e}")
