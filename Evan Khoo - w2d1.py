import math

def computer_circle_area(radius = 5):
    return radius**2*math.pi

def prompt_user_for_radius():
    user_radius = float(input("Please enter a radius: "))
    return user_radius

def display_area(area):
    print(area)

area = round(computer_circle_area(),2)

display_area(area)