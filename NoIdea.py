m,n = map(int,input().split())
array = set(list(map(int,input().split())))
a = list(map(int,input().split()))
b = list(map(int,input().split())) 
h = 0

for x in array:
    if x in a:
        h+=1
    elif x in b:
         h -=1
print(h)
    
         

