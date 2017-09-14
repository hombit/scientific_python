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


### tuple ###

##


### dict ###

# Construction #
d = {0: 'zero', 2: 'two', 10: 'ten'}
print()
