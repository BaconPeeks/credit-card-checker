
# Validate a number string (like a credit card number) 
# using the Luhn algorithm. 
# Return True if valid, 
# False otherwise.

card_types = {
    "Visa": 4,
    "Mastercard": 5,
    "Discover": 6
}

def main(number):
    if len(number) < 16:
        raise ValueError('Card number must be at minimum 16 digits')
    
    if not number.isdigit():
        raise ValueError('Card number must only contain digits')

    if set(number) == {'0'}:
        # Reject all zeros
        return False

    doubled, remaining = double_digits(number)

    total = luhn(doubled, remaining)
    return total


def double_digits(number):
    digits = [int(d) for d in number]
    reversed_digits = digits[::-1]
    to_double = reversed_digits[1::2]
    remaining = reversed_digits[::2]

    doubled = []
    for digit in to_double:
        digit *= 2
        if digit > 9:
            digit -= 9
        doubled.append(digit)

    return doubled, remaining


def luhn(doubled, remaining):
    total = sum(doubled) + sum(remaining)

    return total % 10 == 0
