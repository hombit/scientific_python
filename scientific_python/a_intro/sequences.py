#!/usr/bin/env python3
# Make this file executable
# $ chmod +x strings.py
# Now you can start it just by name:
# $ ./strings.py
# Pay attention to write /usr/bin/env instead of a direct path to you python
# interpreter. This path can vary from system to system and when virtualenv is
# used.

from __future__ import division, print_function


### list ###

## "[]" operator

# Empty list
a = []
a = list()

# list is a collection of various elements that could be and could be not
# objects of the same type. List could be initialized using "[]" operator:
a = [1, 2.3, 4.3, -1+3.5j]
print(a)
# [1, 2.3, 4.3]

# Elements access works as expected, index for the first element is zero, and
# for last element is -1
print(a[0], a[-1], a[-2], a[-3], a[-4])
# 1 (-1+3.5j) 4.3 2.3 1
a[-1] = 12
print(a)
# [1, 2.3, 4.3, 12]

## Basic slicing ##

# Operator "[]" supports slicing. We will discuss slicing in more details later
# with numpy module.
b = a[1:-1]
print(b)
# [2.3, 4.3]
b = a[2:]
print(b)
# [4.3, 12]
b = a[1:2:]
print(b)
# [2.3]
b = a[::2]
print(b)
# [1, 4.3]
a[::2] = [-1, -4.3]
print(a)
[-1, 2.3, -4.3, 12]

## Size of sequence ## 

# Built-in function len() returns sequence size
print(len(a), len(b))
# 4 2

## Methods of the list and "del" statement ##

# list has some basic methods to manipulate with its data
print(a)
# [-1, 2.3, -4.3, 12]

# Add element
a.append(0)
print(a)
# [-1, 2.3, -4.3, 12, 0]

# Add object -500 into index 1. Negative indices can be used
a.insert(1, -500)
print(a)
# [1, -500, 2.3, 4.3, (-1+3.5j), 0]

# Remove and return the last element
x = a.pop()
print(x, a)
# 0 [-1, -500, 2.3, -4.3, 12]

# Or any element by index
x = a.pop(1)
print(x, a)
# -500 [-1, 2.3, -4.3, 12]

# Also you can delete any object and in particular sequence element using "del"
# statement
del a[1]
print(a)
# [-1, -4.3, 12]

# Add all elements from another sequence (any iterabel object in general)
b = [1,2,3]
a.extend(b)
print(a)
# [-1, -4.3, 12, 1, 2, 3]

# .sort() performs in place and doesn't return anything
a.sort()
print(a)
# >> [-4.3, -1, 1, 2, 3, 12]


### For loop and "in" statement ###

## Basic example ##

# In Python for loop has a bit different syntax than in C-like languages. NB
# indention:
for x in [1,2,3,4]:
    print(x)
# 1
# 2
# 3
# 4

# Do not modify list while looping!

## range() ##

# Looping works for any iterable variable. The special case of iterable object
# is generator. Generator doesn't hold all yielding values but calculate them
# on each lookup. The basic example of generators is range() that yields
# sequence of integers but doesn't hold them all in memory.
# In Python 2 use xrange() instead of range().
for x in range(3):
    print(x)
# 0
# 1
# 2

# Another syntax:
for x in range(6, -1, -2):
    print(x)
# 6
# 4
# 2
# 0

## enumerate()

# Often we need to iterate both list elements and its indexes. Of course, you
# can iterate over index `for i in range(len(a))` and then get element by its
# index but python has specific built-in function enumerate() for it.

a = ['hello', 'world']
for i, x in enumerate(a):
    print(i, x)
# 0 hello
# 1 world

## "in" ##

# "in" statement has a stand-alone usage, it is an binary operator that returns
# True when the first variable is a member of the second variable.
a = [1, 2, 3, 4]
print(1 in a)
# True

try:
    a in 1
except TypeError as e:
    print(e)
# argument of type 'int' is not iterable

# Say hello exceptions, I wouldn't tell a lot about them, basically they work as
# in other popular objective oriented languages like C++ or Java.



### Object model in Python ###

## Variables as references ##

# Most of the variables you will use in Python holds references to associated
# objects, not object themselves. The exceptions of this rule are some
# built-in objects like numbers.
# Let's show what does it mean practically:
a = [1, 2, 3]
b = a  # Copy reference to the list, not list itself
a[0] = -1
print(a, b)
# [-1, 2, 3] [-1, 2, 3]

# But:
a = 1
b = a
a += 1
print(a, b)
# 2 1

# To copy list with its values use copy() method or module `copy` of standard
# library
a = [1, 2, 3]
# We can use import in the any part of the code. Exception is import __future__
import copy
b = copy.copy(a)  # or just a.copy()
a[0] = -1
print(a, b)
# [-1, 2, 3] [1, 2, 3]

# More complex example:
a = [1, 2, 3, [4, 5, 6]]
b = a.copy()
a[-1][0] = -100
print(a, b)
# [1, 2, 3, [-100, 5, 6]] [1, 2, 3, [-100, 5, 6]]

# What happens? a.copy() is shallow and copied only members of `a`, while its
# last member is a reference to another list that has copied by reference not
# by values of its members. If you want copy to be deep (recursive) and copy
# all sub-members and sub-attributes of the object then you can use
# copy.deepcopy() function from `copy` module:
a = [1, 2, 3, [4, 5, 6]]
b = copy.deepcopy(a)
a[-1][0] = -100
print(a, b)
# [1, 2, 3, [-100, 5, 6]] [1, 2, 3, [4, 5, 6]]

## "is" ##

# "is" statement can be used to check if two variables hold references to the
# same object:
a = [1, 2, 3]
b = a
print(a is b)
# True
b = a.copy()
print(a is b)
# False

# Let's compare "is" with equality operator "==". "==" checks if all members
# of one object equals to the members of another object:
a = [1, 2, 3]
b = a.copy()
print(a == b, a is b)
# True False
print([] == [], [] is [])
# True, False
print(True == 1, True is 1)
# True False

# Avoid using of "is" for basic types such numbers. It is highly implementation
# dependent and can cause unexpected results:
a = 511
print(511 is 511, a is 511, -100 is -100)
# True False False

## None ##

# None is a special built-in object. It is used when you need to return "empty" # value from the function or send it as function argument. Usually None uses as
# default value of optional argument of function (see dict.get() bellow). It is
# an only object of NoneType, its Boolean value is False and every variable
# that holds None refers to this object. If function doesn't have "return"
# statement or it is empty then it returns None.
# You can check that your variable is None in several ways, but using of "is"
# and "is not" statements are recommended (see PEP 8, http://pep8.org).
none = None
print(none is None)  # Recommended
# True
a = 'hello'
print(a is not None)  # Recommended
# True
print(none == None)  # Not recommended
# True


### tuple ###

## Basics ##

# Empty tuple
t = ()

t = (1, 2, 10+3j, 1, 'hello')
print(t.count(1))
# 2
print(t.index(1))
# 0

# Elements of a tuple can be accessed just like list's elements:
print(t[0])
# 1
print(t[-1])
# 'world'

## One element tuple ##

# Be very careful when produce one element tuples. This is not a tuple:
a = (1)
print(a, type(a))
# 1 <class 'int'>
# But this is a tuple:
a = (1,)
print(a, tuple(a))
# (1,) <class 'tuple'>
# I strongly recommend to use trailing comma in every place you are afraid to
# make a mistake like this. In the modern Python trailing comma is valid in
# almost every place you will want to use it.

## Mutability ##

# Tuples are immutable objects. It means that you cannot change there size,
# replace or add elements. NB that even operator "+=" will produce new object,
# not update current:
t = (1, 2, 10+3j, 1, 'hello')
tt = t
t += (-10, 'world')
print(t)
# (1, 2, (10+3j), 'hello', -10, 'world')
print(tt)
# (1, 2, (10+3j), 'hello')

try:
    t[0] = -1
except TypeError as e:
    print(e)
# 'tuple' object does not support item assignment    

# Of course you still can modify mutable elements of the tuple:
t = (1, [2, 3])
t[1][0] = -100
print(t)
# (1, [-100, 3])

## Unpack values ##

t = (1,2,3)
a, b, c = t
print(a, b)
# 1 2
a, b = b, a
print(a, b)
# 2 1

# Use _ symbol to skip one of the values:
a, _, b = t
print(a, b)
# 1 3

## Return numerical values from functions ##

# Going ahead let me say that returning numerical values from the function will
# produce tuple:
def f():
    return 1, 2
x = f()
print(x, type(x))
# (1, 2) <class 'tuple'>
a, b = f()
print(b, a)
# 2 1


### dict ###

## Construction ##

# Empty dict
d = {}
d = dict()

d = {0: 'zero', 2: 'two', 10: 'ten'}
print(d)

## Value access

# Value access syntax is the same as for lists:
print(d[0])
# zero
d[12] = 'twelve'
print(12 in d)
# True

# Access to absent key will produce exception
try:
    print(d[500])
except KeyError as e:
    print("Key doesn't exist:", e)
# Key doesn't exist: 500

# Instead you can use get() with second optional argument that holds default
# return value:
print(d.get(500, 'Unknown value'))
# Unknown value

# get() without second argument will return None, e.g. the default value of
# the second argument of get() is None
print(d.get(500))
# None

## Other methods ##

# Remove and return value by key:
print(d.pop(0))
# zero
# "del" statement works as usual:
del d[10]

# Add content from another dictionary, it replaces existing keys with new
# values:
d = {0: 'zero', 1: 'one'}
dd = {1: 'ONE', 2: 'TWO'}
d.update(dd)
print(d)
# {0: 'zero', 1: 'ONE', 2: 'TWO'}

## Hashable variables ##

# Note that not any element can be a key of a dict, but only hashable objects.
# Hashable object must have specific __hash__() method that returns integer
# number and such an object can be used as an argument of buil-in hash()
# function that is works just like __hash__(). In general, all immutable
# objects are hashable. So you can use number types, str and tuple as keys and
# cannot use list and dict.

d = {}
d[3 + 0j] = 'complex'
d[(1, 2, 3)] = 'tuple'
d['hello world'] = 'str'
try:
    d[[1, 2, 3]] = 'list'    
except TypeError as e:
    print(e)
# unhashable type: 'list'    

## Iterating ##

d = {0: 'zero', 2: 'two', 10: 'ten'}

# Iteration throw dictionary will yield its keys in "random" (implementation
# -specific) order. This equivalent to `for k in d.keys()`:
for k in d:
    print(k)
# 0
# 2
# 10
# The order can differ

# "in" statement will also look at keys, not values:
print(0 in d)
# True
print('zero' in d)
# False

# You can iterate over values of a dictionary using values(). In Python 2 use
# viewvalues() instead.
for v in d.values():
    print(v)
# zero
# two
# ten
# The order can differ

# Also you can iterate over key-value pairs using items(). In Python 2 use
# viewitems() instead.
for k, v in d.items():
    print(k, v)
# 0 zero
# 2 two
# 10 ten
# The order can differ



### set and frozenset ###

# I have a very good definition for this type. set is a hash-set. You can think
# that set is a dict without values: it can fast (O(n)) check if the element
# presented, you can add and delete elements from it. As a dict set is
# unordered, that means that iteration and popping elements orders are
# implementation specific. Set can hold only hashable elements.

# Empty set
s = set()

s = {1,}  # This is set, not dict. Trailing comma is optional.
s.add(1)
s.add(30)
print(s)
# {1, 30}

print(s.pop(), s.pop())
# 30 1
# Order is implementation specific

s = set(range(5))
s.discard(3)
s.discard(10)  # Does nothing
print(s)

ss = {-1, -2}
s.update(ss)
print(s)
# {-1, -2, 0, 1, 2, 4}

## frozenset ##

# frozenset is a immutable variant of set.

fs = frozenset(range(5))
s = {}
s[fs] = 'frozenset'
print(s)
# {frozenset({0, 1, 2, 3, 4}): 'frozenset'}



### Examples ###

# I try to keep examples clean but may be not fast

## Sorted list without duplicates ##

a = [1, 0, 0, -1, 1, 0, 3, 1, 0, 5, 2]
b = sorted(list(set(a)))
print(b)
# [-1, 0, 1, 2, 3, 5]

## Count the most frequent element ##

d = {}
max_a_item = a[0]
for x in a:
    d[x] = d.get(x, 0) + 1
    if d[x] > d[max_a_item]:
        max_a_item = x
print(max_a_item)
# 0
