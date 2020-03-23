# The Collatz Sequence function
def collatz(number):
    # Check for odd or even number
    num_check = number % 2
    if num_check == 1:
        # If odd, print and return 3 * number + 1
        new_num = 3 * number + 1
        print(new_num)
        return new_num
    else:
        # If even, print and return number // 2 
        new_num = number // 2
        print(new_num)
        return new_num

# Ask for user to enter a number
print('Enter number:')
while True:
    # Catchs the ValueError exception upon invalid entry (looking for an integer)
    try:
        a_num = int(input())
        break
    except ValueError:
        print('Please enter a valid integer.')

# Calls the collatz funtion until the funtion returns a 1
while True:
    a_num = collatz(a_num)
    if a_num == 1:
        break