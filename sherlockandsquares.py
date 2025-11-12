import math
t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    result = math.floor(math.sqrt(b)) - math.ceil(math.sqrt(a)) + 1
    print(result if result > 0 else 0)
