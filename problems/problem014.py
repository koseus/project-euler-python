def collatz_sequence_length(n):
    length = 1
    while n > 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        length += 1
    return length

def solve():
    """
    Find the starting number, under one million, which produces the longest Collatz sequence.
    """
    max_length = 0
    starting_number = 0
    for i in range(1, 1000000):
        length = collatz_sequence_length(i)
        if length > max_length:
            max_length = length
            starting_number = i
    return starting_number 