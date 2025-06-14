def solve():
    """Largest prime factor of 600851475143."""
    n = 600851475143
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n