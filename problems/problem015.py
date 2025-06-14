def solve():
    """
    Find the number of lattice paths in a 20x20 grid.
    """
    size = 20
    # Create a grid where each cell represents the number of paths to reach it
    grid = [[1] * (size + 1) for _ in range(size + 1)]
    
    # For each cell, the number of paths is the sum of paths from left and top
    for i in range(1, size + 1):
        for j in range(1, size + 1):
            grid[i][j] = grid[i-1][j] + grid[i][j-1]
    
    return grid[size][size]
