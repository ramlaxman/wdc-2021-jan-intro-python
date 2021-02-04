#!/usr/bin/env python
# coding: utf-8

# In[1]:


# str.split and str.strip


# In[2]:


# str.split always returns a list of strings

s = 'abcd efgh ijkl'
s.split(' ')  # return a list of strings, based on s, using ' ' as a field separator


# In[3]:


s = 'abcd:efgh:ijkl'
s.split(':') 


# In[4]:


s.split('e')


# In[5]:


s.split(':efg')


# In[6]:


s = 'this is a very interesting example'
s.split(' ')


# In[7]:


s = 'this    is a very     interesting example'
s.split(' ')


# In[8]:


s.split()   # no argument == None, which really means *ANY* whitespace, *ANY* length


# In[12]:


name = input('Enter your name: ')
print(f'Hello, {name}!')


# In[13]:


name


# In[14]:


# str.strip removes the whitespace from the edges
name.strip()


# In[15]:


s = 'abcde'

s.strip('ae')


# In[16]:


s = '   a     b   c    '

s.strip()


# In[17]:


name = input('Enter your name: ').strip()
print(f'Hello, {name}!')


# In[18]:


name = input('Enter your name: ').split()
print(f'Hello, {name}!')


# In[ ]:




