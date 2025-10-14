a = int(input())
a_set = set(map(int,input().split()))
b = int(input())
b_set = set(map(int,input().split()))
c_set = a_set.symmetric_difference(b_set)
for i in sorted(c_set):
    print(i)
