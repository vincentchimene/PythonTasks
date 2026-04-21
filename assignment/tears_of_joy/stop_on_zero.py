"""
11. Sentinel: stop on zero
Keep reading integers from the user. When they enter 0, stop and print the total of all entered numbers.
Expected output: Enter: 4 / Enter: 7 / Enter: 0 / Total: 11
"""

sum_of_numbers = 0
while True:
    number = int (input("Enter: "))
    sum_of_numbers = sum_of_numbers + number
    if number == 0:
        break
print(sum_of_numbers)
