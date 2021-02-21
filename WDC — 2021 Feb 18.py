#!/usr/bin/env python
# coding: utf-8

# # Agenda
# 
# 1. virtualenv
# 2. Objects!
# 

# In[1]:


s = 'abcd'
type(s)


# In[2]:


n = 123
type(n)


# In[3]:


d = {'a':1, 'b':2, 'c':3}
type(d)


# # What is an object?
# 
# 1. `id` -- unique ID numbers
# 2. `type` -- every object has a class/type
# 3. attributes

# In[4]:


type(str)


# In[5]:


type(int)


# In[6]:


type(dict)


# In[7]:


type(type)


# In[8]:


# simplest Python class ever

class SimpleClass:
    pass


# In[9]:


type(SimpleClass)


# In[12]:


# two instances of SimpleClass!
a = SimpleClass()
b = SimpleClass()


# In[13]:


dir(a)


# In[14]:


dir(b)


# In[15]:


a.x = 100
a.y = {10, 20, 30, 40, 50}

b.q = [100, 200, 300]
b.r = {'a':1, 'b':2}


# In[16]:


vars(a)   # what attributes did I define on a?


# In[17]:


vars(b)


# In[18]:


a.x


# In[19]:


a.y


# In[20]:


b.q


# In[21]:


b.r


# In[22]:


a.q


# In[25]:


class SimpleClass:
    def __init__(self):
        self.x = 100
        self.y = [10, 20, 30]

a = SimpleClass()
b = SimpleClass()


# In[26]:


vars(a)


# In[27]:


vars(b)


# In[ ]:


a = SimpleClass()

    # this runs SimpleClass.__new__
    #    creates the new object, which I'll call "o"
    # call __init__(o)  -- pass "o" to __init__ as an argument
    #    __init__gets the new object, calling it "self"
    #    in __init__, we add new attributes to "o"
    # returns "o", the new object


# In[29]:


class SimpleClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

a = SimpleClass(10, [10, 20, 30])
b = SimpleClass(200, [1000, 2000])


# In[30]:


vars(a)


# In[31]:


vars(b)


# In[33]:


class Person:
    def __init__(self, name):
        self.name = name
        
    def get_name(self):
        return self.name
    
    def set_name(self, new_name):
        self.name = new_name
        
p1 = Person('name1')
p2 = Person('name2')

print(f'Hello, {p1.get_name()}')
p1.set_name('asdfasfafa')
print(f'Hello, {p1.get_name()}, with a new name')


# In[34]:


class Person:
    def __init__(self, name):
        self.name = name
                
p1 = Person('name1')
p2 = Person('name2')

print(f'Hello, {p1.name}')
p1.name = 'asdfasfafa'
print(f'Hello, {p1.name}, with a new name')


# In[35]:


Person.__bases__


# In[36]:


object in Person.__bases__


# In[37]:


isinstance(p1, Person)


# In[38]:


isinstance(p1, object)


# In[39]:


class Person:
    def __init__(self, name):
        self.name = name
        
    def greet(self):
        return f'Hello, {self.name}!'


# In[40]:


p1 = Person('name1')
p2 = Person('name2')

print(p1.greet())


# In[54]:


class Person:
    global population
    population = 0

    def __init__(self, name):
        self.name = name
        Person.population += 1
        
    def greet(self):
        return f'Hello, {self.name}!'
    
print(f'Before, population = {Person.population}')
p1 = Person('name1')
p2 = Person('name2')
print(f'After, population = {Person.population}')
print(f'After, p1.population = {p1.population}')
print(f'After, p2.population = {p2.population}')

print(p1.greet())
print(p2.greet())


# # Searching for variables and attributes
# 
# - Variable search is:
#     - `L` local
#     - `E` enclosing function
#     - `G` global
#     - `B` builtins
# - Attribute search is:
#     - `I` instance
#     - `C` class
#     - `P` parent(s) of the class
#     - `O` object (top of the hierarchy)

# In[48]:


Person.population


# In[49]:


Person.population = 500


# In[50]:


vars(Person)


# In[53]:


print("A")
class Person:
    print("B")
    my_attr = 0
    
    def __init__(self, name):
        print("C")
        self.name = name
    print("D")
print("E")

p1 = Person('name1')
p2 = Person('name2')


# In[58]:


class Person:
    global population
    population = 12345


# In[59]:


population


# In[70]:


class Person:
    def __init__(self, name):
        self.name = name
        
    def greet(self):
        return f'Hello, {self.name}!'
    
p1 = Person('name1')
p2 = Person('name2')

print(p1.greet())
print(p2.greet())


class Employee(Person):   # Employee is-a Person

    def __init__(self, name, employee_id):
        #Person.__init__(self, name)  # better in Python 2!
        super().__init__(name)        # better in Python 3!
        self.employee_id = employee_id
        
    def greet(self):
        return f'{super().greet()} (fellow employee!)'
            
e1 = Employee('emp1', 1) # e1 has __init__? NO.  Employee has __init__? YES
e2 = Employee('emp2', 2)

print(e1.greet())  # e1 has greet? NO.  Employee has greet? NO. Person has greet? YES
print(e2.greet())


# In[66]:


vars(e1)


# In[67]:


vars(e2)


# In[64]:


# e1.greet() -> Person.greet(e1)

Person.greet(e1)


# # Next time
# 
# 1. Magic methods
# 2. Exceptions
# 3. Test

# In[ ]:




