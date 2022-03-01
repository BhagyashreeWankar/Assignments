#!/usr/bin/env python
# coding: utf-8

# ### 1.Write a Python Program to Display Fibonacci Sequence Using Recursion?

# In[1]:


def rec_febo(n):
    if n <=1:
        return n
    else:
        return (rec_febo(n-1)+rec_febo(n-2))
    
nterms = 10

if(nterms <= 0):
    print("Please Enter Positive Integer")
else:
    print("Fibonacci Sequence")
    for i in range(nterms):
        print(rec_febo(i))


# ### 2.Write a Python Program to Find Factorial of Number Using Recursion?

# In[5]:


def rec_fact(n):
    if n==1:
        return n
    else:
        return n*rec_fact(n-1)
       

num = int(input("Enter number"))

if num < 0:
    print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    print("The factorial of", num, "is", rec_fact(num))


# ### 3. Write a Python Program to calculate your Body Mass Index?

# In[7]:


height = float(input("Enter height in feet"))
weight = float(input("Enter weight in kg"))
print("Body Mass Index of Body is:",round(weight/(height*height),2))


# ### 4.Write a Python Program to calculate the natural logarithm of any number?

# In[10]:


import math
print("math.log(100.2) :",math.log(100.2))
print("math.log(100.72) : ",math.log(100.72))
print("math.log(math.pi) : ",math.log(math.pi))


# ### 5. Write a Python Program for cube sum of first n natural numbers?

# In[15]:


def sumOfSeries(n):
    sum = 0
    for i in range(1,n+1):
        sum += i*i*i
    return sum
        
num = int(input("Enter Number"))

print("cube sum of first n natural numbers:",sumOfSeries(num))
    
 


# In[ ]:




