#!/usr/bin/env python
# coding: utf-8

# ### 1. What are escape characters, and how do you use them?

# In[ ]:


- To insert characters that are illegal in a string, use an escape character.
- An escape character is a backslash \ followed by the character you want to insert

for ex.


# In[3]:


txt = "To insert characters that are \" illegal\" in a string "
print(txt)


# ### 2. What do the escape characters n and t stand for?

# - Escape characters \n for new line and \t for tab in sentence

# In[6]:


txt = "hello\nworld"
print(txt)


# In[7]:


txt1 = "hello\tworld"
print(txt1)


# ### 3. What is the way to include backslash characters in a string?

# - Use the syntax "\\" within the string literal to represent a singal backslash

# ### 4. The string "Howl's Moving Castle" is a correct value. Why isn't the single quote character in the word Howl's not escaped a problem?

# - The single quote character in the word Howl's is fine because you've used double quotes to mark the begining and end the string
# txt = "Howl's Moving Castle"
# print(txt)

# ### 5. How do you write a string of newlines if you don&#39;t want to use the n character?

# In[1]:


print("Hello")
print("world")


# ### 6. What are the values of the given expressions?
# 

# In[3]:


'Hello, world!'[1]


# In[4]:


'Hello, world!'[0:5]


# In[5]:


'Hello, world!'[:5]


# In[6]:


'Hello, world!'[3:]


# ### 7. What are the values of the following expressions?

# In[9]:


'Hello'.upper()


# In[10]:


'Hello'.upper().isupper()


# In[12]:


'Hello'.upper().lower()


# ### 8. What are the values of the following expressions?

# In[13]:


'Remember, remember, the fifth of July.'.split()


# In[15]:


'-'.join("There can only one.".split())


# ### 9.What are the methods for right-justifying, left-justifying, and centering a string?

# In[23]:


str = "this is string example....wow!!!";
print(str.rjust(50, '0'))


# In[25]:


print(str.ljust(50,'0'))


# In[27]:


print(str.center(50,' '))


# ### 10.What is the best way to remove whitespace characters from the start or end?

# In[28]:


"        to remove whitespace characters     ".strip()

