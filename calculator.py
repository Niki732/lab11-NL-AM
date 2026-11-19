#https://github.com/Niki732/lab11-NL-AM
#Partner 1: Niki Lin
#Partner 2: Aaesha Mahurkar

"""
#calculator.py
#- Defines functions used to create a simple calculator

#One function per operation, in order.
"""

import math
def square_root(a):
    if a<0:
        raise ValueError("Value must be greater than 0")
    return math.sqrt(a)
def hypotenuse(a,b):
    return math.hypot(a,b)
def add(a, b): 
    return a+b

def subtract(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    if a==0:
        raise ZeroDivisionError("Cannot divide by zero")
    return b/a

def logarithm(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Invalid logarithm input")
    return math.log(b,a)

def exp(a,b):
    return a**b
sub= subtract
log=logarithm



