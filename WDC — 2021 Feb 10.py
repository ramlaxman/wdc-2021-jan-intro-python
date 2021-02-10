#!/usr/bin/env python
# coding: utf-8

# # Agenda
# 
# 1. Writing functions
# 2. Parameters
# 3. Defaults
# 4. Return values
# 5. Scopes (local, global, and builtin)

# In[1]:


s = 'abcd'
x = len(s)


# In[2]:


x


# In[3]:


type(x)


# In[4]:


x = s.upper()


# In[5]:


x


# In[6]:


type(x)


# In[7]:


x = s.upper


# In[8]:


x


# In[9]:


type(x)


# In[10]:


s.upper()


# In[11]:


x()


# In[12]:


help(s.upper)


# In[13]:


d = {'a':1, 'b':2, 'c':3}

for key, value in d.items():
    print(f'{key}: {value}')


# In[19]:


for key, value in d.items:
    print(f'{key}: {value}')


# In[20]:


def hello():
    print('Hello!')


# In[21]:


type(hello)


# In[22]:


hello = 5


# In[23]:


type(hello)


# In[24]:


hello()


# In[25]:


def hello():
    print('Hello!')


# In[26]:


hello()


# In[27]:


x = hello()


# In[28]:


type(x)


# In[29]:


print(x)


# In[30]:


def hello():
    return 'Hello!'


# In[31]:


hello()


# In[32]:


x = hello()

type(x)


# In[33]:


def hello(name):
    return f'Hello, {name}!'


# In[34]:


hello()


# In[35]:


hello('world')


# In[36]:


hello('Reuven')


# In[37]:


hello(5)


# In[38]:


hello([10, 20, 30])


# In[39]:


hello(d)


# In[40]:


hello(hello)


# In[41]:


def hello(name):
    if type(name) == str:
        return f'Hello, {name}!'
    else:
        return 'I wanted a string!'


# In[42]:


hello('world')


# In[43]:


hello(5)


# In[44]:


type('abcd')


# In[45]:


type(5)


# In[46]:


type([10, 20, 30])


# In[47]:


type(str)


# In[48]:


type(int)


# In[49]:


type(list)


# In[50]:


type(type)


# In[51]:


def hello(name:str):  # type annotations ... type hints
    return f'Hello, {name}!'


# In[52]:


hello('world')


# In[53]:


hello(5)


# In[54]:


hello(d)


# In[55]:


# duck typing


# In[56]:


def hello(name):
    return f'Hello, {name}!'


# In[57]:


help(len)


# In[58]:


help(hello)


# In[72]:


# docstring

def hello(name):
    """This is the friendliest function ever written!
    
    Requires: One argument, typically a string
    Modifies: Nothing
    Returns: A friendly string
    """
    return f'Hello, {name}!'


# In[73]:


hello('abcd')


# In[74]:


help(hello)


# In[75]:


hello.__doc__


# # Exercise: mysum
# 
# 1. Write a function, `mysum`, that takes one argument, an iterable of numbers.
# 2. The function should return the sum of these numbers.
# 3. Don't use the builtin `sum` function!

# In[76]:


sum([10, 20, 30])


# In[77]:


sum((10, 20, 30, 40, 50))


# In[78]:


def mysum(numbers):
    total = 0
    for one_number in numbers:
        total += one_number
    return total

mysum([10, 20, 30])


# In[79]:


mysum((10, 20, 30, 40, 50))


# In[80]:


mysum([10, 'a', 20])


# In[81]:


def hello(first, last):
    return f'Hello, {first} {last}!'


# In[82]:


hello('Reuven', 'Lerner')


# In[83]:


hello('out', 'there')


# In[84]:


hello('there')


# In[85]:


hello('famousnamehere')


# In[86]:


def hello(first, last='(No last name)'):
    return f'Hello, {first} {last}!'


# In[87]:


hello('a', 'b')


# In[88]:


hello('a')


# In[89]:


hello.__code__.co_argcount


# In[90]:


hello.__defaults__


# In[91]:


def myfunc(a, b, c):
    d = a + b + c 
    
    print(e)
    return d


# In[92]:


myfunc(10, 20, 30)


# In[93]:


def myfunc():
    asdfafafsafsafafa


# In[95]:


def myfunc():
    adsfasfafafa
     asdfafafa


# In[97]:


def myfunc(a, b, c):
    d = a + b 
    return d


# In[98]:


myfunc.__code__.co_argcount


# In[99]:


myfunc.__defaults__


# In[100]:


myfunc.__code__.co_varnames


# In[101]:


x = 100
y = x       #  y = 100

x = 200
y


# In[102]:


x = 100

def myfunc(y):
    y = 200
    
myfunc(x)    
x


# In[103]:


x = [10, 20, 30]

def add_one(y):
    y.append(1)
    
add_one(x)
x


# In[104]:


def add_one(y=[]):
    y.append(1)
    return y

x = [10, 20, 30]
add_one(x)
x


# In[105]:


add_one(x)
x


# In[106]:


add_one()


# In[107]:


add_one()


# In[108]:


add_one()


# In[109]:


def add_one(y=[]):
    y.append(1)
    return y


# In[110]:


add_one.__defaults__


# In[111]:


add_one() 


# In[112]:


add_one.__defaults__


# In[113]:


def add_one(y=None):
    if y is None:
        y = []
    y.append(1)
    return y


# In[114]:


add_one()


# In[115]:


add_one()


# In[116]:


add_one()


# In[117]:


def add(a, b):
    return a + b


# In[118]:


add(10, 5)   # positional arguments


# In[119]:


add(a=10, b=5)  # keyword arguments


# In[120]:


add(b=10, a=5)


# In[121]:


add(10, b=5)


# In[122]:


add(a=10, 5)


# In[123]:


add(10, a=5)


# In[124]:


def add(a=10, b=5):
    return a + b


# In[125]:


add()


# In[126]:


add(2)


# In[127]:


add(, 2)


# In[128]:


add(b=2)  # uses a's default


# # Parameter types
# 
# 1. Mandatory
# 2. Optional (with a default)

# In[129]:


mysum([10, 20, 30])


# In[130]:


mysum([10, 20, 30 ,40, 50])


# In[131]:


mysum(10, 20, 30)


# In[132]:


def mysum(a=0, b=0, c=0, d=0, e=0):
    return a + b + c + d + e


# In[133]:


mysum(10, 20, 30)


# In[134]:


mysum(10, 20, 30, 40, 50)


# In[135]:


mysum(10, 20, 30, 40, 50, 60)


# In[139]:


# *args  == 'splat args'

def mysum(*numbers):   # (1) all remaining positional args , (2) numbers is a tuple
    print(f'{numbers=}')
    total = 0
    for one_number in numbers:
        total += one_number
    return total


# In[140]:


mysum(10, 20, 30, 40, 50)


# In[141]:


mysum(100, 200)


# In[142]:


mysum([10, 20, 30, 40, 50])


# In[143]:


def myfunc(a, b, *args):
    return f'{a=}, {b=}, {args=}'


# In[144]:


myfunc(10, 20, 30, 40,50)


# # Exercise: all_lines
# 
# 1. Write a function, `all_lines`, that takes one mandatory parameter and any number of optional ones.
# 2. The mandatory parameter is `outfilename`, the name of the file into which we'll write.
# 3. All the rest of the arguments will go into `args`, names of files from which we want to read.
# 4. When the function finishes, all of the lines from the input files should be written to the output file.  All lines from the first file, then all lines from the 2nd file, then all lines from the 3rd file, etc.

# In[145]:


def all_lines(outfilename, *args):
    with open(outfilename, 'w') as outfile:
        for one_filename in args:
            for one_line in open(one_filename):
                outfile.write(one_line)


# In[146]:


get_ipython().run_line_magic('ls', '*.txt')


# In[149]:


all_lines('outfile.txt', 'myconfig.txt', 'myfile2.txt', 'wcfile.txt')


# In[150]:


get_ipython().system('cat outfile.txt')


# In[151]:


def myfunc(a, b, *args):
    return f'{a=}, {b=}, {args=}'


# In[152]:


myfunc(10, 20, 30, 40, 50)


# In[153]:


def myfunc(a, b=999, *args):
    return f'{a=}, {b=}, {args=}'


# In[155]:


myfunc(2)


# In[156]:


myfunc(2, 4)


# In[157]:


myfunc(2, args=(100, 200, 300))


# In[158]:


def myfunc(a, *args, b=999):  # b is a keyword-only parameter
    return f'{a=}, {b=}, {args=}'


# In[159]:


myfunc(10, 20, 30, 40, 50)


# In[160]:


myfunc(10, 20, 30, 40, 50, b=888)


# In[161]:


myfunc(10, b=888, 20, 30, 40, 50)


# In[ ]:





# # Parameter types
# 
# 1. Mandatory parameters
# 2. Optional parameters (with defaults)
# 3. `*args` — uncaptured positional arguments
# 4. keyword-only parameters 

# In[162]:


def myfunc(a, *args, b):    # b is still positional only *AND* mandatory
    return f'{a=}, {b=}, {args=}'


# In[163]:


myfunc(10, 20, 30, 40, 50)


# In[164]:


myfunc(10, 20, 30, 40, 50, b=777)


# # `**kwargs`
# 
# dict with keyword arguments that no other parameter grabbed

# In[166]:


def myfunc(a, b=10, **kwargs):
    return f'{a=}, {b=}, {kwargs=}'


# In[167]:


myfunc(2)


# In[168]:


myfunc(2, 4)


# In[169]:


myfunc(2, 4,6)


# In[170]:


myfunc(2, 4, x=100, y=200, z=300)


# In[171]:


def write_config(filename, **kwargs):
    with open(filename, 'w') as outfile:
        for key, value in kwargs.items():
            outfile.write(f'{key}={value}\n')


# In[172]:


write_config('myconfig.txt', a=100, b=[20, 30, 30], c=200)


# In[173]:


get_ipython().system('cat myconfig.txt')


# In[175]:


def write_config(filename,  sep='=', **kwargs):
    with open(filename, 'w') as outfile:
        for key, value in kwargs.items():
            outfile.write(f'{key}{sep}{value}\n')


# In[176]:


write_config('myconfig.txt', a=100, b=[20, 30, 30], c=200)


# In[177]:


get_ipython().system('cat myconfig.txt')


# In[180]:


write_config('myconfig.txt', '::', a=100, b=[20, 30, 30], c=200)


# In[181]:


get_ipython().system('cat myconfig.txt')


# In[182]:


def myfunc(*args, **kwargs):
    return f'{args=}, {kwargs=}'


# In[183]:


myfunc(10, 20, 30, a=100, b=200, c=300)


# In[188]:


def myfunc(x, y, *args, z=100, **kwargs):
    return f'{x=}, {y=}, {args=}, {z=}, {kwargs=}'


# In[189]:


myfunc(10, 20, 30, a=100, b=200, c=300)


# # Exercise: xml
# 
# 1. Write a function, `xml`, that returns a string with XML.
# 2. Arguments will be as follows:
#     - First positional is `tagname`, a string with the name of the tag
#     - Second positional is `text`, a string (optional) with the text
#     - Others will be keyword arguments, used in the opening tag as attributes
<firstname>Reuven</firstname>

<name>
    <first>Reuven</first>
    <last>Lerner</last>
</name>


<user_info>
    <name language="English">
        <first>Reuven</first>
        <last>Lerner</last>
    </name>
    <company></company>
</user_info>
# In[ ]:


print(xml('foo'))               # first argument = tagname
# <foo></foo>

print(xml('foo', 'bar'))        # second (optional) argument = content
# # # # <foo>bar</foo>

print(xml('a',
          xml('b',
              xml('c', 'hello'))))
# # # # # # <a><b><c>hello</c></b></a>

# # # kwargs become attributes in opening tag

print(xml('tag', 'text', a=1, b=2, c=3))

# # # # <tag a="1" b="2" c="3">text</tag>

print(xml('tag', 'text', a=1, b=2))
# # # # <tag a="1" b="2">text</tag>

print(xml('tag', a=1, b=2))
# # # # # <tag a="1" b="2"></tag>


# In[198]:


def xml(tagname, text='', **kwargs):
    attributes = ''
    for key, value in kwargs.items():
        attributes += f' {key}="{value}"'
    
    return f'<{tagname}{attributes}>{text}</{tagname}>'

print(xml('foo')) 
print(xml('foo', 'bar')) 

print(xml('a',
          xml('b',
              xml('c', 'hello'))))

print(xml('tag', 'text', a=1, b=2, c=3))
print(xml('tag', 'text', a=1, b=2))
print(xml('tag', a=1, b=2))


# In[ ]:





# # Parameter types
# 
# 1. Mandatory parameters
# 2. Optional parameters (with defaults)
# 3. `*args` — uncaptured positional arguments
# 4. keyword-only parameters 
# 5. `**kwargs` -- uncaptured keyword arguments

# In[199]:


x = 100

if True:
    x = 200
    
x


# In[200]:


x = 100

print(f'{x=}')


# # Scopes
# 
# - `L` Local — start here if you're in a function
# - `E` Enclosing
# - `G` Global — start here if you're *NOT* in a function
# - `B` Builtin

# In[201]:


'x' in globals() 


# In[202]:


my_amazing_variable_name = 12345


# In[203]:


'my_amazing_variable_name' in globals()


# In[204]:


globals()['my_amazing_variable_name']


# In[205]:


x = 100

def myfunc():
    print(f'In myfunc, {x=}')  # is x local?  NO... is x global? YES

print(f'Before, {x=}')  # is x global? YES
myfunc()
print(f'After, {x=}')   # is x global? YES


# In[206]:


'x' in myfunc.__code__.co_varnames


# In[207]:


x = 100

def myfunc():
    x = 200
    print(f'In myfunc, {x=}')   # is x local?

print(f'Before, {x=}')  # is x global? YES
myfunc()
print(f'After, {x=}')    # is x global? YES


# In[208]:


myfunc.__code__.co_varnames


# In[209]:


x = 100

def myfunc():
    print(f'In myfunc, {x=}')  # is x local? 
    x = 200

print(f'Before, {x=}')  # is x global? YES
myfunc()
print(f'After, {x=}')   


# In[210]:


myfunc.__code__.co_varnames


# In[211]:


x = 100

def myfunc():
    x = x + 1
    print(f'In myfunc, {x=}')  # is x local? 

print(f'Before, {x=}')  # is x global? YES
myfunc()
print(f'After, {x=}')   


# In[215]:


x = 100

def myfunc():
    global x
    x = 200
    print(f'In myfunc, {x=}')  

print(f'Before, {x=}')  
myfunc()
print(f'After, {x=}')   


# In[213]:


myfunc.__code__.co_varnames


# In[216]:


def myfunc(x):
    global x
    print(x)


# # Next time
# 
# - Comprehensions
# - Sorting
# - Modules

# In[ ]:




