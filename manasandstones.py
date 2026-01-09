def stones(n, a, b):
    # Start with a set containing just the starting stone (0)
    current_stones = {0}
    
    # We loop n-1 times because we take n-1 steps
    for _ in range(n - 1):
        next_stones = set()
        
        # For every stone we currently have, add 'a' and 'b'
        for s in current_stones:
            next_stones.add(s + a)
            next_stones.add(s + b)
            
        # Update current_stones to be the new set we just calculated
        current_stones = next_stones
        
    # Return sorted list as expected
    return sorted(current_stones)
