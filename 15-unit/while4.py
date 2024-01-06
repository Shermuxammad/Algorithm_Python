# Input an integer variable
n = int(input("Enter integer value positive than 0 (n > 0): "))

# Ensure (n>0)or not
while n <= 0:
    print("n value must be greater than 0. Please enter valid value!")
    n = int(input("Enter integer value: "))
# Include the text to a variable
result = "It is power of 3"
# Ensure (n>0)or not
while n > 1:
    if n%3!=0:
        result = "It is not power of 3"
        break
    n/=3
# Output the result
print(result)
    
    