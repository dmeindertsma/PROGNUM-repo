#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

f = input("Enter a function of x, like x**2-3*x: ")
a = float(input("Enter lower limit a: "))
b = float(input("Enter upper limit b: "))

x=np.random.uniform(low=a, high=b, size=100000000)
y=eval(f)

integral=(b-a)*np.mean(y)
print(integral)


# In[ ]:




