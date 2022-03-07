"""
Program: Team Activity 2
Author: Evan Khoo
Purpose: practice calling existing functions.
Date: 01/19/2022
IDE: Visual Studios Code
"""

from datetime import datetime,timedelta

def main():
    gender    = input("Please enter your gender (M or F): ")
    birth_day = input("Enter your birthdate (YYYY-MM-DD): ")
    weight    = float(input("Enter your weight in U.S. pounds: "))
    height    = float(input("Enter your height in U.S. inches: "))

    age  = compute_age(birth_day)
    kilo = lbs_to_kilo(weight)
    cm   = in_to_cm(height)
    bmi  = body_mass_index(kilo, cm)
    bmr  = basal_metabolic_rate(gender, kilo, cm, age)

    print(f"Age (years): {age}")
    print(f"Weight (kg): {kilo:.1f}")
    print(f"Height (m): {(cm/100):.1f}")
    print(f"Body mass index: {bmi:.1f}")
    print(f"Basal metabolic rate (kcal/day): {bmr:.1f}")
    pass

def compute_age(birth_day):
    birthdate = datetime.strptime(birth_day, "%Y-%m-%d")
    today = datetime.now()
    age = today.year - birthdate.year

    if birthdate.month > today.month or \
        (birthdate.month == today.month and \
            birthdate.day > today.day):
        age -= 1
    return age

def lbs_to_kilo(weight):
    kilo = (weight/2.205)
    return kilo

def in_to_cm(height):
    cm = (height*2.54)
    return cm

def body_mass_index(kilo, cm):
    bmi = ((10000*kilo)/(cm**2))
    return bmi

def basal_metabolic_rate(gender, kilo, cm, age):
    if gender == "f" or gender == "F":
        bmr = (447.593+(9.247*kilo)+(3.098*cm)-(4.330*age))
    else:
        bmr = (88.362+(13.397*kilo)+(4.799*cm)-(5.677*age))
    return bmr

main()