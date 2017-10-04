#!/usr/bin/env python3

from __future__ import division, print_function, unicode_literals


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
    assert str(e) == "plus() missing 1 required positional argument: 'y'"
    
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

def parallelogram_volume(a, b=1, c=1):
    return a * b * c
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
# class.

## Argument packing ##

# "*" symbol before argument name (usually it is named args) means that
# function takes any number of positional arguments and all of them are packed
# into one tuple.
def packed_args(*args):
    return args
assert packed_args(1) == (1,)
assert isinstance(packed_args(1), tuple)
assert len(packed_args(1)) == 1
assert packed_args() == tuple()
assert isinstance(packed_args(1, 2, 3), tuple)
assert len(packed_args(1, 2, 3)) == 3
assert (1, 2, 3) == packed_args(1, 2, 3)

# "**" before argument name (usually it is named kwargs — keyword arguments)
# means that function takes any number of keyword arguments and all of them are
# packed into one dict.
def packed_kwargs(**kwargs):
    return kwargs
x = packed_kwargs(key='value', one=1)
assert isinstance(x, dict)
assert len(x) == 2
assert ('key' in x) and ('one' in x)
assert ('value' in x.values()) and (1 in x.values())
try:
    packed_kwargs('hello')
    assert False
except TypeError as e:
    assert str(e) == "packed_kwargs() takes 0 positional arguments but 1 was given"

# And all together now!
def packed_args_kwargs(*args, **kwargs):
    return len(args), len(kwargs)
assert packed_args_kwargs(1, 2, 3, four=4, five=5) == (3, 2)

def packed_and_non_packed(x, *args, key=None, **kwargs):
    return len(args), len(kwargs)
assert packed_and_non_packed(1) == (0, 0)
assert packed_and_non_packed(1, 2, 3, four=4, five=5) == (2, 2)
assert packed_and_non_packed(1, 2, 3, four=4, five=5, key='value') == (2, 2)

## Arguments unpacking ##

# In the same way positional and keyword arguments can be passed in as a parts
# of iterable ordered variables and unpacked them inside the function.
a, b, c = 2, 3, 4
l = [a, b, c]
t = (a, b, c)
d = {'a': a, 'b': b, 'c': c}
volume = a * b * c
assert volume ==  parallelogram_volume(*l)
assert volume ==  parallelogram_volume(*t)
assert volume ==  parallelogram_volume(**d)
assert volume ==  parallelogram_volume(a, *(b, c))
assert volume ==  parallelogram_volume(a, **{'b': b, 'c': c})
assert volume ==  parallelogram_volume(*[a], c=c, **{'b': b})
assert volume ==  parallelogram_volume(a, *[b], c=c)


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
