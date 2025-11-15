n = int(input()) 
arr = list(map(int,input().split())) 

while(arr):
    m = min(arr)
    print(len(arr))
    while(m in arr):
        arr.remove(m) 
    for i in range(len(arr)):
        arr[i] -= m 
    
    
