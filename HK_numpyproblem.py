import numpy 

m,n = map(int,input().split())

arrayA = []
arrayB = []

for _ in range(m):
    arrayA.append(list(map(int,input().split())))

for _ in range(m):
    arrayB.append(list(map(int,input().split())))


A = numpy.array(arrayA,int)
B = numpy.array(arrayB,int)

print(A+B)
print(A-B)
print(A*B)
print(A//B)
print(A%B)
print(A**B)
