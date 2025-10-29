from collections import deque 
t = int(input()) 
for _ in range(t):
    found = 1 
    n = int(input())
    c = deque(list(map(int,input().split()))) 
    top = None
    while(len(c)>=1):
        x = c[0]
        y = c[-1]
        if top == None:
            top = x if x>y else y 
            if top == x:
                c.popleft() 
            else:
                c.pop()  
        else:
            z = x if x>y else y 
            if z <= top and z==x:
                top = z
                c.popleft()
            elif z<= top and z==y:
                top = z 
                c.pop() 
            else:
                found = 0
                break
    if found==0:
        print("No")
    else:
       print("Yes")
                
                
            
                
    
