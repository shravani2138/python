#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#extract each digit from an integer in the reverse order.


# In[ ]:


number = 7536
print("Given number", number)
while number > 0:
    digit = number % 10
    number = number // 10
    
    print(digit, end=" ")

