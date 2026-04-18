"""
START

INPUT PURCHASES

IF PURCHASE > 1000 OR PURCHASE < 10000
    DISCOUNT_PERCENT = 5 
IF PURCHASE > 10000 OR PURCHASE < 50000
    DISCOUNT_PERCENT = 10 
IF PURCHASE > 50000
    DISCOUNT_PERCENT = 20
DISCOUNT = (PURCHASE * DISCOUNT_PERCENT)/100
PRINT DISCOUNT
STOP
"""

purchase = int (input("Enter Amount purchased: "))

if (purchase > 1000) or (purchase < 10000):
    discount_percent = 5
if (purchase > 10000) or (purchase < 50000):
    discount_percent = 10
if (purchase > 50000):
    discount_percent = 20

discount = (purchase * discount_percent)/100
print("discount: ",discount)

