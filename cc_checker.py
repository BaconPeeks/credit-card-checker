card_types = {
    "Visa": 4,
    "Mastercard": 5,
    "Discover": 6
}

def main(number):
    """
    Validate a credit card number string using the Luhn algorithm.
    
    Args:
        number (str): The credit card number as a string of digits.
        
    Returns:
        bool: True if the number passes the Luhn check, False otherwise.
    
    Raises:
        ValueError: If the number length is less than 16 or contains non-digit characters.
    """
    # Ensure the credit card number is at least 16 digits long
    if len(number) < 16:
        raise ValueError('Card number must be at minimum 16 digits')
    
    # Ensure the card number contains only digits
    if not number.isdigit():
        raise ValueError('Card number must only contain digits')

    # Reject input that is all zeros (invalid card)
    if set(number) == {'0'}:
        return False

    # Process the digits to prepare for Luhn calculation
    doubled, remaining = double_digits(number)

    # Compute the Luhn checksum and return True if valid
    total = luhn(doubled, remaining)
    return total


def double_digits(number):
    """
    Process the card number digits for the Luhn algorithm:
    Double every second digit from the right, subtracting 9 if the result is greater than 9.
    
    Args:
        number (str): The credit card number string.
        
    Returns:
        tuple: A tuple containing two lists:
            - doubled: list of doubled (and adjusted) digits
            - remaining: list of digits that were not doubled
    """
    # Convert the input string into a list of integers
    digits = [int(d) for d in number]
    
    # Reverse the list to process digits from right to left
    reversed_digits = digits[::-1]
    
    # Select digits to double (every second digit starting from index 1)
    to_double = reversed_digits[1::2]
    
    # Select the digits that remain unchanged (every other digit starting from index 0)
    remaining = reversed_digits[::2]

    doubled = []
    # Double each digit and subtract 9 if the result is more than 9
    for digit in to_double:
        digit *= 2
        if digit > 9:
            digit -= 9
        doubled.append(digit)

    return doubled, remaining


def luhn(doubled, remaining):
    """
    Calculate the Luhn checksum from processed digit lists.
    
    Args:
        doubled (list): List of digits doubled and adjusted.
        remaining (list): List of digits that were not doubled.
        
    Returns:
        bool: True if the total modulo 10 is zero (valid card), False otherwise.
    """
    # Sum all digits from doubled and remaining lists
    total = sum(doubled) + sum(remaining)

    # Return True if total modulo 10 is zero, else False
    return total % 10 == 0
