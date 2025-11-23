n,k = map(int,input().split()) 
s= list(map(int,input().split())) 
arr=[0]*k
le=0 

for j in s:
    r = j%k 
    arr[r]+=1

if arr[0]>=1:
    le+=1 
for i in range(1,(k+1)//2):
    le+=max(arr[i],arr[k-i])
if k % 2 == 0:
    if arr[k // 2] > 0:
        le+=1
print(le)
