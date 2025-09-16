#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    d = 0
    u = 0
    sp = path[0] 
    r = []
    for i in range(len(path)):
        if path[i] == 'U':
            u+=1 
        else:
            d+=1
        
        if d-u ==0 and sp =='U':
            r.append('m')
            try:
               sp = path[i+1]
            except IndexError:
                return(r.count('v'))   
            continue
        if d-u ==0 and sp =='D':
            r.append('v')
            try:
               sp = path[i+1]
            except IndexError:
                return(r.count('v'))   
    return(r.count('v'))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
