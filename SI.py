#!/usr/bin/env python
# coding: utf-8

# In[15]:


#simple interest


# In[43]:


def simple_interest(p,t,r):
    print("The principal is ", p)
    print("The time is ", t)
    print("The rate is ", r)
    si = (p * t * r)/100
    print("Simple_interest is ", si)
    return si

# Driver code
simple_interest(8, 6, 8)


# In[ ]:




