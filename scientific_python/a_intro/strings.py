#!/usr/bin/env python3


### str ###

## Python 2 vs 3 ##

from __future__ import division, print_function, unicode_literals

# And once again 2 vs 3. Python 2 and 3 differ in one more core feature: string
# encoding. In Python 2 str class corresponds to a sequence of bytes but in
# Python 3 it corresponds to a sequence of Unicode encoded symbols. You may
# think that in scientific applications encoding of strings doesn't matter. But
# in real life you can catch some troubles when grab ASCII data from files with
# popular packages like pandas and numpy. Again, you should orient to Python 3
# behaviour. In Python 2 importing unicode_literals from __future__ makes all
# strings in current file Unicode but it cannot solve all problems with data
# obtained from old-fashion code. If you have to support Python 2 than have a
# look at six module: https://pythonhosted.org/six/


## Basics ##

# str is a built-in type representing a sequences of Unicode characters (bytes
# in Python 2). Objects of str are immutable, hashable and iterable.

# Single and double quotes are equivalent. I prefer single quotes but when we
# we have to use quote of some type as a symbol inside the string it is
# convenient to use quotes of the other type.
s = 'Hello world'
ss = "Hello world"
assert s == ss
assert s[:5] == 'Hello'
try:
    s[0] = 'h'  # str is immutable
except TypeError as e:
    # Use of single quote inside double quotes:
    assert str(e) == "'str' object does not support item assignment"
set_with_str = {s}  # str is hashable
assert s == set_with_str.pop()

# str can be constructed with one more type of quotes: triple quotes (double
# prefered). Instead of other two types this one can be used for multiline
# string:
"""Also this type of string is used for two more purposes:
  - As comments (like this one) (it isn't recommended by PEP 8).
  - As documentation string for function or class (see bellow).
"""
def my_mystery_function(name='Joe'):
    """This function does black magic and can destroy your life.
    
    Keyword arguments:
    name -- The name of person to curse.
    """
    return name + ' is cursed'

def my_simple_function():
    """Even one-line docstrings should be in triple quotes (PEP 257)"""
    return

# These docstrings can be accessed via __doc__ variable (because functions are
# objects too). You can see a "documentation" produced by these docstrings when
# use built-in help() function in the python command prompt or when use "?" in
# ipython/Jupyter.
assert 'Keyword' in my_mystery_function.__doc__.splitlines()[2]
# Here splitlines() produces a list of string's lines.

assert 'pep' in my_simple_function.__doc__.lower()
# Here lower() makes all characters have a lower case. Similarly upper() works.
# One more method of these family is capitalize() that makes the first
# character have upper case and other characters have lower case.


