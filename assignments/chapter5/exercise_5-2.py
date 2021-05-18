#!/usr/bin/env python3
# program to get a list of numbers from the user and output the largest and
# smallest number entered

user_string = ""
user_number = None
largest_number = None
smallest_number = None
while True:
    user_string = input("Enter a number: ")
    if user_string == "done":
        break
    try:
        user_number = int(user_string)
    except:
        print("invalid input")
        continue
    if largest_number is None or user_number > largest_number:
        largest_number = user_number
    if smallest_number is None or user_number < smallest_number:
        smallest_number = user_number

print("Maximum is", largest_number)
print("Minimum is", smallest_number)
