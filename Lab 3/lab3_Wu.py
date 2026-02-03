"""
Justin Wu
Feb 3, 2026
Lab 3, examples of conditional statements and loops is python
"""
print("-----example 1: set-up of conditional statements -----")
#conditional statements states the flow the program
age = 11
if (age >=21 and age<=100):
    print("You are an adult!")
elif (age<21 and age>=12):
    print("You are a teenager")
elif (age<12 and age>0): 
    print("You are a kid")    
else:
    print("Unable to read age")

print("\n-----example 2: for loop -----")
for n in range(9, 0, -1):
    print(n)

# for loop in a list
print("\n-----example 3: for loop in a list -----")
numbers = [3,6,1,-8,9,-5]
count_negative = 0
for m in numbers:
    if m<0:
        count_negative += 1

else:
    print(f"There is/are {count_negative} negative numbers")
#for-else, the else statement will run only after the completion of all iterations in the for loop

print('\nEND OF PROGRAM!')

print("\n-----example 4: while loop as a counter -----")
#while loop to print for, 3 to 5, inclusive, step of 2, output --> -3 -1 1 3 5
x = -3
while x <= 5:
    print(x, end="\n")
    x += 2

print("\n-----example 5: while loop to validate an input -----")
# program collects a number from the user and print if the number is even or odd
# after it, the program will ask the user if another number will be tested
# if the user types 'y' or 'Y", then the program will run again
# if the user types any other character that is not 'y' or 'Y', the program will stop

decision_user = 'y'
user_number = 0

while True:
    user_number = int(input("Enter a number: "))
    if user_number%2 == 0 and user_number !=0 :
        print(f"{user_number} is EVEN")
    elif user_number == 0:
        print("The number is zero")
    else:
        print(f"{user_number} is ODD")
    
    decision_user = input("Do you want another run. y or Y to continue: ")
    if decision_user != 'y' and decision_user != 'Y':
        break

print("\n----- Lab Exercise 1: use 'while' loop to validate that the 'user_number' is between 1 and 9 -----")
user_number = int(input("Enter a number between 1 and 9: "))

while user_number < 1 or user_number > 9:
    print("Invalid input. Please enter a number between 1 and 9.")
    user_number = int(input("Enter a number between 1 and 9: "))

print(f"Valid number entered: {user_number}")

print("\n----- Lab Exercise 2: use loop to allow user to guess the number three times. If the user guesses the number before the third attempt, the program should end(break). -----") 
secret_number = 7
attempts = 0

while attempts < 3:
    guess = int(input("Guess the secret number (between 1 and 10): "))
    attempts += 1
    if guess == secret_number:
        print("Congratulations! You've guessed the correct number.")
        break
    elif attempts == 1:
        print("Incorrect guess. Try again. You have 2 attempts left")
    elif attempts == 2:
        print("Incorrect guess. Try again. You have 1 attempts left")
    else:
        print("Sorry, you are out of attempts and you did not guess the number.")