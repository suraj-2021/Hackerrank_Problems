import numpy as np 
np.set_printoptions(legacy='1.13')
n = int(input())
m1= [list(map(int,input().split())) for _ in range(n)] 
m2 = [list(map(int,input().split())) for _ in range(n)]
A = np.array(m1)  
B = np.array(m2) 
dot = A @ B
print(dot)
