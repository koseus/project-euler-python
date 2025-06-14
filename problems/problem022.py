def solve():
    """
    Using names.txt, a 46K text file containing over five-thousand first names, 
    begin by sorting it into alphabetical order. Then working out the alphabetical 
    value for each name, multiply this value by its alphabetical position in the 
    list to obtain a name score.
    """
    # Read and sort names
    with open("assets/p022_names.txt") as f:
        # Read the file, remove quotes, split by comma, and sort
        names = sorted(name.strip('"') for name in f.read().split(','))
    
    total_score = 0
    for i, name in enumerate(names, 1):  # Start position from 1
        # Calculate alphabetical value (A=1, B=2, etc.)
        name_value = sum(ord(c) - ord('A') + 1 for c in name)
        # Multiply by position and add to total
        total_score += name_value * i
    
    return total_score

    
