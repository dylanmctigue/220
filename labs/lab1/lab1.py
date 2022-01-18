"""
Dylan McTigue
lab1.py
Finding monthly interest rate
I did not share my code or discuss my code with anyone. All of this work is mine.
"""

interest_rate = eval(input("enter annual interest rate: "))
billing_cycle_days = eval(input("enter days in billing cycle: "))
previous_balance = eval(input("enter Previous Balance: "))
payment_amount = eval(input("enter Payment Amount: "))
day_payment_made = eval(input("enter day of cycle when payment was made: "))

step1 = previous_balance * billing_cycle_days
step2 = payment_amount * (billing_cycle_days - day_payment_made)
step3 = step1 - step2
avg_daily_balance = step3 / billing_cycle_days
monthly_interest_charge = avg_daily_balance * (interest_rate / 100 / 12)
rmonthly_interest_charge = round(monthly_interest_charge, 2)

print("Your monthly interest charge is $", rmonthly_interest_charge)
