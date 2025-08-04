from collections import deque

N = int(input())
res = []

for _ in range(N):
    top = float('inf')
    n = int(input())
    d = deque(map(int, input().split()))
    possible = True
    while d:
        if d[0] >= d[-1] and d[0] <= top:
            top = d.popleft()
        elif d[-1] > d[0] and d[-1] <= top:
            top = d.pop()
        else:
            possible = False
            break
    res.append('Yes' if possible else 'No')

for x in res:
    print(x)
