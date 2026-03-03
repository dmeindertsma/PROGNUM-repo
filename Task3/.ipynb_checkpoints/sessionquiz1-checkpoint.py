#!/usr/bin/env python
# coding: utf-8

# In[14]:


masses = [1.9891e+30, 1.8986e+27, 
          5.6846e+26, 1.0243e+26, 8.6810e+25,
          5.9736e+24, 4.8685e+24, 6.4185e+23, 
          3.3022e+23, 7.349e+22, 1.25e22]
masses_new=[]

for m in masses:
    if m > 7.349e+22:
        masses_new.append(m)
             
print(masses_new)

print(masses[-5:])
Sum=sum(masses[-5:])
N=len(masses[-5:])
average_mass=Sum/N
print(average_mass)


# In[ ]:




