"""
START
INPUT password
password_length = LENGTH OF PASSWORD
IF password_length < 8
    PRINT Very Weak
IF password_length = 8
    PRINT Weak
IF password_length > 8 or password_length < 16
    PRINT Strong
IF password_length > 16
    PRINT Very Strong
"""

password = input("Enter Amount password ")
password_length = len(password)
if password_length < 8:
    print("Very Weak")
if password_length == 8:
    print("Weak")
if password_length > 8 or password_length < 16:
    print("strong")
if password_length > 16:
    print("Very Strong")
