#!/usr/bin/env python
# coding: utf-8

# In[5]:


def factorial(n):
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        while(n > 1):
            fact *= n
            n -= 1
        return fact
num = 5
print("factorial of",num,"is",factorial(num))


# In[ ]:




