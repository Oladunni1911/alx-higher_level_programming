#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_number = number
if number < 0:
    coeff = -1
    last_number *= -1
else:
    coeff = 1
while last_number > 9:
    last_number %= 10
last_number *= coeff
if last_number < 6 and last_number != 0:
    print(f"Last digit of {number} is {last_number} and is less than 6 and\
 not 0")
elif last_number > 5 and last_number != 0:
    print(f"Last digit of {number} is {last_number} and is greater than 5")
else:
    print(f"Last digit of {number} is {last_number} and is 0")
