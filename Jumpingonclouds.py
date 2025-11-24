def jumpingOnClouds(c):
    i = 0
    jumps = 0
    while i < len(c) - 1:
        # Try to jump 2 clouds if possible
        if i + 2 < len(c) and c[i + 2] == 0:
            i += 2
        else:
            i += 1
        jumps += 1
    return jumps
