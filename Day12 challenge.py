#!/usr/bin/env python
# coding: utf-8

# ## Day 12 challenge

# # FILE HANDLING

# ## 1. create and open a file 30 days 30 hours operations

# In[11]:


file1=open("30 days 30 hours operations.txt", "w")


# ## 2. Write data in it have completed 10 days successfully

# In[12]:


file1.write("I have completed 10 days successfully\n")
file1.close()


# ## Read what I written in that file

# In[13]:


file1=open("30 days 30 hours operations.txt", "r")
print(file1.read())
file1.close()


# ## 3. Append the data your name in to it

# In[14]:


file1=open("30 days 30 hours operations.txt", "a")
file1.write("Myself K. Kamalakannan\n")
file1.close()


# ## Read what I append in to that file

# In[16]:


file1=open("30 days 30 hours operations.txt", "r")
print(file1.read())


# ## 4. Close the file

# In[17]:


file1.close()

