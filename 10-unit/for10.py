# S = 1+1/2+1/3+.....+1/n

n = int(input("n = "))

harmonic = 0.0

if n > 0:
    for i in range(1, n+1):
        harmonic = 1 / i
else:
    print("Value error") 
    
print("The sum of the harmonic series up to {} terms is: {:.4f}".format(n, harmonic))  


