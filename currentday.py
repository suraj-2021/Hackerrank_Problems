import calendar 
x = list(map(int,input().split()))
days = list(calendar.day_name)
y = calendar.weekday(x[2],x[0],x[1])
print(days[y].upper())
