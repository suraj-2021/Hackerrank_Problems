t = int(input())

for _ in range(t):
    n = int(input())
    A = set(map(int,input().split()))
    p = int(input())
    B = set(map(int,input().split()))
    x = A.difference(B)
    if len(x) == 0:
        print('True') 
    else:
        print('False')
    
    
