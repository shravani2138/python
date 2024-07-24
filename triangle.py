#!/usr/bin/env python
# coding: utf-8

# In[2]:


# print triangle


# In[3]:


n = int(input("enetr rows"))
for i in range(0,n):
    for j in range(0,n-i-1):
        print(end = " ")
    for j in range(0,i+1):
        print("*",end = " ")
    print()


# In[ ]:




