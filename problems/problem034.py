def solve():
    """
    145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
    Find the sum of all numbers which are equal to the sum of the factorial of their digits.
    Note: as 1! = 1 and 2! = 2 are not sums they are not included.
    """
    total = 0
    for n in range(3, 1000000):
        if n == sum(factorial(int(digit)) for digit in str(n)):
            total += n
    return total

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

