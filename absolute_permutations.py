def absolutePermutation(n, k):
    if k == 0:
        return list(range(1, n+1))
    
    used = [False] * (n + 1)
    result = [0] * (n + 1)
    
    for i in range(1, n+1):
        candidates = []
        low = i - k
        high = i + k
        
        if low >= 1 and not used[low]:
            candidates.append(low)
        if high <= n and not used[high]:
            candidates.append(high)
        
        if not candidates:
            return [-1]
        
        # Pick smallest for lex min
        cand = min(candidates)
        result[i] = cand
        used[cand] = True
    
    return result[1:]
