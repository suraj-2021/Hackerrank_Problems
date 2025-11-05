n = int(input())
array = input().split()
condition1 = all(int(x) > 0 for x in array)

condition2 = any(x == x[::-1] for x in array)

print(condition1 and condition2)
