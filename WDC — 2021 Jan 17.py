#!/usr/bin/env python
# coding: utf-8

# In[1]:


# IPython -> Jupyter

print('Hello, world!')


# In[2]:


2 + 5


# In[3]:


print('a')    # enter == newline
print('b')    # enter == newline
print('c')    # shift+enter == execute and show results


# In[4]:


2+2
3+3
4+4


# In[5]:


s = 'Hello, world!'


# In[6]:


print(s)


# In[7]:


type(s)


# In[8]:


s = 100


# In[9]:


print(s)


# In[10]:


type(s)


# 1. Data structures
# 2. Functions
# 3. Objects

# In[11]:


x = 100


# In[12]:


type(x)


# In[13]:


name = input('Enter your name: ')


# In[14]:


name


# In[15]:


x = 2

n = input('Enter a number: ')


# In[16]:


x * n


# In[17]:


x = 6
x * n


# In[18]:


x + n


# In[22]:


# shift + enter executes a cell

name = input('Enter your name: ')

if name == 'Reuven':
    print('Hi, boss!')
    print('Nice to see you again!')
else:
    print('Hello, ' + name + '.')


# # Headline
# 
# This is in Markdown. With *italics* and **boldface**.
# 
# 

# In[24]:


# to get into Markdown mode, type M in command mode (click on left / pressing ESC)
# to get into Edit mode, type RET in command mode (or click in the cell)


# # Data types: None

# In[25]:


x = None


# In[26]:


'' == None


# In[27]:


0 == None


# In[28]:


False == None


# In[29]:


type(x)


# In[30]:


print(x)


# In[31]:


x


# # Data types: True and False

# In[32]:


True


# In[33]:


False


# In[34]:


type(True)


# In[35]:


type(False)


# Comparison operators:
# 
# - `==`
# - `!=`
# - `<`
# - `<=`
# - `>`
# - `>=`

# In[36]:


5 < 10


# In[37]:


5 == 5


# In[38]:


6 != 5


# In[39]:


6 == 10


# In[40]:


x = 10
y = 20

if x < y:
    print('x is less than y')


# In[41]:


x = None

if x:
    print('True-ish')
else:
    print('False-ish')


# Everything in Python is `True` in a boolean context, except for:
# 
# - `False`
# - `None`
# - 0
# - everything empty -- `''`, `[]`, `()`, `{}`

# In[44]:


name = input('Enter your name: ')

if name:   # if the name is not the empty string...
    print('Hello, ' + name + '!')
else:      # if we *DID* get an empty string...
    print('You did not enter a name!')


# # Data structure: Numbers
# 
# - `int`
# - `float`
# 

# In[45]:


x = 10
type(x)


# In[46]:


x = 10
y = 3


# In[47]:


x + y


# In[48]:


x - y


# In[49]:


x * y


# In[50]:


x / y   # truediv


# In[51]:


x // y  # floordiv


# In[52]:


x ** y


# In[53]:


x % y


# In[54]:


x


# In[55]:


x = x + 1
x


# In[56]:


# an easier way to add 1 to x
x += 1
x


# In[57]:


x++


# In[58]:


x = 10
y = '20'


# In[59]:


x + y


# In[61]:


# to get an int from a string, use "int" as a function
x + int(y)


# In[62]:


# to get a string from anything, use "str" as a function
str(x) + y


# In[65]:


name = input('Enter your name: ')

if name == 'Reuven':
    print('Hi, boss!')
    print('Nice to see you')
elif name == 'whatever':
    print('That is not a name!')
else:
    print('Hello, ' + name + '.')


# # Exercise: Guessing game
# 
# 1. Make sure your Python 3 setup is working.
# 2. Generate a random integer from 0 through 100.
# 
# ```python3
# import random
# n = random.randint(0, 100)
# ```   
# 
# 3. Print the number, so we don't have to guess too many times.
# 4. Print one of the following:
#     - You got it!
#     - Too low
#     - Too high
#     

# In[66]:


# to install Jupyter, type
# python -m pip install jupyter

# On the command line, you can then run: 
# jupyter notebook 
# python -m jupyter notebook


# In[67]:


# python.org


# In[70]:


x = 1234
x = x ** 20


# In[71]:


x


# In[72]:


x = x ** 20
x


# In[73]:


x = x ** 20
x


# In[84]:


import random

number = random.randint(0, 100)
print(number)

guess = input('Guess the number: ')
guess = int(guess)

if guess == number:
    print('You got it!')
elif guess < number:
    print('Too low')
else:
    print('Too high')


# In[85]:


10 / 3


# In[86]:


x = 10
y = 10.0


# In[87]:


type(x)


# In[88]:


type(y)


# In[89]:


x == y


# In[90]:


x = 10
y = 3.0

x + y


# In[91]:


x - y 


# In[92]:


float(x)


# In[93]:


float('10')


# In[94]:


int(123.456)


# In[95]:


0.1 + 0.2


# In[96]:


x = 10+3j
y = 12-4j


# In[97]:


x + y


# # Data type: string

# In[99]:


python


# In[ ]:


python -m ensurepip
python -m pip install pip
python -m pip install jupyter

jupyter notebook
python -m jupyter notebook


# In[ ]:





# In[ ]:





# In[100]:


s = 'abcd'
type(s)


# In[101]:


s = "abcd"
type(s)


# In[102]:


s


# In[103]:


s = 'He said, "Hello"'
print(s)


# In[104]:


s = "She's so nice"
print(s)


# In[105]:


s = 'She\'s so nice'
print(s)


# In[106]:


s


# In[107]:


s = 'He said, "She\'s so nice"'
s


# In[108]:


print(s)


# In[109]:


print('abcd
      efgh
      ijklmn')


# In[110]:


s = 'abcd\nefgh\nijklmn'
print(s)


# In[111]:


s


# In[112]:


s = 'abcd'
len(s)


# In[113]:


s = 'abcd\n'
len(s)


# In[114]:


s = 'abcd\tefgh\tijkl'
print(s)


# In[115]:


len(s)


# In[116]:


# double a backslash to get one backslash character

s = 'abcd\\tefgh\\tijkl'
print(s)


# In[117]:


path = 'c:\abcd\efgh\ijkl'
print(path)


# In[118]:


# \a == ASCII 7 -- alarm bell


# In[119]:


path = 'c:\\abcd\\efgh\\ijkl'
print(path)


# In[120]:


# double all of the backslashes with "raw string"
# use r  before the opening quote, and all backslashes are doubled

path = r'c:\abcd\efgh\ijkl'
print(path)


# In[121]:


path


# In[122]:


type(path)


# In[123]:


s = 'abcdefghijklmnopqrstuvwxyz'
len(s)


# In[124]:


s[0]   # retrieve first character


# In[125]:


type(s[0])


# In[126]:


s[1]


# In[127]:


s[2]


# In[128]:


s[25]


# In[129]:


i = 25
s[i]


# In[130]:


i = len(s) - 1
s[i]


# In[131]:


s[len(s)-1]


# In[133]:


s[-1]  # same as s[len(s)-1] -- we count from the right side!


# In[134]:


s[-2]


# In[135]:


s[-3]


# In[136]:


s[-4]


# In[137]:


s[-26]


# In[138]:


s[30]


# # Exercise: Grab a character
# 
# 1. Ask the user to enter a string, and assign it to `s`.
# 2. Ask the user to enter an integer, and assign it to `i`.
# 3. If the number is < 0, say it's too low.
# 4. If the number is > the string length, say it's too high.
# 5. Print the character at that index.
# 
# Example:
# 
#     Enter a string: hello
#     Enter an index: 3
#     l
#     
#     Enter a string: hello
#     Enter an index: 30
#     Too high
#     
#     Enter a string: hello
#     Enter an index: -3
#     Too low

# In[141]:


s = input('Enter a string: ')
i = input('Enter an index: ')
i = int(i)

if i < 0:
    print('Too low')
elif i >= len(s):     # off-by-one error
    print('Too high')
else:
    print(s[i])


# In[143]:


s = input('Enter a string: ')
i = int(input('Enter an index: '))

if i <= 0:
    print('Too low')
    
elif i > len(s):
    print('Too high')
else:
    
    print('The letter in index ' + str(i) + ' is \"' + s[i-1] + '\"')


# In[144]:


s


# In[145]:


i


# In[146]:


print('The letter at index' + i + ' is ' + s[i] + '.')


# In[147]:


print('The letter at index ' + str(i) + ' is ' + s[i] + '.')


# In[148]:


# 3.6 -- f-strings started!
print(f'The letter at index {i} is {s[i]}.')


# In[150]:


x = 10
y = 20

s = f'{x} + {y} = {x+y}'
s


# In[151]:


type(s)


# In[ ]:


s = 'a+b=c'

s = f'{1+2}+{3+4}={3+7}'
s = '3+7=10'


# In[ ]:


# slice -- substring


# In[153]:


s = 'abcdefghijklmnopqrstuvwxyz'

len(s)


# In[154]:


# slice syntax : s[start:end+1]

s[5:10]  # s, from index 5 until (not including) index 10


# In[155]:


s[10:20]


# In[156]:


s[:10]   # from the start until (not including) index 10


# In[157]:


s[10:]  # from index 10 through the end


# In[158]:


# advanced slice syntax: s[start:end+1:step]

s[5:20:3]


# In[159]:


s[::2]


# In[160]:


s[100]


# In[161]:


s[:100]


# In[162]:


s[100:200]


# In[163]:


s


# In[164]:


'a' in s  


# In[165]:


'b' in s


# In[166]:


'ab' in s


# In[167]:


'ae' in s


# In[168]:


s


# In[170]:


s[0] = '!'    # strings are **immutable**


# In[171]:


s = '!' + s[1:]
s


# # Exercise: Pig Latin
# 
# Rules for Pig Latin
# 
# 1. If the first letter is a vowel (`a`, `e`, `i`, `o`, or `u`), then we add `way`
# 2. Otherwise, move the first letter to the end, and add `ay`
# 
# Examples:
# 
# 1. `elephant` -> `elephantway`
# 2. `octopus` -> `octopusway`
# 3. `table` -> `abletay`
# 4. `computer` -> `omputercay`
# 5. `papaya` -> `apayapay`
# 
# Ask the user to enter an English word, and print the translation into Pig Latin.

# In[173]:


word = input('Enter a word: ')

if word[0] == 'a' or word[0] == 'e' or word[0] == 'i' or word[0] == 'o' or word[0] == 'u':
    print(word + 'way')


# In[176]:


word = input('Enter a word: ')

if word[0] in 'aeiou':
    print(word + 'way')
else:
    print(word[1:] + word[0] + 'ay')


# In[177]:


# Pythonic


# In[ ]:




