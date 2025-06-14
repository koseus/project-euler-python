def solve():
    """
    Find the product of the Pythagorean triplet for which a + b + c = 1000.
    """
    for a in range(1, 1000):
        for b in range(a + 1, 1000):
            c = 1000 - a - b
            if a**2 + b**2 == c**2:
                return a * b * c

    return None