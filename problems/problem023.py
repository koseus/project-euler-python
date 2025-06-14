def sum_proper_divisors(n):
    """Calculate sum of proper divisors of n"""
    if n == 1:
        return 0
    total = 1  # 1 is always a proper divisor
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            total += i
            if i != n // i:  # Don't count the square root twice
                total += n // i
    return total

def solve():
    """
    Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
    """
    # Find all abundant numbers up to 28123 (given in problem)
    abundant_numbers = [n for n in range(1, 28124) if sum_proper_divisors(n) > n]
    
    # Create a set of all numbers that can be written as sum of two abundant numbers
    sum_of_two_abundant = set()
    for i in abundant_numbers:
        for j in abundant_numbers:
            if i + j <= 28123:  # Only consider numbers up to 28123
                sum_of_two_abundant.add(i + j)
    
    # Sum all numbers that cannot be written as sum of two abundant numbers
    return sum(n for n in range(1, 28124) if n not in sum_of_two_abundant)


