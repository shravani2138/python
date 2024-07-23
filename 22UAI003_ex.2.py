#!/usr/bin/env python
# coding: utf-8

# In[1]:


d1={"apple":50,"mango":100,"kivi":200,"banana":40}


# In[4]:


d1.keys()


# In[5]:


d1.values()


# In[6]:


#adding new element
d1["grapes"]=50


# In[7]:


d1


# In[8]:


#changing and exsting element


# In[9]:


d1["apple"]=100


# In[10]:


d1


# In[12]:


d2={"orange":45,"papaya":120,"chiku":80,"watrmelon":150}


# In[13]:


d2


# In[14]:


#update one dict


# In[15]:


d1.update(d2)


# In[16]:


d1


# In[17]:


#poping an element


# In[18]:


d1.pop("grapes")


# In[20]:


#string 


# In[21]:


v1 = "hello"
v2 = "world"


# In[25]:


v1,v2


# In[26]:


#concatenete


# In[27]:


v1+v2


# In[28]:


print(v1+v2)


# In[29]:


#access substring


# In[32]:


substring = v2[0:8]


# In[33]:


print("substring",substring)


# In[ ]:





# In[34]:


# numpay


# In[1]:


import numpy 

arr = numpy.array([1,2,3,4,5]) 
print(arr)


# In[3]:


import numpy as np

arr = np.array([1,2,3,4,5])
print(arr)


# In[4]:


import numpy as np

arr = np.array([1,2,3,4,5])
print(arr[3])
print(arr[0:3])


# In[21]:


import numpy as np

arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr)
print(arr[1][1])
print(arr[0,4],[2,3])
print(arr[1,4])


# In[27]:


import numpy as np

arr = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]])
print(arr)
print(arr[1][3])
print(arr[2,4],[2,3])


# In[ ]:




