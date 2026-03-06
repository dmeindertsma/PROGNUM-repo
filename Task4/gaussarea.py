#!/usr/bin/env python
# coding: utf-8

# In[6]:


# import numpy as np
from matplotlib import pyplot as plt
from scipy import integrate

def gauss(x, A, x0, sigma, z0):
   return A*np.exp(-(x-x0)**2/(2*sigma**2))+z0
    
A = float(input("Enter value for A: "))
x0 = float(input("Enter value for x0: "))
sig = float(input("Enter value for sig: "))
z0 = float(input("Enter value for z0: "))
xmin = float(input("Integration start: "))
xmax = float(input("Integration end: "))

Area, error = integrate.quad(gauss,xmin,xmax,args=(A, x0, sig, z0))
print(f"The area of integration: {Area}") 

x = np.linspace(xmin-5, xmax+5, 200)
y = gauss(x, A, x0, sig, z0)
x_fill = np.linspace(xmin, xmax, 200)
y_fill = gauss(x_fill, A, x0, sig, z0)

plt.plot(x, y, label="Gaussian")
plt.fill_between(x_fill, y_fill, color="lightblue", label=f"Area = {Area:.3f}")
plt.title("Coursework 4.17")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.show()


# In[ ]:




