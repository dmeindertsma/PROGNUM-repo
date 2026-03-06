#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
from numpy import sin, cos, exp, pi
from scipy.integrate import quad
import random

Expr = input("Enter a function of x: ")

a = 0
b = pi

def f(x):
    '''Return the value of the input expression'''
    return eval(Expr)

try:
    # quad integration 
    area_quad, _ = quad(f, a, b)
    print("Integral using quad():", area_quad)

    # Monte Carlo integration 
    N = 100000
    xs = np.random.uniform(a, b, N)
    ys = [f(x) for x in xs]

    area_mc = (b - a) * np.mean(ys)

    print("Integral using Monte Carlo:", area_mc)

except NameError:
    print("Error: unknown function or variable in expression.")

except SyntaxError:
    print("Error: invalid mathematical expression.")

except Exception as e:
    print("Error:", e)

# Inputting: x**4 + exp(sin(x) + cos(x))
# To demonstrate the errors: x**4 + unknown(x), y or wrong etc

