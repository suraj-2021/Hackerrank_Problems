import re
n = int(input())

for _ in range(n):
    x = input()
    if re.match(r"^\+\d+\.\d+|\-\d+\.\d+|\.\d+|\+\.\d+|\d+\.\d+$",x):
        print("True")
    else:
        print("False")
    
