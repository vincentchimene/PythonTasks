"""
2. Print even numbers
Print all even numbers from 2 to 20 using a for loop.
Expected output: 2  4  6  8  10  12  14  16  18  20
"""
for number in range(1,21):
    if number % 2 == 0:
        print(number, end=" ")
