#!/usr/bin/env python
min_age=18

user_age=input("Enter your age:")
user_age=int(user_age)

if user_age >= min_age:
    print("You may enter the nightclub!")
else:
    print("You must be at least 18 to enter!")
