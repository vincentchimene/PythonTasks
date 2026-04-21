"""
7. Multiplication table [for loop]
Print the 7 times table from 7x1 to 7x12.
Expected output: 
7 x 1 = 7
7 x 2 = 14 
...
"""

for number in range(1,13):
    print(f'7  X  {number:>2}  =  {7*number:>2}', sep="")
