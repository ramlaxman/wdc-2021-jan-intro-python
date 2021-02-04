#!/usr/bin/env python
# coding: utf-8

# # Agenda
# 
# - List methods
# - Strings to lists (and back)
# - Tuples
# - Start of dicts

# In[1]:


mylist = [10, 20, 30, 40, 50]
type(mylist)


# In[2]:


mylist[0]


# In[3]:


mylist[1]


# In[4]:


mylist[-1]


# In[5]:


mylist[2:5]


# In[6]:


len(mylist)


# In[7]:


for one_item in mylist:
    print(one_item, end=' ')


# In[8]:


40 in mylist


# In[9]:


mylist


# In[10]:


mylist[2] = '!!!'
mylist


# In[11]:


s = 'abcd'
s += 'efgh'  # s = s + 'efgh'


# In[12]:


mylist = [10, 20, 30]
mylist.append(40)  


# In[13]:


mylist


# In[14]:


mylist = mylist.append(50)

print(mylist)


# In[15]:


type(None)


# In[16]:


dir(None)


# In[17]:


mylist = []
mylist.append(10)
mylist.append([100, 200, 300])
mylist.append('abcd')

mylist


# In[18]:


len(mylist)


# In[19]:


for one_item in [100, 200, 300]:
    mylist.append(one_item)
    
mylist


# In[20]:


# adding multiple items with +=

mylist += [1234, 5678, 90]
mylist


# In[21]:


mylist += 5


# In[22]:


mylist += 'abcd'


# In[23]:


mylist


# In[24]:


# mylist += 'abcd'
mylist.__iadd__('abcd')


# In[26]:


x = 5
x += 6


# In[27]:


x


# In[28]:


5 += 6


# In[29]:


import friendly_traceback


# In[34]:


5 += 6


# In[35]:


friendly_traceback.explain_traceback()


# In[36]:


# stack - LIFO -- last in, first out

# push -- adds to the end (append)
# pop -- removes from the end (pop)

stack = [10, 20, 30]
stack.append(40)
stack.append(50)

stack


# In[37]:


stack.pop()


# In[38]:


stack


# In[39]:


stack.pop()


# In[40]:


# queue -- FIFO -- first in, first out

# push -- adds to the end (append)
# pop(0) -- removes from the start

queue = [10, 20, 30]
queue.pop(0)


# In[41]:


queue.append(40)
queue


# In[42]:


queue.pop(0)


# In[43]:


queue


# # Exercise: digits, vowels, and others
# 
# 1. Define three lists : `digits`, `vowels`, and `others`
# 2. Ask the user to enter a string.
# 3. Go through the user's string, and add each character to the appropriate list.
# 4. Then print each list.

# In[44]:


digits = []
vowels = []
others = []

s = input('Enter a string: ').strip()

for one_character in s.lower():
    if one_character in 'aeiou':
        vowels.append(one_character)
    elif one_character.isdigit():
        digits.append(one_character)
    else:
        others.append(one_character)
        
print(f'{digits=}, {vowels=}, {others=}')


# In[45]:


for one_list in [digits, vowels, others]:
    print(one_list)


# In[46]:


s = '   a     b    c   '
s.strip()


# In[47]:


s.lstrip()


# In[48]:


s.rstrip()


# In[49]:


s = '5'
int(s)


# In[50]:


x = 5
str(x)


# In[51]:


s = 'abcd'
list(s)


# In[52]:


mylist = [10, 20, 30]
str(mylist)


# In[53]:


s = 'abcd;ef;ghij'
str(s)


# In[54]:


list(s)


# In[56]:


# method: str.split

s.split(';')  # we always get a list of strings back from str.split


# In[57]:


s = 'this is a bunch of words'
s.split(' ')


# In[58]:


s = 'this   is a    bunch  of     words'
s.split(' ')


# In[59]:


s = 'this   is a    bunch  of     words'
s.split()   # no arguments = any whitespace (' ', \n, \r, \t, \v), any length


# In[60]:


words = s.split()
words


# In[61]:


# turn a list of strings into a string
# str.join is a *STRING* method, applied to the string that will be our "glue"

' '.join(words)


# In[62]:


'*'.join(words)


# In[63]:


print('\n'.join(words))


# In[64]:


'*'.join([10, 20, 30])


# # Exercise: Pig Latin sentence
# 
# 1. Ask the user to enter a sentence.
# 2. Translate each word into Pig Latin.
# 3. Display the translated words on a single line.
# 
# ```python
# word = input('Enter a word: ').strip()
# 
# if word[0] in 'aeiou':
#     print(word + 'way')
# else:
#     print(word[1:] + word[0] + 'ay')
# ```

# In[65]:


sentence = input('Enter a sentence: ').strip()

for word in sentence.split():
    if word[0] in 'aeiou':
        print(word + 'way')
    else:
        print(word[1:] + word[0] + 'ay')


# In[66]:


sentence = input('Enter a sentence: ').strip()

for word in sentence.split():
    if word[0] in 'aeiou':
        print(word + 'way', end=' ')
    else:
        print(word[1:] + word[0] + 'ay', end=' ')


# In[67]:


sentence = input('Enter a sentence: ').strip()

output = []

for word in sentence.split():
    if word[0] in 'aeiou':
        output.append(word + 'way')
    else:
        output.append(word[1:] + word[0] + 'ay')

print(output)


# In[68]:


print(' '.join(output))


# In[71]:


mylist = ['abcd efgh ijklm'.split(),
          'no pqr stuv'.split(),
          'wx yz 1234'.split()]

mylist


# In[72]:


output = ''

for one_record in mylist:
    output += '\t'.join(one_record) + '\n'
    
print(output)


# In[76]:


output = []

for one_record in mylist:
    output.append('\t'.join(one_record))
    
print('\n'.join(output))

sequence -- str, list, tuple


              contents         mutable/immutable?
string         str                 immutable
list           anything            mutable           (the same type)
tuple          anything            immutable         (different types)
# In[77]:


t = (10, 20, 30)
type(t)


# In[78]:


t = (10, 20)
type(t)


# In[79]:


t = (10)
type(t)


# In[80]:


t = ()
type(t)


# In[81]:


4 + 5 * 6


# In[82]:


(4 + 5) * 6


# In[83]:


t = (10,)
type(t)


# In[84]:


t = 10, 20, 30, 40, 50

t


# # Dictionary (`dict`)
# 
# - Hash
# - Hash table
# - Hashmap
# - Map
# - Associative array
# - Key-value pair
# - Name-value pair

# In[86]:


d = {'a':1, 'b':2, 'c':3}


# In[87]:


type(d)


# # Dictionaries
# 
# - Keys can be any *immutable* type (usually numbers or strings)
# - Values can be anything at all
# - Every key has one value, every value has one key
# - Every key appears once, and only once

# In[88]:


len(d)   


# In[92]:


'a' in d  # the "in" operator just looks at keys, not values


# In[90]:


'c' in d


# In[91]:


2 in d


# In[93]:


d


# In[94]:


d['a']


# In[95]:


d['b']


# In[96]:


d['c']


# In[97]:


d['asdfafa']


# In[98]:


k = 'b'
d[k]


# # Exercise: Restaurant
# 
# 1. Define a dict, `menu`, in which the keys are the menu entries and the values are the prices.
# 2. Define a variable, `total`, set to 0, in which we'll calculate the bill.
# 3. Ask the user, repeatedly, to order something from the menu.
#     - If we get an empty string, stop asking and print the total.
#     - If the user enters something on the menu, print the price and current total (and add to current total)
#     - If the user asks for something *not* on the menu, then scold them and ask to try again
#     
# Example:
# 
#     Order: sandwich
#     sandwich is 20, total is 20
#     Order: tea
#     tea is 10, total is 30
#     Order: elephant
#     we are fresh out of elephant today!
#     Order: [ENTER]
#     total is 30

# In[100]:


menu = {'sandwich':20, 'tea':10, 'cake':15, 'apple':7}

total = 0

while True:
    s = input('Order: ').strip()
    
    if not s:  # empty string? exit from the loop
        break
        
    if s in menu:
        price = menu[s]
        total += price
        print(f'{s} costs {price}, total is {total}')
    else:
        print(f'We are out of {s} today.')

print(f'total = {total}')


# In[102]:


d = {}         # empty dict
d['a'] = 1  

d


# In[103]:


d['b'] = 2


# In[104]:


d


# In[105]:


d['a'] = 3


# In[106]:


d


# In[107]:


mylist = [10, 20, 30]
d[mylist] = 100


# In[108]:


d


# In[109]:


d[mylist]


# In[110]:


s = '   abc   def   ghi   '

s.strip()  # return a string, without whitespace on the ends


# In[111]:


s.split()   # returns a list of strings, uses whitespace (any type, any length) to split


# In[112]:


s.split() in d


# In[113]:


d = {'a':1, 'b':2, 'c':3}

while True:
    k = input('Enter a key: ').strip()
    
    if not k:
        break
        
    if k in d:
        print(f'd[{k}] = {d[k]}')
    else:
        print(f'{k} is not a key in d')


# In[114]:


# dict.get is just like [] if the key exists
d.get('a')


# In[115]:


d.get('b')


# In[116]:


d.get('c')


# In[118]:


# if the key does NOT exist, we get None back
print(d.get('p'))


# In[119]:


# if the key does NOT exist, and we pass a second argument, we get that value back
d.get('p', 'No such key')


# # Exercise: digits, vowels, and others — dict edition
# 
# 1. Define a dict, `counts`, with three keys (`digits`, `vowels`, and `others`), with all three values set to 0.
# 2. Ask the user to enter a string.
# 3. Go through the string, and count how many times each of these (digits, vowels, and others) appear.
# 4. Print `counts`.

# In[120]:


counts = {'digits':0,
         'vowels':0,
         'others':0}

s = input('Enter a string: ').strip()

for one_character in s.lower():
    if one_character in 'aeiou':
        counts['vowels'] += 1
    elif one_character.isdigit():
        counts['digits'] += 1
    else:
        counts['others'] += 1
        
print(counts)    


# In[121]:


for one_item in counts:
    print(one_item)


# In[122]:


for key in counts:
    print(f'{key}: {counts[key]}')


# In[123]:


for one_item in counts.items():
    print(one_item)


# In[124]:


# tuple unpacking -- unpacking

mylist = [10, 20, 30]
x = mylist

x


# In[125]:


x,y,z = mylist


# In[126]:


x


# In[127]:


y


# In[128]:


z


# In[129]:


x,y = mylist


# In[130]:


w,x,y,z = mylist


# In[131]:


for one_item in counts.items():
    print(one_item)


# In[132]:


mylist = [10, 20, 30]
x,y,z = mylist


# In[133]:


x


# In[134]:


y


# In[135]:


z


# In[136]:


mylist[0] = 999


# In[137]:


mylist


# In[138]:


mylist = [[10], [20], [30]]
x,y,z = mylist


# In[139]:


x


# In[140]:


x[0] = 999
x


# In[141]:


mylist


# In[142]:


counts


# In[143]:


for one_item in counts.items():
    print(one_item)


# In[144]:


for key, value in counts.items():
    print(f'{key}: {value}')


# In[145]:


for one_letter in 'abcd':
    print(one_letter)


# In[146]:


for index, one_letter in enumerate('abcd'):
    print(f'{index}: {one_letter}')


# In[147]:


counts.keys()


# In[148]:


counts.values()


# In[149]:


for key in counts.keys():
    print(key)


# In[150]:


for key in counts:
    print(key)


# # Exercise: Rainfall
# 
# 1. Define an empty dict, `rainfall`.
# 2. Ask the user (repeatedly) to enter the name of a city.
# 3. If the city name is blank, stop asking.
# 4. If the city name is *not* blank, ask how much rain (in mm) fell there yesterday.
#     - If this is a new city, then put the value in the dict.
#     - If this is a city we already had before, then add the new value to the old one.
# 5. After the user presses Enter, print the dict in a loop.
# 
# Example:
# 
#     City: Jerusalem
#     Rain: 5
#     City: Tel Aviv
#     Rain: 4
#     City: Jerusalem
#     Rain: 3
#     City: [ENTER]
#     
#     Jerusalem: 8
#     Tel Aviv: 4

# In[156]:


rainfall = {}

while True:
    city_name = input('Enter city name: ').strip()
    
    if not city_name:
        break
        
    mm_rain = input('Enter mm rain: ').strip()

    if not mm_rain.isdigit():
        print(f'{mm_rain} is not numeric; try again')
        continue
        
    mm_rain = int(mm_rain)
    
#     if city_name in rainfall:
#         rainfall[city_name] += mm_rain
#     else:
#         rainfall[city_name] = mm_rain
        
    rainfall[city_name] = rainfall.get(city_name, 0) + mm_rain

for city_name, mm_rain in rainfall.items():
    print(f'{city_name}: {mm_rain}')   


# In[152]:


rainfall


# In[157]:


mylist = [10, 20, 30]
20 in mylist             # O(n)


# In[158]:


d = {'a':1, 'b':2, 'c':3}
'b' in d                 # O(1)


# In[159]:


hash('a')


# In[160]:


hash('b')

    index        key          value
      0           'a'           10
      1           'b'           20
    
[1, None, None, None, None, 0, None, None]
# In[161]:


d = {}
d['a'] = 10
hash('a') % 8


# In[162]:


d['a'] 


# In[163]:


d['b'] = 20
hash('b') % 8


# In[164]:


'b' in d


# In[165]:


for one_character in 'cdefg':
    print(f'{one_character}, {hash(one_character) % 8}')


# In[166]:


for one_character in 'abcdefg':
    print(f'{one_character}, {hash(one_character) % 8}, {hash(one_character) % 16}')


# # Next time:
# 
# 1. Sets
# 2. Files
# 3. Combinations of data structures
# 4. Functions

# In[ ]:




