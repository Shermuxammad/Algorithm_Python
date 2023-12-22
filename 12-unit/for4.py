n = int(input("n = "))

number = 0

for i in range(1, int(n/2)+1):
    if n%i == 0:
        number += i
        
    if number<=2:
        print("The prime numbers are:", number)
    else:
        print("There no prime numbers! ")

            