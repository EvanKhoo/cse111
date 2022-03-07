"""
Program: Team Activity 1
Author: Evan Khoo
Purpose: practice calling existing functions.
Date: 01/12/2022
IDE: Visual Studios Code
"""

from datetime import datetime

print("To exit shopping please enter 0 for both price and quantity")

#building users cart asking for price and quantity
price = float(input("Please enter the price: $"))
quantity = float(input("Please enter the quantity: "))
cart = float((price*quantity))
print(f"\nYou cart total is: ${cart}\n")
while price != 0:
    price = float(input("Please enter the price: $"))
    quantity = float(input("Please enter the quantity: "))
    cart = (cart+(price*quantity))
    print(f"\nYou cart total is: ${cart}\n")

sub_total = cart
date_time = datetime.now()
week_date = date_time.weekday()

if week_date == 1 or week_date == 2 and sub_total >= 50:
    discount = (sub_total*0.1)
    new_sub_total = (sub_total*0.9)
    tax = (new_sub_total*.06)
    total = (new_sub_total*1.06)

    print(f"Discount Amount: ${discount:.2f}")
    print(f"Sales tax amount: ${tax:.2f}")
    print(f"Total: ${total:.2f}")
elif week_date == 1 or week_date == 2 and sub_total < 50:
    difference = (50 - sub_total)
    tax = (sub_total*.06)
    total = (sub_total*1.06)

    print(f"The amount needed to recieve discount: ${difference:.2f}")
    print(f"Sales tax amount: ${tax:.2f}")
    print(f"Total: ${total:.2f}")
else:
    tax = (sub_total*0.06)
    total = (sub_total*1.06)
    print(f"Sales tax: ${tax:.2f}")
    print(f"Total: ${total:.2f}")