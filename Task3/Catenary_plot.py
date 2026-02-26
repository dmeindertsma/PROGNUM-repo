#!/usr/bin/env python
# coding: utf-8

# In[1]:


from matplotlib import pyplot as plt
from math import *
y=[]
for x in range(-5,6):
    a=cosh(x)
    y.append(a)
x=range(-5,6)

plt.plot(x, y, marker='o', color='r', label='cosh(x)')
plt.title("The shape of a catenary")                             
plt.ylabel("y")  
plt.xlabel("x") 
plt.grid()                                      
plt.legend()                                     
plt.show()

from matplotlib import pyplot as plt
from math import *
import numpy as np
x=np.arange(-5, 6)
y=np.cosh(x)
plt.plot(x, y, marker='o', color='r', label='cosh(x)')
plt.title("The shape of a catenary")                             
plt.ylabel("y")  
plt.xlabel("x") 
plt.grid()                                      
plt.legend()                                     
plt.show()


# In[ ]:




