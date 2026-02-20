#!/usr/bin/env python
# coding: utf-8

# In[3]:


D=float(input("Day as a floating point number:"))
M=float(input("Month as a number:"))
Y=float(input("Year:"))
JD = 367*Y -7*(Y+(M+9)//12)//4 - 3*((Y+(M-9)//7)//100 + 1)//4 + (275*M)//9 + D + 1721029-0.5
print(f"The Julian Date for {D, M, Y} is: {JD}")


# In[5]:


D=float(input("Day as a floating point number of date 1:"))
M=float(input("Month as a number of date 1:"))
Y=float(input("Year of date 1:"))
JD = 367*Y -7*(Y+(M+9)//12)//4 - 3*((Y+(M-9)//7)//100 + 1)//4 + (275*M)//9 + D + 1721029-0.5
print(f"The Julian Date for {D, M, Y} is: {JD}")

d=float(input("Day as a floating point number of date 2:"))
m=float(input("Month as a number of date 2:"))
y=float(input("Year of date 2:"))
jd = 367*y -7*(y+(m+9)//12)//4 - 3*((y+(m-9)//7)//100 + 1)//4 + (275*m)//9 + d + 1721029-0.5
print(f"The Julian Date for {d, m, y} is: {jd}")
x=jd-JD
print(f"The number of days between date 1 and date 2 in the Gregorian calendar is: {x}")


# In[ ]:




