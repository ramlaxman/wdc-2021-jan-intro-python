#!/usr/bin/env python
# coding: utf-8

# # Agenda
# 
# 1. More string things
# 2. Methods vs. functions
# 3. Loops
#     - `for`
#     - Looping a specific number of times
#     - `break` 
#     - `continue`
#     - `while`
# 4. Lists

# In[1]:


'abcd'


# In[2]:


"abcd"


# In[3]:


# raw string -- automatically doubles all backslashes
path = r'c:\abcd\efghi\jklmn'

path


# In[4]:


# f-string -- format string
# {} contains Python code

x = 'abc'
y = 3

f'x = {x}, y = {y}'


# In[5]:


f'x = {x}, y = {y}, x*y = {x*y}'


# In[6]:


# triple-quoted string

"""this is a string

a very nice string

What do you think of my string?
"""


# In[8]:


print('a')

"""
print('b')
print('c')
"""


# In[9]:


s = 'שלום'
len(s)


# In[10]:


# bytestring -- works with bytes, not charaters
b'abcd'


# In[11]:


b'שלום'


# In[12]:


s.encode()  # return a bytestring from this string


# In[13]:


s


# In[14]:


b = s.encode()


# In[15]:


b


# In[16]:


b.decode()   # get a string, based on the bytes


# In[17]:


type(b)


# In[19]:


bytes(s, encoding='utf-8')


# In[20]:


len(s)


# In[21]:


input('abcd')


# In[22]:


print('abcd')


# In[ ]:


# function
FUNC(DATA)


# In[ ]:


# methods
DATA.METHOD()
DATA.METHOD('a', 'b', 'c')


# In[23]:


len(s)


# In[24]:


s.len()


# In[25]:


s = 'aBcDeF'
s.lower()


# In[26]:


s


# In[27]:


s.upper()


# In[28]:


s.capitalize()


# In[30]:


help(str)


# In[32]:


name = input('Enter your name: ')
print(f'Hello, {name}!')


# In[33]:


name.strip()


# In[34]:


name = input('Enter your name: ')
name = name.strip()
print(f'Hello, {name}!')


# In[35]:


name = input('Enter your name: ').strip()
print(f'Hello, {name}!')


# In[36]:


name


# In[37]:


x = input('Enter a number: ')
y = input('Enter a second number: ')

print(f'{x} + {y} = {x+y}')


# In[38]:


x = input('Enter a number: ')
y = input('Enter a second number: ')

x = int(x)
y = int(y)

print(f'{x} + {y} = {x+y}')


# In[39]:


x = input('Enter a number: ')
y = input('Enter a second number: ')

x = int(x)
y = int(y)

print(f'{x} + {y} = {x+y}')


# In[41]:


x = input('Enter a number: ')
y = input('Enter a second number: ')

if not x.isdigit():
    print(f'{x} is not numeric')
elif not y.isdigit():
    print(f'{y} is not numeric')
else:
    x = int(x)
    y = int(y)

    print(f'{x} + {y} = {x+y}')


# In[42]:


x = input('Enter something: ')


# In[43]:


x


# In[44]:


s = 'Reuven'

print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])
print(s[5])


# In[45]:


# DRY -- don't repeat yourself


# In[47]:


s = 'Reuven'

print('Start')
for one_character in s:
    print(one_character)
print('End')


# In[48]:


s = 'Reuven'

print('Start')
for one_character in s[::2]:
    print(one_character)
print('End')


# In[49]:


s = 'Reuven'
index = 0

print('Start')
for one_character in s:
    print(f'{index}: {one_character}')
    index += 1
print('End')


# In[50]:


s = 'Reuven'

print('Start')
for index, one_character in enumerate(s):
    print(f'{index}: {one_character}')
print('End')


# # Exercise: digits, vowels, and others
# 
# 1. Define three variables, all set to 0: `digits`, `vowels`, and `others`.
# 2. Ask the user to enter a string
# 3. For each character, check if it's a digit, vowel, or something else.  Add to the appropriate variable value.
# 4. Print all of the count variables, and their current values.
# 
# Example:
# 
#     Enter a string: hello 123
#     digits: 3, vowels 2, others 4
#     

# In[51]:


if one_character in 'aeiou':
    print('It is a vowel!')


# In[53]:


digits = 0
vowels = 0
others = 0

s = input('Enter a string: ').strip()

for one_character in s.lower():
    if one_character.isdigit():
        digits += 1
    elif one_character in 'aeiou':
        vowels += 1
    else:
        others += 1
        
# print(f'digits = {digits}, vowels = {vowels}, others = {others}')

# in Python 3.9
print(f'{digits=}, {vowels=}, {others=}')


# In[54]:


s = 'abcdabcd'
look_for = 'd'

for one_character in s:
    if one_character == look_for:
        print(f'Found {look_for}')


# In[56]:


s = 'abcdabcd'
look_for = 'd'

print('Start')
for one_character in s:
    if one_character == look_for:
        break   
    
    print(one_character)
print('End')


# In[57]:


s = 'abcdabcd'
look_for = 'd'

print('Start')
for one_character in s:
    if one_character == look_for:
        continue   
    
    print(one_character)
print('End')


# In[58]:


print('Yay!')
print('Yay!')
print('Yay!')
print('Yay!')
print('Yay!')


# In[59]:


# DRY -- don't repeat yourself


# In[60]:


for i in 5:
    print('Yay!')


# In[61]:


for i in range(5):
    print('Yay!')


# In[62]:


for i in range(5):
    print(f'{i} Yay!')


# In[63]:


for i in range(5,10):
    print(f'{i} Yay!')


# In[64]:


for i in range(5,20,3):
    print(f'{i} Yay!')


# In[65]:


for i in range(10, 1, -1):
    print(i, end=' ')


# # Exercise: Name triange
# 
# 1. Ask the user to enter their name.
# 2. Print the first letter, first two letters, first 3 letters, etc.
# 
# Example:
# 
#     Enter your name: Reuven
#     R
#     Re
#     Reu
#     Reuv
#     Reuve
#     Reuven
#     

# In[71]:


name = input('Enter your name: ').strip()

for i in range(1,len(name)+1):
    print(name[:i])


# In[72]:


name


# In[73]:


name[:6]


# In[74]:


len(name)


# In[75]:


range(len(name))


# In[76]:


name[:5]


# In[77]:


x = 5

while x > 0:
    print(x)
    x -= 1


# In[78]:


while True:
    name = input('Enter your name: ').strip()
    
    if not name:   # exit from the loop if we got an empty string
        break
        
    print(f'Hello, {name}!')


# # Exercise: Summing numbers
# 
# 1. Define `total` to be a variable with a value 0.
# 2. Ask the user, repeatedly, to enter a number.
# 3. If the user gives us an empty string, stop asking and print `total`.
# 4. If the user gives us something that cannot be turned into an integer, then scold them and ask for a new value.
# 5. If the input can be turned into an int, do that and add to `total`.
# 
# Example:
# 
#     Enter a number: 5
#     Enter a number: 10
#     Enter a number: abcd
#         abcd is not a number!
#     Enter a number: 5
#     Enter a number: [ENTER]
#     Total is 20
# 

# In[79]:


s = '123'
s.isdigit()


# In[80]:


s.isdecimal()


# In[81]:


s.isnumeric()


# In[82]:


s = '一二三'
s.isdigit()


# In[83]:


s.isdecimal()


# In[84]:


s.isnumeric()


# In[85]:


s = '12ab'

s.isdigit()


# In[86]:


s.isdecimal()


# In[87]:


s.isnumeric()


# In[88]:


help(s.isnumeric)


# In[89]:


s = '0x12ab'
s.isnumeric()


# In[90]:


total = 0

while True:
    s = input('Enter a number: ').strip()
    
    if not s:
        break
        
    if not s.isdigit():
        print(f'{s} is not numeric; try again')
        continue
        
    total += int(s)
    
print(f'{total=}')
    


# In[ ]:


total = 0

s = input('Enter a number: ').strip()

while s:
    if not s.isdigit():
        print(f'{s} is not numeric; try again')
        continue
        
    total += int(s)
    
    s = input('Enter a number: ').strip()
    
print(f'{total=}')
    


# In[92]:


total = 0

# := assignment expression operator
# walrus 

while s := input('Enter a number: ').strip():
    if not s.isdigit():
        print(f'{s} is not numeric; try again')
        continue
        
    total += int(s)
    
print(f'{total=}')
    


# In[94]:


n = 50

if (x := n * 3) > 100:
    print('Yes!')


# In[95]:


x


# In[102]:


s = 'abcdabcd'
look_for = '!'

found_it = False
for one_character in s:
    if look_for == one_character:
        print(f'Found {look_for}')
        found_it = True
        break
        
if not found_it:
    print(f'Did not find {look_for}')


# In[104]:


s = 'abcdabcd'
look_for = 'd'

for one_character in s:
    if look_for == one_character:
        print(f'Found {look_for}')
        break

else:   # if I got to the end of the "for" loop WITHOUT a break
    print(f'Did not find {look_for}')


# In[106]:


for i in range(5):
    print(i)
    if i == 4:
        break
else:
    print('Got to else')


# In[107]:


mylist = [10, 20, 30, 40, 50]

type(mylist)


# In[108]:


# sequence -- string, list, or tuple

mylist[0]


# In[109]:


mylist[1]


# In[110]:


mylist[-1]


# In[111]:


# slice
mylist[2:5]


# In[112]:


mylist[:4]


# In[113]:


# loop
for one_item in mylist:
    print(one_item, end=' ')


# In[114]:


30 in mylist


# In[115]:


mylist = [10, 20, 30]
len(mylist)


# In[116]:


biglist = [mylist, mylist, mylist]
biglist


# In[117]:


len(biglist)


# In[118]:


biglist[0]


# In[119]:


biglist[0][1]


# In[124]:


# loop
for one_item in mylist:
    print(one_item, end='\n\n\n')


# In[125]:


mylist


# In[126]:


biglist


# In[127]:


s = 'abcde'
s[0]


# In[128]:


s[0] = '!'   # strings are immutable


# In[129]:


mylist[0] = '!'   # lists are mutable


# In[130]:


mylist


# In[131]:


n = 10
n = 20


# In[132]:


n = 10


# In[133]:


mylist


# In[134]:


biglist


# For visualizing Python:
# https://pythontutor.com
# 
# For seeing my example:
# http://pythontutor.com/visualize.html#code=mylist%20%3D%20%5B10,%2020,30%5D%0Abiglist%20%3D%20%5Bmylist%5B%3A%5D,%20mylist%5B%3A%5D,%20mylist%5B%3A%5D%5D%0A%0Amylist%5B0%5D%20%3D%20'!'%0Abiglist%5B1%5D%5B1%5D%20%3D%20'%3F'%0A%0Aprint%28mylist%29%0Aprint%28biglist%29%0A&cumulative=false&curInstr=6&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false

# # Next time:
# 
# - List methods
# - String to list (and back)
# - Tuples
# - Dictionaries

# In[ ]:




