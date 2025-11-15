from datetime import date

d1, m1, y1 = map(int, input().split())
d2, m2, y2 = map(int, input().split())

actual = date(y1, m1, d1)
expected = date(y2, m2, d2)

if actual > expected:
    if y1 > y2:
        print(10000)
    elif m1 > m2:
        print(500 * (m1 - m2))
    else:
        print(15 * (d1 - d2))
else:
    print(0)
