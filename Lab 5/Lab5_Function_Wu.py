"""
Justin Wu
Feb 5, 2026
Lab 5, functions
"""
import math 
# Example 1
def area_rectangle(width, length):
    return width*length

# void function does not return a value
def print_area_results(width,length,area):
    print(f"The area of rectangle of {width} and {length} is {area}")

# Example 2: calculate the distance of two points
# distance = square_root of ( (x2-x1)^2 + (y2-y1)^2)
# function 1) collect a number bewteen 1 and 10
def collectnum(point):
    num = int(input(f"Enter a number for {point}: "))
    # use a loop to recollect the number if the number is not between 1 and 10
    while(num<1 or num>10):
        num = int(input("Invalid! Enter a number between 1 and 0: "))

    return num

# function that calculates and returns the distance
# distance = square_root of ( (x2-x1)^2 + (y2-y1)^2)
def calculate_distance(x1,x2,y1,y2):
    return math.sqrt(math.pow((x2-x1),2) + math.pow((y2-y1),2))

# function to print the result
def print_distance(x1,x2,y1,y2,distance):
    print(f"The distance of point ({x1},{y1}) and ({x2},{y2}) is {round(distance,2)}")

# EXERCISE