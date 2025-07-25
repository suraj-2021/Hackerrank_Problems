from collections import OrderedDict 

ordered = OrderedDict()

n = int(input())

for i in range(0,n):
    q =0
    string = " "
    x = input().split()
    if len(x)>2:
        q = int(x.pop())
        string = " ".join(x)
        
        if string not in ordered:
            ordered[string] = q
        
        else:
            ordered[string]+=q
        
    
    else:
        if x[0] not in ordered:
            ordered[x[0]] = int(x[1])
        else:
            ordered[x[0]]+=int(x[1])
    
for x,y in ordered.items():
    print(x+' '+str(y))
