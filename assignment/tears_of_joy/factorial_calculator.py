"""
10. Factorial calculator
Calculate the factorial of a number n entered by the user using a while loop.
Expected output: 
Enter n: 5 
Factorial: 120
"""

product =1
n = int(input("Enter n: "))
while n >= 1:
    product = product * n
    n = n - 1
print(product)
