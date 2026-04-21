"""
5. Repeat a greeting
Ask the user for their name once, then print 'Hello, <name>!' five times using loop.
Expected output (name = Adeola): Hello, Adeola! is printed 5 times
"""
name = input("Enter your name: ")
for number in range(6):
    print("Hello, ", name,"!",sep="")
