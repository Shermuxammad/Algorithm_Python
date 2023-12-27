n = int(input('n = '))

x = True

for i in range(1, n+1):
    a = int(input('a = '))
    if x:
        max = a
        min = a
        x = False
        
    if min > a:
        min = a 
    if max < a:
        max = a
print("Entered {} numbers, the biggest is {} and the smallest is {} and the intermediate arithmetic is".format(n, max, min), (max+min)/2)