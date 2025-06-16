def solve():
    """
    We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.
    The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.
    Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
    HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
    """
    products = set()
    for a in range(1, 100):
        for b in range(a, 10000):
            product = a * b
            if is_pandigital(a, b, product):
                products.add(product)
    return sum(products)

def is_pandigital(a, b, product):
    digits = str(a) + str(b) + str(product)
    return len(digits) == 9 and set(digits) == set('123456789')

