n = int(input("Enter n value (n > 0): "))
while n<=0:
    print("n value must be bigger than 0. Enter valud number!")
    n = int(input("Enter n value (n > 0): "))
k = 1
while not k**2<=n:
    k += 1
print(k)