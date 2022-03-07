"""
Program: Prove Milestone 03
Author: Evan Khoo
Purpose: Prove that you can write functions 
with parameters and call those functions with arguments.
Date: 01/22/2022
IDE: Visual Studios Code
"""

# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing
import random

def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500
    diameter = 15
    space = 5
    interval = diameter + space
    x = 100
    y = 300

    # Call the start_drawing function in the draw2d.py library
    # which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Draw a pine tree.
    tree_center_x = 170
    tree_bottom = 100
    tree_height = 200

    # Draw another pine tree.
    tree_center_y = 90
    tree_bottom_2 = 70
    tree_height_2 = 220

    
    

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    sky = draw_sky(canvas, scene_width, scene_height, x, y, diameter)
    ground = draw_ground(canvas, scene_width, scene_height)
    pine_tree = draw_pine_tree(canvas, tree_center_x, tree_bottom, tree_height)
    pine_tree_2 = draw_pine_tree(canvas, tree_center_y, tree_bottom_2, tree_height_2)

    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.
def draw_sky(canvas, scene_width, scene_height, x, y, diameter):
    random.seed(42)
    """Draw the sky and all the objects in the sky."""
    draw_rectangle(canvas, 0, scene_height / 3,
        scene_width, scene_height, width=0, fill="sky blue")

    draw_rectangle(canvas, x+ 238, y+40, 
        x+ 240, y+50, width=0, fill="medium blue")
    draw_rectangle(canvas, x+ 248, y+20, 
        x+ 250, y+35, width=0, fill="medium blue")
    draw_rectangle(canvas, x+ 280, y+0, 
        x+ 282, y+10, width=0, fill="medium blue")
    draw_rectangle(canvas, x+ 260, y+25, 
        x+ 262, y+40, width=0, fill="medium blue")
    draw_rectangle(canvas, x+ 300, y-20, 
        x+ 302, y-5, width=0, fill="medium blue")
    draw_rectangle(canvas, x+ 248, y-30, 
        x+ 250, y-20, width=0, fill="medium blue")

    draw_sun(canvas, x-130, y+110, diameter+100)
    draw_cloud(canvas, x + 210, y+50, diameter+40)
    draw_cloud(canvas, x+250, y+75, diameter+30)
    draw_cloud(canvas, x + 270, y+50, diameter+40)
    draw_cloud(canvas, x+240, y+50, diameter+20)
    

def draw_sun(canvas, x, y, diameter):
    draw_oval(canvas, x, y, x + diameter, y + diameter, fill="yellow2")

def draw_cloud(canvas, x, y, diameter):
    draw_oval(canvas, x , y , x + diameter, y + diameter, fill="white")

def draw_ground(canvas, scene_width, scene_height):
    """Draw the ground and all the objects on the ground."""
    draw_rectangle(canvas, 0, 0,
        scene_width, scene_height / 3, width=0, fill="tan4")

def draw_pine_tree(canvas, center_x, bottom, height):
    """Draw a single pine tree.
    Parameters
        canvas: The canvas where this function
            will draw a pine tree.
        center_x, bottom: The x and y location in pixels where
            this function will draw the bottom of a pine tree.
        height: The height in pixels of the pine tree that
            this function will draw.
    Return: nothing"""
    trunk_width = height / 10
    trunk_height = height / 8
    trunk_left = center_x - trunk_width / 2
    trunk_right = center_x + trunk_width / 2
    trunk_top = bottom + trunk_height

    # Draw the trunk of the pine tree.
    draw_rectangle(canvas, trunk_left, trunk_top, trunk_right, bottom, 
    outline="gray20", width=1, fill="tan3")
    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = center_x - skirt_width / 2
    skirt_right = center_x + skirt_width / 2
    skirt_top = bottom + height

    # Draw the crown (also called skirt) of the pine tree.
    draw_polygon(canvas, center_x, skirt_top,
        skirt_right, trunk_top,
        skirt_left, trunk_top,
        outline="gray20", width=1, fill="dark green")

# Call the main function so that
# this program will start executing.
main()

#Pseudo code
"""
import random

def draw_cloud(canvas, width, height, x_min, x_max, y_min, y_max):
    for i in range (0, 4):
        x_start = random.randrange(x_min, x_max)
        y_start = random.randrange(y_min, y_max)
    count()

def draw_clouds (number_of_clouds):
    for i in range (0, number_of_clouds):
        draw_cloud(...)

import math
def calucluate_circle_area(radius):
    return math.pi*radius**2
area = calculate_circle_area(5)
print(area)


str=input("please enter your name: )
    for i in range (0, len(str), 2):
        print(str(i))
    
"""