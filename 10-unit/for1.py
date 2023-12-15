n = int(input("n = "))
k = int(input("How many time do you want to repeat the n: "))
if n > 0:
    for i in range(1, k+1):
        print(f"{i}-n = {n}", )
else:
    print("Error")