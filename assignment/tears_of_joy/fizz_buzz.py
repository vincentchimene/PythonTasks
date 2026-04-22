"""
12. FizzBuzz
Print numbers 1-50. For multiples of 3 print 'Fizz', multiples of 5 print 'Buzz', multiples of both print 'FizzBuzz'.
Expected output: 1  2  Fizz  4  Buzz  Fizz  7 ... FizzBuzz
"""
for numbers in range(1,51):
    if numbers % 5  == 0 and numbers % 3 == 0:
        print("FizzBuzz", end="  ")
    elif numbers % 5 == 0:
        print("Buzz", end="  ")
    elif numbers % 3 == 0:
        print("Fizz", end="  ")
    else:
        print(numbers, end="  ")

