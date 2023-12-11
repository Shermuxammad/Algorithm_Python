import math

a = float(input())
b = float(input())


if a <= 0 and b <= 0:
    print('Invalid number')
else:
    root = math.sqrt(a * b)
    print(root)
