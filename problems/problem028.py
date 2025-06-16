def solve():
    """
    Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:
    21 22 23 24 25
    20  7  8  9 10
    19  6  1  2 11
    18  5  4  3 12
    17 16 15 14 13
    It can be verified that the sum of the numbers on the diagonals is 101.
    What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
    """
    size = 1001
    total = 1  # Start with the center number 1
    
    # For each layer of the spiral (starting from the inner layer)
    for layer in range(1, (size + 1) // 2):
        # Calculate the four corner numbers for this layer
        # The corners are at positions: top-right, top-left, bottom-left, bottom-right
        # The numbers increase by 2*layer for each step
        corner = (2 * layer + 1) ** 2  # top-right corner
        total += corner  # top-right
        total += corner - 2 * layer  # top-left
        total += corner - 4 * layer  # bottom-left
        total += corner - 6 * layer  # bottom-right
    
    return total
    