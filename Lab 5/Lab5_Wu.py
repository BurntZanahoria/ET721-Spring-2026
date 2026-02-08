"""
Justin Wu
Feb 5, 2026
Lab 5, Functions
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
# Guess number is a constant
GUESS_NUMBER = 5

# Generate random number between 1 and 10
random_num = generate_random_number(1, 10)

# Compare random number with guess number
compare_numbers(random_num, GUESS_NUMBER)