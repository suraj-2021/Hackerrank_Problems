import math
import os
import random
import re
import sys

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(m):
    matrix.append(input().strip())

word = ""
for i in range(0,n):
    j =0
    while(j<m):
        word+=matrix[j][i]
        j+=1

y = re.sub(r"(?<=\w)[^\w]+(?=\w)"," ",word )
print(y)
