#!/usr/bin/env python
# coding: utf-8

# ## Day13 challenge

# # RegEX

# ## Write a python program for all the cases which can check a string contains only a certain set of characters
# ## (In this case a-z, A-Z and 0-9)

# In[1]:


import re


# In[21]:


def is_contain(string):
    char1=re.compile(r'[^a-zA-Z0-9]')
    string=char1.search(string)
    return not bool(string)
print(is_contain("65432hgfdsKMNBYU34"))
print(is_contain("43328**&^%$#@!"))


# ## Write a python program that matches a word containing 'ab'.

# In[43]:


def word_match(word):
    pattern='ab'
    if re.search(pattern, word):
        return 'found a match!'
    else:
        return 'not found a match'
print(word_match("acdb"))
print(word_match("dsfab"))


# ## Write a python program to check for a number at the end of a word/sentence

# In[25]:


def numAtEnd(string):
    text=re.compile(r'.*[0-9]$')
    if text.match(string):
        return True
    else:
        return False
print(numAtEnd("kamal@123"))
print(numAtEnd("sriram"))
print(numAtEnd("ajay@654"))


# ## Write a python program to search the numbers (0-9) of length between 1 to 3 in a given string

# In[31]:


results = re.finditer(r'([0-9]{1,3})', 'Question number 1, 2, 16 and 111 are important')
print("Number whose length between 1 to 3")
for n in results:
    print(n.group(0))


# ## write a python program to match a string that contains only uppercase letters

# In[40]:


def onlyUpper(text):
    pattern=r'[A-Z]'
    if(re.search(pattern, text)):
        return 'matched !'
    else:
        return 'unmatched !'
print(onlyUpper("SRIRAM"))
print(onlyUpper("sriram"))


# In[ ]:




