def solve():
    """Sum of multiples of 3 or 5 below 1000."""
    return sum(number for number in range(1000) if number % 3 == 0 or number % 5 == 0)
