# Input positive integers A and B
a = int(input('Enter positive integer A = '))
b = int(input('Enter positive integer (B < A) B = '))

# Ensure A and B is greater than 0
if a > 0 and b > 0:
    # Ensure A is greater than B
    while a <= b:
        print("A must be greater than B -> (A>B)")
        a = int(input('Enter positive integer (A > B): '))
        b = int(input('Enter positive integer B: '))
            
    empty_part = a
    while a>=b:
        a -= b
    # Output the result
    print(f"Your Empty part of the section is '{a}'")
else:
    print('A and B must be greater than 0')

