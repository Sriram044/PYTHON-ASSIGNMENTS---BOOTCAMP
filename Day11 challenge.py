#!/usr/bin/env python
# coding: utf-8

# ## Day 11 challenge

# # MODULES

# ## 1. Create a python module with list and import the module in another .py file and change the value in list

# In[1]:


import Day11_external as external
external.ext_func(external.list1)


# In[2]:


external.list1[0]='Kamalakannan'
external.ext_func(external.list1)


# In[12]:


list2=["MGR", "jayalalitha", "karunanithi", "kamarajar"]
external.ext_func(list2)


# ## 2. Install pandas package (try to import the package in a python file)

# In[13]:


pip install pandas


# ## 3. Import a module that picks random number and write a program to fetch a random number from 1 to 100 on every run

# In[14]:


import numpy as py
py.random.randint(low=1, high=100)


# In[15]:


py.random.randint(low=1, high=100)


# In[16]:


py.random.randint(low=1, high=100, size=10)


# ## 4. Import sys package and find the python path

# In[19]:


import sys
sys.maxsize


# In[20]:


sys.path


# In[21]:


sys.version


# In[27]:


sys.argv[1]


# ## 5. Try to install a package and uninstall a package using pip

# In[3]:


pip install django


# In[ ]:




