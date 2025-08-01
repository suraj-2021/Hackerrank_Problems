from collections import deque
n = int(input())
d = deque() 
for _ in range(n):
    x = input().split()
    if x[0] =='append':
        d.append(x[1])
    elif x[0]=='appendleft':
        d.appendleft(x[1])
    elif x[0]=='pop':
        d.pop()
    else:
        d.popleft()
print(*list(d))
