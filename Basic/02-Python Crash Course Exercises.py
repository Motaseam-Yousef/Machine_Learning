#!/usr/bin/env python
# coding: utf-8

# ___
# 
# <a href='http://www.pieriandata.com'> <img src='../Pierian_Data_Logo.png' /></a>
# ___
# # Python Crash Course Exercises 
# 
# This is an optional exercise to test your understanding of Python Basics. If you find this extremely challenging, then you probably are not ready for the rest of this course yet and don't have enough programming experience to continue. I would suggest you take another course more geared towards complete beginners, such as [Complete Python Bootcamp](https://www.udemy.com/complete-python-bootcamp/?couponCode=PY20)

# ## Exercises
# 
# Answer the questions or complete the tasks outlined in bold below, use the specific method described if applicable.

# ** What is 7 to the power of 4?**

# In[1]:


7**4


# ** Split this string:**
# 
#     s = "Hi there Sam!"
#     
# **into a list. **

# In[2]:


s = "Hi there Sam!"


# In[3]:


s.split()


# ** Given the variables:**
# 
#     planet = "Earth"
#     diameter = 12742
# 
# ** Use .format() to print the following string: **
# 
#     The diameter of Earth is 12742 kilometers.

# In[10]:


planet = "Earth"
diameter = 12742


# In[12]:


print("The diameter of {} is {} kilometers.".format(planet,diameter))


# ** Given this nested list, use indexing to grab the word "hello" **

# In[14]:


lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]


# In[15]:


lst[3][1][2]


# ** Given this nested dictionary grab the word "hello". Be prepared, this will be annoying/tricky **

# In[17]:


d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}


# In[18]:


d['k1'][3]['tricky'][3]['target'][3]


# ** What is the main difference between a tuple and a list? **

# In[23]:


# Tuple is immutable


# ** Create a function that grabs the email website domain from a string in the form: **
# 
#     user@domain.com
#     
# **So for example, passing "user@domain.com" would return: domain.com**

# In[20]:


def domainGet(email):
    return email.split("@")[1]
    


# In[21]:


domainGet('user@domain.com')


# ** Create a basic function that returns True if the word 'dog' is contained in the input string. Don't worry about edge cases like a punctuation being attached to the word dog, but do account for capitalization. **

# In[23]:


def findDog(string):
    # convert to lower
    string=string.lower()
    return 'dog' in string


# In[24]:


findDog('Is there a dog here?')


# ** Create a function that counts the number of times the word "dog" occurs in a string. Again ignore edge cases. **

# In[29]:


def countDog(string):
    # convert to lower
    string=string.lower()
    return string.count("dog")


# In[30]:


countDog('This dog runs faster than the other dog dude!')


# ** Use lambda expressions and the filter() function to filter out words from a list that don't start with the letter 's'. For example:**
# 
#     seq = ['soup','dog','salad','cat','great']
# 
# **should be filtered down to:**
# 
#     ['soup','salad']

# In[52]:


seq = ['soup','dog','salad','cat','great']


# In[56]:


lst=[]
for i in range(len(seq)):
    x=str(seq[i])
    if x.startswith('s'):
        lst.append(seq[i])


# In[57]:


print(lst)


# In[76]:


list(filter(lambda x:str(x).startswith('s'),seq))


# In[81]:


list(filter(lambda x:x[0]=='s',seq))


# ### Final Problem
# **You are driving a little too fast, and a police officer stops you. Write a function
#   to return one of 3 possible results: "No ticket", "Small ticket", or "Big Ticket". 
#   If your speed is 60 or less, the result is "No Ticket". If speed is between 61 
#   and 80 inclusive, the result is "Small Ticket". If speed is 81 or more, the result is "Big    Ticket". Unless it is your birthday (encoded as a boolean value in the parameters of the function) -- on your birthday, your speed can be 5 higher in all 
#   cases. **

# In[73]:


def caught_speeding(speed, is_birthday):
    if is_birthday==True:
        speed-=5
    print(speed)
    if speed<=60:
        return "No Ticket"
    elif 61<=speed<=80:
        return "Small Ticket"
    elif speed>80:
        return "Big Ticket"
    pass


# In[74]:


caught_speeding(81,True)


# In[75]:


caught_speeding(81,False)

