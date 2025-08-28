#task1 calulate factorial using a funtion

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

#Taking input from user
num = int(input("Enter a number: "))

#calling the function and displaying the result
result = factorial(num)
print(f"The factorial of {num} is {result}")

#Task2 using the math module for calculation

import math

#ask user for input
num = int(input("Enter a number: "))

#using math module for calculations
sqrt_val = math.sqrt(num)
log_val = math.log(num)
sine_val = math.sin(num)

#dislpay results
print(f"sqrt({num}) is {sqrt_val}")
print(f"log({num}) is {log_val}")
print(f"sine({num}) is {sine_val}")
