from itertools import product
from math import prod
m,n = map(int,input().split())
l = []

for _ in range(m):
    l.append(list(map(int,input().split()))[1:])

products = list(product(*l)) 

**** this needs to be fixed**** => result = max([(sum(x**x)for x in j)%n for j in products])

print(products)

