#3.7
"""(Table of Squares and Cubes) In Exercise 2.8, you wrote a script to calculate the
squares and cubes of the numbers from 0 through 5, then printed the resulting values in
table format. Reimplement your script using a for loop and the f-string capabilities you
learned in this chapter to produce the following table with the numbers right aligned in
each column.


"""
print(f'number, square, cube')
for number in range(1, 6):    
    print(f'{number:>2}{number*number:>6}{number*number*number:>4}')

