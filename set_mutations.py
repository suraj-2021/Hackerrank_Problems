N = int(input())
A = set(list(map(int,input().split())))
n = int(input())
for _ in range(n):
    c = input().split()
    x = set(list(map(int,input().split())))
    method_name = c[0]
    method = getattr(A,method_name)
    method(x)
    
print(sum(A))    
