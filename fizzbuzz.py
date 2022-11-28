#!/usr/bin/env python
number=input("enter a number 1 to 20:")
number=int(number)
for number in range(21):
  def doFizzBuzz(number):
    if number%3==0 and number%5==0:
        print("FizzBuzz")
    elif number%3==0:
        print("Fizz")
    elif number%5==0:
        print("Buzz")
    else:
        print(number)
doFizzBuzz(number)
