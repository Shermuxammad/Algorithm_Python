n = int(input("Enter n value (n > 0): "))
while n<=0:
    print("n value must be bigger than 0. Enter valud number!")
    n = int(input("Enter n value (n > 0): "))
k = 1
while not k**2>n:
    k += 1
result = k**2
print(f"Given number is {n} and  (k**2 > n) second number is {k}, the power of k = {result} is bigger than {n}")