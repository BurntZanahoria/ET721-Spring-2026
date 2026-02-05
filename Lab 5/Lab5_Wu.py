"""
Justin Wu
Feb 5, 2026
Lab 5, Function
"""
import math
from Lab5_Function_Wu import *

print("\n ----- Example 1: user-defined function ")
w = 10
length = 2
a = area_rectangle(w,length)
print_area_results(w,length,a)

print("\n ----- Example 2: calculate the distance of two points ")
x1 = collectnum('x1')
x2 = collectnum('x2')
y1 = collectnum('y1')
y2 = collectnum('y2')

# testing
# print(f"({x1},{x2}) ({y1},{y2})")

# testing 2
# print(f"distance = {calculate_distance(x1,x2,y1,y2)}")

distance = calculate_distance(x1,x2,y1,y2)
print_distance(x1,x2,y1,y2,distance)

print(f"\nEXERCISE")