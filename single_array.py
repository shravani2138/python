#!/usr/bin/env python
# coding: utf-8

# In[1]:


# basic operations on single array


# In[3]:


import numpy as np

a = np.array([[1, 2],[3, 4]])
b = np.array([[4, 3],[2, 1]])
               
print ("Adding 1 to every element:", a + 1)
print ("\nSubtracting 2 from each element:", b - 2)
print ("\nSum of all array " "elements: ", a.sum())

print ("\nArray sum:\n", a + b)


# In[ ]:




