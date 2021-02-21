#!/usr/bin/env python
# coding: utf-8

# # Agenda
# 
# 1. Magic methods
# 2. Exceptions
# 3. Questions
# 4. Survey + test

# In[4]:


import random

class Person:
    x = 100   # Person.x
    
    def __init__(self, name):
        num = random.randint(0, 100)
        
        self.name = name
        self.num = num
        print(Person.x)
        
    def greet(self):
        return f'Hello, {self.name}!'
    
    def very_excited_greeting(self):
        return f'{self.greet()}!!!!!'


# In[3]:


p = Person('name')
print(p.very_excited_greeting())  # 


# In[ ]:





# # Name search
# 
# - Variable: L (local), E (enclosing), G (global), B (builtins)
# - Attribute: I (instance), C (class), P (parents), O (object)

# In[5]:


def myfunc():
    asdfafafafafa


# In[6]:


myfunc()


# In[7]:


asdfafafafafa = 5

myfunc()


# In[8]:


class A:
    def __init__(self, x):
        self.x = x
        
    def x2(self):
        return self.x * 2
    
class B:
    def __init__(self, y):
        self.y = y
        
    def y3(self):
        return self.y * 3
    
class Q(A, B):
    def __init__(self, x, y):
        A.__init__(self, x)
        B.__init__(self, y)


# In[9]:


Q.__mro__ #  method resolution order


# In[10]:


q = Q(10, 20)


# In[11]:


class A:
    def __init__(self, x):
        self.x = x
        
    def x2(self):
        return self.x * 2
    
class B:
    def __init__(self, y):
        self.y = y
        
    def y3(self):
        return self.y * 3
    
class Q(A, object, B):
    def __init__(self, x, y):
        A.__init__(self, x)
        B.__init__(self, y)


# In[17]:


class A:
    def __init__(self, x):
        self.x = x
        self.z = 100
        
    def x2(self):
        return self.x * 2
    
    def hello(self):
        return 'Hello from A!'
    
class B:
    def __init__(self, y):
        self.y = y
        self.z = 200
        
    def y3(self):
        return self.y * 3
    
    def hello(self):
        return 'Hello from B!'
    
class Q(A, B):
    def __init__(self, x, y):
        super().__init__(x)
#         A.__init__(self, x)
#         B.__init__(self, y)


# In[18]:


q = Q(10, 20)

q.hello()   # up to order in __mro__


# In[19]:


q.z  # up to order in  __init__


# In[20]:


q.y3()   # PO


# In[23]:


class Person:
    def __init__(self, name):
        self.name = name
        
    def greet(self):
        return f'Hello, {self.name}!'
    
    def __str__(self):
        return f'I am a Person, named {self.name}!'
    
p = Person('name')


# In[24]:


print(p)  # --> print(str(p)) --> print(p.__str__()) -> print(Person.__str__(p)) --> print(object.__str__(p))


# # When we say `print(p)`
# 
# - `print(str(p))`
# - `print(p.__str__())`
# - [a bit of magic]
# - `print(Person.__str__(p))`
# - `print(object.__str__(p))`

# In[25]:


# an_instance.a_method()  --> Class.a_method(an_instance)


# In[26]:


s = 'abcd'

s.upper() 


# In[27]:


str.upper(s)


# In[28]:


print(p)


# In[33]:


class Person:
    def __init__(self, name):
        self.name = name
        
    def greet(self):
        return f'Hello, {self.name}!'


    def __str__(self):
        return f'[str] I am a Person, named {self.name}!'
    
    def __repr__(self):
        return f'[repr] I am a Person, named {self.name}!'
    
p = Person('name')


# In[34]:


print(p)


# In[35]:


str(p)


# In[36]:


repr(p)


# In[37]:


p


# In[38]:


[p, p, p]


# In[39]:


print([p,p,p])


# In[40]:


print([str(p), str(p), str(p)])


# # Exercise: Printing ice cream
# 
# 1. Add `__repr__` to `Scoop`. If I say `str(s1)`, we will get back the string `"Scoop of chocolate"`.
# 2. Add `__repr__` to `Bowl`. If I say `str(b)`, we will get back something like this:
# 
# ```
# Bowl of:
#     - Scoop of chocolate
#     - Scoop of vanilla
#     - Scoop of coffee
# ```
# 

# In[42]:


class MyClass:
    def __init__(self, x):
        self.x = x
        
    def __len__(self):
        return 123
        
m = MyClass('abcde')        

len(m)


# In[43]:


m.__len__()  # double underscore, before and after == "dunder"


# In[49]:


class MyClass:
    def __init__(self, x):
        self.x = x
        
    def __len__(self):
        return 123.0
    
    def __str__(self):
        return 5
        
m = MyClass('abcde')        


# In[50]:


print(m)


# In[51]:


del(x)


# In[52]:


mylist = [10, 20, 30]

x = mylist[99999]


# In[53]:


x


# In[56]:


mylist = [10, 20, 30]

print('Before')

try:
    print('A')
    x = mylist[99999]
    print('B')
except IndexError as e:
    print(f'There was a problem: {e}')

print('After')


# In[60]:


mylist = [10, 20, 30]

print('Before')

try:
    print('A')
    print(100/0)
    print('B')
except IndexError as e:
    print(f'There was a problem: {e}')
except ZeroDivisionError as e:
    print(f'Stop dividing by zero!')
except Exception as e:
    print(f'Something else')

print('After')


# In[61]:


100/0


# In[62]:


import sys


# In[63]:


sys.excepthook


# In[69]:


class OnlyStringsWelcomeHereError(Exception):
    pass

def hello(name):
    if isinstance(name, str):
        return f'Hello, {name}!'
    else:
        raise OnlyStringsWelcomeHereError('You did not give me a string!')


# In[70]:


hello('world')


# In[71]:


try:
    hello(5)
except OnlyStringsWelcomeHereError as e:
    print(f'I had a problem: {e}')


# In[ ]:




