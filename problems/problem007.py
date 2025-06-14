from utils.math_helpers import is_prime

def solve():
    """
    Find the 10001st prime number.
    """
    count = 0
    num = 1

    while count < 10001:
        num += 1
        if is_prime(num):
            count += 1
        # print(num)
    return num 