a =  int(input("a = "))
# b =  int(input("b = "))

for i in range(1, a+1):
    num1 = 0
    for j in range(1, i+1):
        if i%j == 0:
            num1 += 1
    if num1 == 2:
        print(i)
    
# for k in range(1, b+1):
#     num2 = 0
#     for l in range(1, k+1):
#         if k%l == 0:
#             num2 += 1
#     if num2 == 2:
#         print(k)
        
        
        