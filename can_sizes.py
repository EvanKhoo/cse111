"""
Program: can sizes
Author: Evan Khoo
Purpose: Calculate can storage efficiency
Date: 01/26/2022
IDE: Visual Studios Code
"""
import math

def main():
    name = ["#1 Picnic", "#1 Tall", "#2", "#2.5", "#3 Cylinder", "#5", "#6Z", "#8Z short", "#10", "#211", "#300", "#303"]
    radius = [6.83, 7.78, 8.73, 10.32, 10.79, 13.02, 5.40, 6.83, 15.72, 6.83, 7.62, 8.10]
    height = [10.16, 11.91, 11.59, 11.91, 17.78, 14.29, 8.89, 7.62, 17.78, 12.38, 11.27, 11.11]
    vol = [compute_volume(radius, height)]
    combined =[]
    complicated = []

    i = 0
    for value in name:
        combined = (*name, *vol)
        complicated.append(combined)
        print(complicated[i])
        i += 1
    

    #compute_surface_area()

def compute_volume(radius, height):
    vol = []
    i = 0
    for value in radius:
        volume = (math.pi*(radius[i]**2)*height[i])
        vol.append(round(volume, 2))
        i += 1
    return vol
    
#def compute_surface_area():

main()