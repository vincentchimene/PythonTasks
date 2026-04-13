principal = float (input("Enter Principal"))

annual_Rate = float (input("Enter Annual Rate"))

time = float (input("Enter time in years"))

monthly_rate = annual_Rate / 100 / 12

monthly_payment = principal * (monthly_rate*(1 + monthly_rate)**time) /(((1 + monthly_rate)**time) - 1)
print(monthly_payment)
