"""
Program: boxes
Author: Evan Khoo
Purpose: Practice using built in python functions
Date: 01/11/2022
IDE: Visual Studios Code
"""
import math

items = float(input("Enter the number of items: "))
items_box = float(input("Enter the number of items per box: "))

#required boxes
boxes = items/items_box

print (f"""For {items} items, packing {items_box} items in each box, 
you will need {math.ceil(boxes)} boxes.""")