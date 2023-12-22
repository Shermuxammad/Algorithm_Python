a = int(input("Enter a = "))
b = int(input("Enter b = "))

num1 = 0
num2 = 0

for i in range(1, a+1):
    if a%i == 0:
        num1 += 1
    print(num1)

for j in range(1, b+1):
    if b%j == 0:
        num2 += 1
    print(num2)

    