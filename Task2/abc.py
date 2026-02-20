#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from math import sqrt
a=float(input("a = "))
b=float(input("b = "))
c=float(input("c = "))
D=b**2-4*a*c

if D==0:
    x1=(-b+sqrt(D))/(2*a)
    x2=(-b-sqrt(D))/(2*a)
    print(f"The solution for x ={x1} ")
elif D<0:
    print(f"x has no real solutions.")
else:
    x1=(-b+sqrt(D))/(2*a)
    x2=(-b-sqrt(D))/(2*a)
    print(f"The two solutions for x are: {x1} and {x2}")

