#!/usr/bin/env python
# coding: utf-8

# ### Write a Python Program to Find LCM?

# In[1]:


def compute_lcm(x, y):
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm

num1 = 54
num2 = 24

print("The L.C.M. is", compute_lcm(num1, num2))


# ### Write a Python Program to Find HCF?

# In[3]:


def compute_hcf(x, y):

    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i 
    return hcf

num1 = 54 
num2 = 24

print("The H.C.F. is", compute_hcf(num1, num2))


# ### Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal?

# In[4]:


dec = 144

print("The decimal value of",dec,"is:")
print(bin(dec),"in binary:")
print(oct(dec),"in Octal:")
print(hex(dec),"in Octal:")


# ### Write a Python Program To Find ASCII value of a character?

# In[6]:


c = 'p'
print("ASCII value of "+ c + " is",ord(c))


# ### Write a Python Program to Make a Simple Calculator with 4 basic mathematical operations?

# In[2]:


def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y

print("Select Operation:")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    choice = input("Enter Choice(1/2/3/4):")
    
    if choice in ('1','2','3','4'):
        num1 = float(input("Enter first number"))
        num2 = float(input("Enter second number"))
        
        if choice == '1':
            print(num1,"+",num2,"=",add(num1,num2))
        elif choice == '2':
            print(num1,"-",num2,"=",sub(num1,num2))
        elif choice == '3':
            print(num1,"*",num2,"=",mul(num1,num2))
        elif choice == '4':
            print(num1,"/",num2,"=",div(num1,num2))
            
        next_cal = input("Lets do the next calculation(yes/no)")
        
        if next_cal == "no":
            break
    else:
        print("Invalid input")
    
    
    


# In[ ]:




