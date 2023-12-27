# Optimal Tub son

from math import *


n = int(input("n = "))
print(2, end=" ")
sanagich = 0
for i in range(3, n+1, 2):
    s = 0
    for j in range(3,int(sqrt(i))+1, 2):
        sanagich += 1   
        if i%j == 0:
            s += 1
            break
    if s == 0:
        print(i, end=" ")
print("\nSum of loop: ", sanagich)