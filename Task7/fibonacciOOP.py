#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Fibonacci:
    """Class for calculating Fibonacci sequence"""
    def __init__(self,N,M):
        self.N=N
        self.M=M
        
    def fibo(self):
        """ Return the Fibonacci numbers less than N that can be divided by M.
        This function is written by dmeindertsma on 25-02-2026.
        Parameters: N,M
        """
# Fibonacci sequence less than N
    
        x=[0,1]
        while len(x)< self.N:
            x.append(x[-2]+x[-1])
        
# Numbers that can be divided by M
    
        result=[]
        for value in x:
            if value%self.M==0:
                result.append(value)
        return result

    def nth_term(self):
        """
        Return the N-th Fibonacci number (0-indexed)
        """
        x = [0, 1]
        while len(x) < self.N:
            x.append(x[-2] + x[-1])
        return x[-1]  # N-th term
    
fib = Fibonacci(N=100, M=7)

# N-th term
print("100th Fibonacci number:", fib.nth_term())

# Fibonacci numbers < N-th term divisible by 7
print("Fibonacci numbers divisible by 7:", fib.fibo())


# In[ ]:




