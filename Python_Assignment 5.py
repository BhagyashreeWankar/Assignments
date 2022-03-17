#!/usr/bin/env python
# coding: utf-8

# ### 1. What does an empty dictionary's code look like?

# In[1]:


Dict = {}
print("Empty Dictionary",Dict)


# ### 2. What is the value of a dictionary value with the key &#39;foo&#39; and the value 42?

# In[4]:


Dict1 = {'foo':42} 
print("Values:",Dict1.values())


# In[5]:


Dict1.keys()


# ### 3. What is the most significant distinction between a dictionary and a list?

# In[ ]:


List -
     1. Collection of various elements just like an array
     2. Placing all elements inside [],
     3. Indices are integer values starts with 0
     4. Lists are mutable in nature
     5. Sort() method sorts the elements in ascending or descending order
    
Dictionary -
     1. Collection of elements in the hashed structure as key-value pairs
     2. Placing all key-value pairs inside curly brackets({})
     3. The keys in the dictionary are any given data type
     4. Dictionaries are mutable, but keys do not allow duplicates
     5. Sort() method sorts the keys in the dictionary by default   


# ### 4. What happens if you try to access spam[&#39;foo&#39;] if spam is {&#39;bar&#39;: 100}?

# In[6]:


spam = {'bar':100}
spam['foo']


# ### 5. If a dictionary is stored in spam, what is the difference between the expressions &#39;cat&#39; in spam and &#39;cat&#39; in spam.keys()?

# In[ ]:


- There is no difference . The in operator checks wheathe a value exists as a key in the dictionary.


# ### 6. If a dictionary is stored in spam, what is the difference between the expressions &#39;cat&#39; in spam and &#39;cat&#39; in spam.values()?

# In[ ]:


- 'cat' in spam checks whether there is a 'cat' key in the dictionary while 'cat' in spam.values() checks whether there is a value 'cat' for 
    one of the keys in spam


# ### 7. What is a shortcut for the following code?
# ### if &#39;color&#39; not in spam:
# ### spam[&#39;color&#39;] = &#39;black&#39;

# In[ ]:


Shortcut of the above code is

'color' not in spam.keys()


# ### 8. How do you &quot;pretty print&quot; dictionary values using which module and function?

# In[13]:


# Within pprint module there is a function with the same name pprint()
import pprint
dct_arr = [
  {'Name': 'abc', 'Age': '23', 'Country': 'India'},
  {'Name': 'xyz', 'Age': '44', 'Country': 'India'}
]
pprint.pprint(dct_arr)

