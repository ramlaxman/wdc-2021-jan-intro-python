#!/usr/bin/env python
# coding: utf-8

# # Agenda
# 
# 1. Comprehensions
# 2. Sorting (and key functions)
# 3. Modules

# In[ ]:





# In[1]:


numbers = range(10)

output = []

for one_number in numbers:
    output.append(one_number ** 2)
    
output


# In[3]:


output = [one_number ** 2 for one_number in numbers]


# In[4]:


output


# In[5]:


[one_number ** 2             # expression -- SELECT
 for one_number in numbers]  # iteration  -- FROM 


# In[6]:


mylist = ['abcd', 'efghi', 'jk']

'*'.join(mylist)


# In[8]:


mylist = [10, 20, 30]

'*'.join(mylist)  # can't run str.join on a list of ints, just a list of strings


# In[9]:


mylist = [10, 20, 30]

'*'.join([str(one_item)
          for one_item in mylist])


# # Exercises: Comprehensions
# 
# 1. Ask the user to enter a sentence. Using a list comprehension and `str.capitalize`, print the input with every word capitalized. (Just like `str.title` would do, but without using it.)
# 
# 2. Ask the user to enter numbers, separated by spaces. (We will get a single string.) Use a comprehension to sum the numbers. You can use the builtin `sum` function, which expects to get a list of integers.

# In[10]:


s = 'this is a test sentence'
s.capitalize()


# In[11]:


s.title()


# In[12]:


s = input('Enter a sentence: ').strip()

print(s.title())


# In[16]:


' '.join([one_word.capitalize()
          for one_word in s.split()])


# In[19]:


s = input('Enter some numbers: ').strip()

sum([int(one_item)
     for one_item in s.split()])


# In[24]:


[one_line.split(':')[0]              # expression  -- SELECT
 for one_line in open('/etc/passwd') # iteration   -- FROM
 if not one_line.startswith('#')]    # condition   -- WHERE


# In[25]:


get_ipython().system('ls *.txt')


# In[26]:


get_ipython().system('cat nums.txt')


# # Exercise: Sum numbers
# 
# Read from `nums.txt` in to a list comprehension, and give the comprehension to `sum` in order to sum the numbers.

# In[27]:


[one_line
for one_line in open('nums.txt')]


# In[28]:


[one_line.strip()
for one_line in open('nums.txt')]


# In[29]:


[int(one_line.strip())
for one_line in open('nums.txt')]


# In[30]:


int()


# In[31]:


int('10')


# In[32]:


int('     10      ')


# In[33]:


int('')


# In[37]:


sum([int(one_line)
for one_line in open('nums.txt')
if one_line.strip().isdigit()])


# In[38]:


s = '123'
s.isdigit()


# In[39]:


s = ' 123'
s.isdigit()


# In[40]:


def count_vowels(one_word):
    total = 0
    
    for one_character in one_word:
        if one_character in 'aeiou':
            total += 1
            
    return total

count_vowels('abcde')


# In[41]:


count_vowels('hello')


# In[42]:


def count_vowels(one_word):
    return sum([1
                for one_character in one_word
                if one_character in 'aeiou'])


# In[43]:


count_vowels('hello')


# In[44]:


get_ipython().system('head linux-etc-passwd.txt')


# # Exercise: Usernames + IDs
# 
# 1. Read from `linux-etc-passwd.txt` in a list comprehension.
# 2. From each line (except for comments and blank lines), produce a list of two elements -- the username (index 0) and the user ID (index 2).
# 3. The result will be a list of lists.

# In[47]:


[one_line
 for one_line in open('linux-etc-passwd.txt')
 if not one_line.startswith('#') and one_line.strip() ]


# In[49]:


[[one_line.split(':')[0], one_line.split(':')[2]]
 for one_line in open('linux-etc-passwd.txt')
 if not one_line.startswith(('#', '\n'))]


# In[50]:


[one_line.split(':')[0:3:2]      # slice -- [start:end:step]
 for one_line in open('linux-etc-passwd.txt')
 if not one_line.startswith(('#', '\n'))]


# In[51]:


dict([one_line.split(':')[0:3:2]   
 for one_line in open('linux-etc-passwd.txt')
 if not one_line.startswith(('#', '\n'))])


# In[52]:


import random
random.randint(0, 100)


# In[53]:


numbers = [random.randint(0, 100)
           for i in range(10)]


# In[54]:


numbers


# In[55]:


numbers.sort()     # ideally, don't use this
numbers


# In[56]:


numbers = [58, 68, 1, 48, 94, 68, 30, 22, 77, 33]


# In[58]:


sorted(numbers)  # sorted is a builtin function


# In[59]:


sorted(open('nums.txt'))


# In[60]:


for one_line in open('nums.txt'):
    print(len(one_line), end= ' ')


# In[61]:


words = 'This is a bunch of words for my Python course at WDC'.split()
words


# In[62]:


sorted(words)


# In[63]:


ord('a')


# In[66]:


ord('b')


# In[67]:


ord('A')


# In[68]:


ord('B')


# In[69]:


'Zoo' < 'aaa'


# In[70]:


sorted([one_word.lower()
         for one_word in words])


# In[71]:


# A < B?

# f(A) < f(B)

# sorted - key function

sorted(words, key=str.lower)


# In[75]:


d1 = {'a':1, 'c':2}
d2 = {'a':10, 'b':3}

d1 < d2


# # Exercises: Sorting
# 
# 1. Ask the user to enter a sentence. Sort the words in the sentence by the number of vowels each word contains.
# 2. Ask the user to enter a sentence. Sort the words by each of the words *backwards* -- that is, first checking the final letter, then the 2nd to last letter, and so on.

# In[79]:


words = input('Enter a sentence: ').split()

def by_vowel_count(one_word):
    print(f'Now checking {one_word}')
    total = 0
    
    for one_character in one_word:
        if one_character in 'aeiou':
            total += 1
            
    return total

sorted(words, key=by_vowel_count)


# In[80]:


words = input('Enter a sentence: ').split()

def by_backwards_word(one_word):
    return one_word[::-1]

sorted(words, key=by_backwards_word)


# In[82]:


one_word = 'fantastically'


# In[83]:


one_word[::-1]   # [START:END:STEPSIZE]   


# In[84]:


one_word[8:3:-1]


# In[88]:


one_word[-1::-1]


# In[91]:


words = input('Enter a sentence: ').split()

def by_backwards_word(one_word):
    output = ''
    for i in range(len(one_word)):
        output += one_word[len(one_word)-1-i]
    return output

sorted(words, key=by_backwards_word)


# In[90]:


def by_backwards_word(one_word):
    output = ''
    for i in range(len(one_word)):
        output += one_word[len(one_word)-1-i]
    return output

by_backwards_word('abcde')


# In[92]:


numbers = [
[random.randint(0, 10) for i in range(5)],
[random.randint(0, 10) for i in range(5)],
[random.randint(0, 10) for i in range(5)],
[random.randint(0, 10) for i in range(5)]
]


# In[93]:


numbers


# In[94]:


sorted(numbers)


# In[95]:


sorted(numbers, key=sum)


# In[96]:


sorted(numbers, key=sum, reverse=True)


# In[97]:


d1 = {'a':1, 'b':2, 'c':3}
d2 = {'b':20, 'c':30, 'd':1}
d3 = {'a':25, 'b':15, 'c':1}

all_dicts = [d1, d2, d3]

sorted(all_dicts)


# In[98]:


def by_b(one_dict):
    return one_dict['b']

sorted(all_dicts, key=by_b)


# In[99]:


def by_value_sums(one_dict):
    return sum(one_dict.values())

sorted(all_dicts, key=by_value_sums)


# # Modules

# In[100]:


# DRY -- don't repeat yourself

import random


# In[101]:


type(random)


# In[102]:


random


# In[103]:


import sys


# In[104]:


sys.path


# In[105]:


import asdfaf


# In[106]:


random.randint(0, 100)


# In[107]:


dir(random)


# In[108]:


help(random)


# In[109]:


random.randint(0, 100)


# In[110]:


randint(0, 100)


# In[111]:


random['randint']


# In[113]:


from random import randint 


# In[114]:


'randint' in globals()


# In[115]:


import mymod


# In[116]:


dir(mymod)


# In[117]:


# dunder -- double underscore


# In[118]:


mymod.__file__


# In[119]:


mymod.__name__


# In[120]:


import mymod as m


# In[121]:


m


# In[122]:


import mymod


# In[123]:


dir(mymod)


# In[125]:


import importlib
importlib.reload(mymod)


# In[126]:


dir(mymod)


# In[127]:


mymod.x


# In[128]:


mymod.y


# In[129]:


mymod.z


# In[130]:


mymod.hello('world')


# In[131]:


sys.path


# In[132]:


importlib.reload(mymod)


# In[134]:


importlib.reload(mymod)


# In[ ]:




