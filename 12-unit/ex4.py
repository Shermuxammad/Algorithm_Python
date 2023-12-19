n = int(input("N = "))
sum_of_num = 0
for i in range(1, n+1):
    if n%i==0:
        sum_of_num += i
print(sum_of_num)