"""
Program: tire_volume
Author: Evan Khoo
Purpose: Take user input, perform arthimetic, display result
Date: 01/08/2022
IDE: Visual Studios Code
"""
import math
from datetime import datetime

#tire width
w = int(input("Enter the width of the tire in mm (ex 205): "))
#aspect ration
a = int(input("Enter the aspect ratio of the tire (ex 60): "))
#wheel diameter
d = int(input("Enter the diameter of the wheel in inches (ex 15): "))
#tire volume
v = (((math.pi * (w ** 2)*a)*((w*a)+(2540*d)))/10000000000)

print(f"The approximate volume is {v:.2f} liters")

date_time = datetime.now()
with open("volume.txt", mode = "at") as volume_files:
    print(f"{date_time:%Y-%m-%d}, {w}, {a}, {d}, {v:.2f}, ", file=volume_files)
