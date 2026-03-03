#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np

# Defining R, P and S

R="R"
P="P"
S="S"

Start = input(f"Choose rock: R, paper: P or scissors: S: ")        # Players input
RPS = np.array(['R', 'P', 'S'])                                    
indx = np.random.randint(0, len(RPS), 1)                           # Random respons
print(RPS[indx])

# Stating the conditions of winning or losing:

if Start==R and RPS[indx]=='S':
    print("You win!")
elif Start==P and RPS[indx]=='R':
    print("You win!")
elif Start==S and RPS[indx]=='P':
    print("You win!")
elif Start==R and RPS[indx]=='R':
    print("Tie!")
elif Start==P and RPS[indx]=='P':
    print("Tie!")
elif Start==S and RPS[indx]=='S':
    print("Tie!")
else:
    print("You lose :(")


# In[ ]:




