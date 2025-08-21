T = int(input())
symbol = ["+","-"]
result = []
for _ in range(T):
    N = list(input().strip())
    
    try:
       float("".join(N))
       pass
    except ValueError:
        result.append("False")
        continue
    
    if "." in N and((N.count(symbol[0])+N.count(symbol[1]))<=1):
        index = 0
        while(N[index]!="."):
            index+=1
        if len(N[index+1:])<=0:
            result.append("False")
            continue
        else:
            result.append("True")
            continue
    else:
        result.append("False")
        continue
        
for i in result:
    print(i)
    
    
    
