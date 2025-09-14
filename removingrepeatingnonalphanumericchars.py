import re 

m,n = map(int,input().split())

words = [input() for _ in range(m)] 


string = ""
for i in range(n):
    for j in range(m):
        string+=words[j][i]
        
pattern = r"(?<=\w)\W+(?=\w)"
result = re.sub(pattern," ",string)
print(result)
