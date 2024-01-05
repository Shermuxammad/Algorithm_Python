# Input positive A and B integers
A = int(input('Enter positive integer A: '))
B = int(input('Enter positive integer (B<A) B: '))
# Ensure that both integers bigger than 0
if A>0 and B>0:
    # Ensure A must be bigger than B
    while A <= B:
        # Output the invalid action
        print('A must be bigger than B. Please enter valid number (A>B)')
        # Input positive A and B integers
        A = int(input('Enter positive integer A: '))
        B = int(input('Enter positive integer (B<A) B: '))
    count = 0
    # Ensure A must be bigger than B
    while A >= B:
        A -= B
        count += 1
    # Ourput the result
    print(f'B can be included {count} time(s)')
# Output the invalid result that A and B must be bugger than 0 (A&B > 0)
else:
    print('Invalid number A and B must be bigger than 0')
