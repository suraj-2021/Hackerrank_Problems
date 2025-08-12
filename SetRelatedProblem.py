A = set(map(int,input().split()))
n = int(input())
i=1
for _ in range(n):
    a = set(map(int,input().split()))
    
    if A.union(a)!=A:
        i=0
        break
if i==1:
    print("True")
else:
    print("False")
