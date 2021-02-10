#!/usr/bin/env python
# coding: utf-8

# # Agenda
# 
# 1. Sets
# 2. Files
# 3. Combinations of data structures
# 

# In[2]:


d = {'a':1, 'b':2, 'c':3}

d['a'] = 999
d


# In[3]:


logged_in = {}

logged_in['user1'] = 1
logged_in['user2'] = 1
logged_in['user5'] = 1


# In[4]:


'user5' in logged_in


# In[5]:


logged_in.pop('user5')


# In[6]:


# Set -- dict without values


# In[7]:


s = {10, 20, 30, 40, 50}
type(s)


# In[8]:


s.add(100)
s


# In[9]:


s.add(200)
s


# In[10]:


s.add(100)


# In[11]:


s


# In[12]:


s.add(30)
s


# In[13]:


30 in s


# In[14]:


100 in s


# In[15]:


555 in s


# In[16]:


s = {}
type(s)


# In[17]:


# empty set
s = set()
type(s)


# In[18]:


s


# In[19]:


s.add(10)
s


# In[20]:


s.remove(10)
s


# In[21]:


numbers = [10, 20, 30, 10, 20, 30, 20, 30, 40, 20, 30, 50]
set(numbers)


# In[22]:


# add lots of things at once
s


# In[23]:


s.update([10, 20, 30, 20, 30, 40, 20, 30, 40, 50])
s


# In[24]:


s.update([40, 50, 60])


# In[25]:


s


# In[26]:


s += [70, 80, 90]


# In[27]:


s += {70, 80, 90}


# In[28]:


s1 = {10, 20 ,30, 40}
s2 = {30, 40, 50, 60}

s1 | s2   # union


# In[29]:


s1 & s2    # intersection


# In[30]:


s1 ^ s2    # xor


# In[31]:


s1 |= s2   # union, assign to s1


# In[32]:


s1


# In[33]:


s1 = {10, 20 ,30, 40}
s2 = {30, 40, 50, 60}


# In[34]:


s1 - s2


# In[35]:


s2 - s1


# In[36]:


s1.symmetric_difference(s2)


# In[37]:


{10, 20} < s1


# In[38]:


{10, 20, 50} < s1


# # Data structures
# 
# 1. `None`
# 2. booleans `True` and `False`
# 3. `int`, `float`
# 4. `str`
# 5. `list`
# 6. `tuple`
# 7. `dict`
# 8. `set`

# In[39]:


# Files

# file-like object


# In[40]:


# (1) open the file for reading
# (2) get a file-like object back, and assign to f

f = open('/etc/passwd')


# In[41]:


f


# In[42]:


f.read()


# In[45]:


f = open('/etc/passwd')

for one_line in f:
    print(one_line, end='')
    
f.close()


# In[46]:


for one_line in open('/etc/passwd'):
    print(one_line, end='')


# In[50]:


# print the usernames

for one_line in open('/etc/passwd'):
    if not one_line.startswith('#'):
        print(one_line.split(':')[0])


# In[51]:


get_ipython().system('ls *.txt')


# In[52]:


cat nums.txt


# # Exercise: Sum numbers
# 
# 1. Read from `nums.txt`, one line at a time.
# 2. Add the numbers together.  You should get 83.

# In[53]:


# open(r'c:\foo\bar\nums.txt')


# In[54]:


for one_line in open('nums.txt'):
    print(one_line, end='')


# In[60]:


total = 0
for one_line in open('nums.txt'):
    if one_line.strip():
        total += int(one_line)
print(f'{total=}')


# In[56]:


int('5')


# In[57]:


int('     5      ')


# In[58]:


int(' \n\n\t\t 5\v\v\t\t')


# In[ ]:


total = 0
for one_line in open('nums.txt'):
    if one_line.strip().isdigit():
        total += int(one_line)
print(f'{total=}')


# In[61]:


# wc -- word count

get_ipython().system('wc wcfile.txt')


# In[62]:


get_ipython().system('cat wcfile.txt')


# # Exercise: wc
# 
# 1. Write a program that, for a file, prints:
#     - Number of lines (including blank lines)
#     - Number of characters (including whitespace, \n, etc.)
#     - Number of words (separated by spaces/whitespace)
#     - Number of different/unique words

# In[67]:


counts = {'lines':0,
          'chars':0,
          'words':0}
unique_words = set()

for one_line in open('wcfile.txt'):
    counts['lines'] += 1
    counts['chars'] += len(one_line)
    counts['words'] += len(one_line.split())
    unique_words.update(one_line.split())

counts['unique'] = len(unique_words)
for key, value in counts.items():
    print(f'{key}: {value}')


# In[66]:


s = 'abc def ghi'
s.split()  # whitespace is our separator


# In[68]:


f = open('/etc/passwd', 'r')  # 2nd argument is optional, defaults to 'r'


# In[69]:


f = open('myfile.txt', 'w')   # 'w' means: open for writing


# In[70]:


f


# In[71]:


f.write('abcde\n')
f.write('fgh\n')
f.write('ijklmnop\n')


# In[72]:


get_ipython().system('cat myfile.txt')


# In[73]:


f.flush()   # flush the buffer to disk


# In[74]:


get_ipython().system('cat myfile.txt')


# In[75]:


f.close()   # close first flushes the file


# In[77]:


with open('myfile2.txt', 'w') as f:
    f.write('10:35 abcde\n')
    f.write('10:35 fghijkl\n')
    f.write('10:35 zzzz')
    # f.__exit__() -- flush + close the file


# In[78]:


get_ipython().system('cat myfile2.txt')


# In[79]:


with open('/etc/passwd') as f:
    for one_line in f:
        print(len(one_line), end=' ')


# In[80]:


d = {'a':1, 'b':2, 'c':3}

with open('myconfig.txt', 'w') as f:
    for key, value in d.items():
        f.write(f'{key}={value}\n')


# In[81]:


get_ipython().system('cat myconfig.txt')


# In[82]:


get_ipython().system('ls')


# In[83]:


f = open('wdc-2021-jan-28.zip')


# In[84]:


f.readline()


# In[86]:


# str -- Unicode characters
# bytes -- bytes only!


# In[87]:


b = b'abcde'
type(b)


# In[88]:


b[0]


# In[93]:


f = open('wdc-2021-jan-28.zip', 'rb')  # read mode + binary/bytes


# In[94]:


b = f.read(20)


# In[95]:


b


# In[96]:


b[0]


# In[97]:


b[1]


# In[98]:


b[2]


# In[99]:


b[3]


# # Combinations of data structures
# 
# - list of lists
# - list of tuples
# - list of dicts
# - dict of dicts
# - dict of lists

# In[100]:


# Spotlight, 129, Tom McCarthy
# The Big Short, 130, Adam McKay
# The Martian, 141, Ridley Scott


# In[104]:


# list of lists

movies = [['Spotlight', 129, 'Tom McCarthy'],
          ['The Big Short', 130, 'Adam McKay'],
          ['The Martian', 141, 'Ridley Scott']]

look_for = input('Enter movie name: ').strip()

for one_movie in movies:
    if look_for == one_movie[0]:
        print(f'Found {look_for}, {one_movie[1]} min, dir {one_movie[2]}')
        break
        
else:
    print(f'Did not find {look_for}')


# In[106]:


# list of tuples

movies = [('Spotlight', 129, 'Tom McCarthy'),
          ('The Big Short', 130, 'Adam McKay'),
          ('The Martian', 141, 'Ridley Scott')]

look_for = input('Enter movie name: ').strip()

for one_movie in movies:
    if look_for == one_movie[0]:
        print(f'Found {look_for}, {one_movie[1]} min, dir {one_movie[2]}')
        break
        
else:
    print(f'Did not find {look_for}')


# In[110]:


# list of dicts

movies = [{'name':'Spotlight', 'min':129, 'dir':'Tom McCarthy'},
          {'name':'The Big Short', 'min':130, 'dir':'Adam McKay'},
          {'name':'The Martian', 'min':141, 'dir':'Ridley Scott',
           'sale':True}]

look_for = input('Enter movie name: ').strip()

for one_movie in movies:
    if look_for == one_movie['name']:
        print(f'Found {look_for}, {one_movie["min"]} min, dir {one_movie["dir"]}')
        if 'sale' in one_movie:
            print('\tAlso: On sale!')
        break
        
else:
    print(f'Did not find {look_for}')


# In[115]:


# dict of dicts

movies = {'Spotlight' : {'min':129, 'dir':'Tom McCarthy'},
          'The Big Short' : {'min':130, 'dir':'Adam McKay'},
          'The Martian': {'min':141, 'dir':'Ridley Scott','sale':True}
         }

look_for = input('Enter movie name: ').strip()

if look_for in movies:
    one_movie = movies[look_for]
    print(f'Found {look_for}, {one_movie["min"]} min, dir {one_movie["dir"]}')
    if 'sale' in one_movie:
        print('\tAlso: On sale!')
        
else:
    print(f'Did not find {look_for}')


# In[122]:


movies = [{'name':'Spotlight', 'min':129, 'dir':'Tom McCarthy'},
          {'name':'The Big Short', 'min':130, 'dir':'Adam McKay'},
          {'name':'The Martian', 'min':141, 'dir':'Ridley Scott'}]

movie_name_dict = {}
movie_dir_dict = {}

for one_movie in movies:
    movie_name_dict[one_movie['name']] = one_movie
    movie_dir_dict[one_movie['dir']] = one_movie


# In[123]:


movie_name_dict


# In[124]:


movie_dir_dict


# In[125]:


movie_name_dict['Spotlight']['min'] = 555

movie_name_dict


# In[126]:


movie_dir_dict


# In[ ]:





# In[127]:


# dict of dicts

movies = {'Spotlight' : {'min':129, 'dir':'Tom McCarthy'},
          'The Big Short' : {'min':130, 'dir':'Adam McKay'},
          'The Martian': {'min':141, 'dir':'Ridley Scott','sale':True}
         }

look_for = input('Enter movie name: ').strip()

if look_for in movies:
    one_movie = movies[look_for]
    print(f'Found {look_for}, {one_movie["min"]} min, dir {one_movie["dir"]}')
    if 'sale' in one_movie:
        print('\tAlso: On sale!')
        
else:
    print(f'Did not find {look_for}')


# In[128]:


for key, value in movies.items():
    print(f'{key}: {value}')


# In[129]:


for movie_name, movie_info in movies.items():
    print(f'{movie_name}: {movie_info}')


# In[130]:


list(movies)


# In[131]:


d


# In[132]:


print(f'{d["a"]=}')


# In[ ]:




