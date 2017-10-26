#!/usr/bin/env python3

from __future__ import division, print_function, unicode_literals

import copy

### Return ###

def one():
    print(1)
    return 1
assert one() == 1
# 1

# Functions are variables:
f = one
assert f() == 1

# if not return value or not "return" statement then functions returns None:
def none_function():
    return
assert none_function() is None

def pass_function():
    pass  # special statement for empty blocks
assert pass_function() is None

# Multiple comma separated values after "return" are packed into tuple
def one_two_tuple():
    return 1, 2
a, b = one_two_tuple()
assert (a == 1) and (b == 2)
assert (1, 2) == one_two_tuple()
assert isinstance(one_two_tuple(), tuple)
# Use built-in function isinstance() to check if an object is an instance of
# some class. isinstance() is recommended way by PEP 8, do NOT use more
# complicated expressions like `type(one_two_tuple()) is tuple`



### Arguments ###

## Positional arguments ##

def plus_one(x):
    return x + 1
x = 5    
assert x + 1 == plus_one(x)

def plus(x, y):
    return x + y
x = y = 3
assert x + y == plus(x, y)
# All positional arguments are required
try:
    plus(x)
    assert False
except TypeError as e:
    assert str(e).startswith('plus()')
    
## Keyword arguments ##

# First of all, positional arguments can be called as keywords
def minus(x, y):
    return x - y
a, b = 2, 5
assert a - b == minus(x=a, y=b)
assert a - b == minus(y=b, x=a)

# Keyword arguments always go after positional arguments (as in function
# definition, as in function call). Keyword arguments have default value,
# often (not always!) None is used as special default value (remember
# dict.get(key, default=None)).
def hello(name='Ira'):
    return '{} {}'.format('hello', name)
assert 'hello Ira' == hello()
assert 'hello Joe' == hello(name='Joe')

# Keyword argument can be called as positional one:
assert 'hello Julia' == hello('Julia')

if __package__:
    from .utils import parallelogram_volume
else:
    from utils import parallelogram_volume
a, b, c = 1, 2, 3    
assert a == parallelogram_volume(a)
assert a * b == parallelogram_volume(a=a, b=b)
assert a * b == parallelogram_volume(b=b, a=a)
assert a * b * c == parallelogram_volume(a, b, c)
assert a * b * c == parallelogram_volume(a, b, c=c)

# You should never use mutable value as a default. Functions in Python are
# objects and they hold there default values in the special attribute
# __defaults__.
assert parallelogram_volume.__defaults__ == (1, 1)

# When a function needs to use default value for its keyword argument it looks
# to this variable and takes (not copy!) the value from it. So if the default
# is mutable then it can be changed by function itself or returned to user and
# changed by her. This is an example of such behaviour:
def do_not_use_mutable_defaults(x=[]):
    x.append(1)
    return x
assert do_not_use_mutable_defaults() == [1]
assert do_not_use_mutable_defaults() == [1, 1]
assert do_not_use_mutable_defaults() == [1, 1, 1]

# If you really want this behaviour you should make it explicit. For example,
# write class with varying attribute (instead of varying default of keyword
# argument), implement __call__() method (then an object of your class can
# be called as a function using operator "()") and create an instance of this
# class. A short example:
class CallableWithMemory:
    __used_arguments = []

    def __call__(self, x):
        self.__used_arguments.append(x)
        # Return copied data to prevent modification of the attribute:
        return copy.deepcopy(self.__used_arguments)

callable_with_memory = CallableWithMemory()  # instance works as function
assert callable_with_memory(1) == [1]
assert callable_with_memory(2) == [1, 2]
l = callable_with_memory([3,4,5])
l[-1][-1] = -100  # object attribute hasn't changed!
assert callable_with_memory('hello') == [1,2,[3,4,5],'hello']


## Argument packing and unpacking ##

# A lot of these examples are Python 3 specific so they are located in separate
# module.
from sys import version_info
if version_info[0] >= 3:
    if __package__:
        from .functions_packing_unpacking import packing, unpacking
    else:
        from functions_packing_unpacking import packing, unpacking
    packing()
    unpacking()


## "lambda" statement ##

# Python has a special syntax for so called anonymous functions. Anonymous
# functions are useful when you would like to write one-line function in place
# instead of writing separate "def"-block.
# We will use reduce() function from `functools` standard library module (it is
# built-in function in Python 2) as an example. This function takes three
# positional arguments: a function of two variables, iterable and an initial
# value (optional). The function of two variable will take a pair of currently
# reduced variable (at the first step it is the first value of a collection of 
# initial value if specified) and the next value of the iterable and produce
# new current reduced value.
from functools import reduce
def sum_of_squares(x, y):
    return x + y**2
assert reduce(sum_of_squares, range(5), 0) == 30
# And an example with anonymous function produced by "lambda" statement:
assert reduce(lambda x, y: x + y**2, range(5), 0) == 30
# So the syntax of "lambda" statement as follows:
# lambda [arg, arg, ...]: one-line expression which result will be returned

# An object produced by "lambda" is similar to a one produced by "def".
# However, it isn't recommended by PEP 8 to assign this object to some 
# variable and use it after, because errors produced by anonymous functions
# are more difficult to debug.



### Examples ###

## Bisection ##

# Avoid to implement such algorithms yourself! You should prefer to use
# implementations prepared by community (`bisect` module of standard library,
# `scipy.optimization` module
# https://docs.scipy.org/doc/scipy/reference/tutorial/optimize.html). This is
# a training example.

# TODO: write something
