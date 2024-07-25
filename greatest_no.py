#!/usr/bin/env python
# coding: utf-8

# In[1]:


#greatest number in three number


# In[3]:


a = int(input("enter first number"))
b = int(input("enter second number"))
c = int(input("enetr third number"))

if a>b:
    if b>c:
        print("greatest number is :",a)
    else:
        print("greatest number is :",c)
else:
    if b>c:
        print("greatest number is :",b)
    else:
        print("greatest number is :",c)


# In[ ]:




