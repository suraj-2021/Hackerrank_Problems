import re 
n = int(input())
pattern = r'#[0-9a-fA-F]{3}(?:[0-9a-fA-F]{3})?\b'
for _ in range(n):
    x = input()
    if ':' in x:
        y = re.search(pattern,x)
        for i in y:
            print(i)
            
            
        
