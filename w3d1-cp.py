"""
Program: writing functions
Author: Evan Khoo
Purpose: Writing and using own functions
Date: 01/18/2022
IDE: Visual Studios Code
"""

def main():
    s_odometer = float(input("Enter the first odometer reading (miles): "))
    e_odometer = float(input("Enter the second odometer reading (miles): "))
    fuel       = float(input("Enter the amount of fuel used (gallons): "))

    mpg = miles_per_gallon(s_odometer, e_odometer, fuel)
    lp100k = lp100k_from_mpg(mpg)

    print(f"You are getting {mpg:.2f} miles per gallon.")
    print(f"You are getting {lp100k:.2f} kilometers per liter.")

def miles_per_gallon(s_odometer, e_odometer, fuel):
    mpg = ((e_odometer-s_odometer)/fuel)
    return mpg

def lp100k_from_mpg(mpg):
    lp100k = 235.215/mpg
    return lp100k

main()