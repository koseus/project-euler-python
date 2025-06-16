def get_cycle_length(d):
    """
    Find the length of the recurring cycle in the decimal representation of 1/d.
    Returns 0 if the decimal terminates.
    """
    # Keep track of remainders we've seen and their positions
    remainders = {}
    remainder = 1  # Start with remainder 1
    position = 0
    
    while remainder != 0:
        # If we've seen this remainder before, we've found a cycle
        if remainder in remainders:
            return position - remainders[remainder]
        
        # Record this remainder and its position
        remainders[remainder] = position
        
        # Perform one step of long division
        remainder = (remainder * 10) % d
        position += 1
    
    return 0  # No cycle found (decimal terminates)

def solve():
    """
    Find the value of d < 1000 for which 1/d contains the longest recurring cycle
    in its decimal fraction part.
    """
    max_cycle_length = 0
    result = 0
    
    # We only need to check prime numbers, as composite numbers will have
    # cycle lengths that are factors of their prime factors
    for d in range(2, 1000):
        cycle_length = get_cycle_length(d)
        if cycle_length > max_cycle_length:
            max_cycle_length = cycle_length
            result = d
    
    return result
