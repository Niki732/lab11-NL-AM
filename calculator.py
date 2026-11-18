"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
#https://github.com/Niki732/lab11-NL-AM
#Partner 1: Niki Lin
#Partner 2: Aaesha Mahurkar

import math
def add(a, b): 
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if a==0:
        raise ZeroDivisionError("Cannot divide by zero")
    return b/a

def logarithm(a, b):
    if a<=1 or a == 1 or b <= 0:
        raise ValueError("Invalid logarithm input")
    return math.log(b,a)

def exponent(a,b):
    return a**b




