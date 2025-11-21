n,k = map(int,input().split()) 
s = list(map(int,input().split()))
array = [0 for _ in range(k)]
out=1

for i in range(k):
    for j in s:
        if j%k == i:
            array[i]+=1 

for i in range(1, (k + 1) // 2):
    pair_remainder = k - i
    out += max(array[i], array[pair_remainder])
    
print(out)
