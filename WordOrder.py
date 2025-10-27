from collections import OrderedDict
n = int(input())
x = OrderedDict() 
t = 0 
for _ in range(n):
    y = input() 
    if y not in x:
        t+=1
        x[y]=1 
    else:
        x[y]+=1 
print(t)
print(*x.values())
    
