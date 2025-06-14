from utils.math_helpers import lcm

def solve():
    """
    Find the smallest positive number that is evenly divisible by all numbers from 1 to 20.
    """
    result = 1
    for i in range(2, 21):
        result = lcm(result, i)
        # print(result)
    return result

   