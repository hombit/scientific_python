#!/usr/bin/env python3


# -- Python 2 vs 3 --

from __future__ import division, print_function, unicode_literals

# And once again 2 vs 3. Python 2 and 3 differ in one more core feature: string
# encoding. In Python 2 `str` class corresponds to a sequence of bytes but in
# Python 3 it corresponds to a sequence of Unicode encoded characters. You may
# think that in scientific applications encoding of strings doesn't matter. But
# in real life you can catch some troubles when grab ASCII data from files with
# popular packages like `pandas` or `numpy`. Again, you should orient to Python
# 3 behaviour. In Python 2 importing `unicode_literals` from `__future__` makes
# all string declarations return Unicode typed variables in current file but it
# cannot solve all problems with data obtained from old-fashion code.
# If you have to support Python 2 than have a look at `six` module:
# <https://pythonhosted.org/six/>


# We will use it later:
from sys import version_info


# ## Basics

# ### Declaration and slicing

# `str` is a built-in type representing a sequences of Unicode characters (bytes
# in Python 2). Objects of `str` are immutable, hashable and iterable.

# Single `'` and double `"` quotes are equivalent. I prefer single quotes but
# when we have to use quote of some type as a symbol inside the string it is
# convenient to use quotes of the other type.
s = 'Hello world'
ss = "Hello world"
assert s == ss  # assert raises AssertionError if boolean value is False
assert s[:5] == 'Hello'
try:
    s[0] = 'h'  # str is immutable
except TypeError as e:
    # Use of single quote inside double quotes:
    assert str(e).endswith("object does not support item assignment")
set_with_str = {s}  # str is hashable
assert s == set_with_str.pop()

# ### Docstring

# `str` can be constructed with one more type of quotes: triple quotes (double
# prefered). Instead of other two quote types this one can be used for
# multiline string:
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


# These docstrings can be accessed via `.__doc__` attribute (because functions
# are objects too). You can see a "documentation" produced by these docstrings
# when use built-in `help()` function in the python command prompt or when use
# "?" in `ipython`/`Jupyter`.
assert my_mystery_function.__doc__.endswith('\n    ')
# Here `.endswith(x)` checks with the string ends with `x` string. Also look at
# similar `.startswith()` method. `'\n'` is end of line symbol, look discussion
# about `\` symbol bellow.
assert 'Keyword' in my_mystery_function.__doc__.splitlines()[2]
# Here `.splitlines()` produces a list of the string's lines.

assert 'pep' in my_simple_function.__doc__.lower()
# Here `.lower()` makes all characters have a lower case. Similarly `.upper()`
# works. One more method of these family is `.capitalize()` that makes the
# first character have upper case and other characters have lower case.

# `str` has a lot of methods, use them instead of write your own code:
# <https://docs.python.org/3/library/stdtypes.html#string-methods>

# ### Raw strings

# Ordinary strings declaration supports `'\'` symbol for special characters
# like `'\n'` — end of line, `"\'"` and `'\"` produces actual quote instead
# of end of string declaration, `'\\'` produces `\` symbol itself, see full
# list on <https://docs.python.org/3/reference/lexical_analysis.html>

# However, using of `\` can be confusing and ugly, for example in regular
# expressions (see `re` module of standard library) or $\LaTeX$ (e.g. as plot
# label in [`matplotlib`](http://matplotlib.org)). If you would like to ignore
# all special characters in the string than use `r`/`R` symbol just before the
# first quote. String prefixes like `r` can be used with any quote type.
raw_string = r'Hello\nWorld'
string = 'Hello\nWorld'
assert len(raw_string.splitlines()) == 1
assert len(string.splitlines()) == 2

# ### Other prefixes

# There are two more types of prefixes: `b`/`B` and `u`/`U`. They are used to
# declare `bytes` (`str` in Python 2) and `str` (`unicode` in Python 3). Prefix
# `f`/`F` will be discussed in the next section.


# ## Formatting

# There are three syntaxes of string formatting In the modern Python. First two
# of them are described in examples on <https://pyformat.info>. Here we will
# discuss only basics of formatting.

# ## Operator `%`

# Operator `%` is the most old and less powerful Python formatting tool, I
# recommend to not use it in new programs.

s = '%d' % 1
assert s == '1'

x = 1
s = '%s = %d' % ('x', x)
assert s == 'x = 1'

# Syntax of format mini-language is very close to `C`'s `*printf` one and
# described on
# <https://docs.python.org/3/library/string.html#format-specification-mini-language>

# ### `str.format()`

# `.format()` method of `str` is preferred format tool. It has clear syntax,
# works on both Python 2 and 3 and much more powerful than `%` operator.

s = '{}'.format(1)
assert s == '1'

x = 1
s1 = '{} = {}'.format('x', x)
s2 = '{:s} = {:d}'.format('x', x)
# Arguments order isn't important:
s3 = '{name:s} = {value:d}'.format(name='x', value=x)
s4 = '{1} = {0}'.format(x, 'x')
assert s1 == s2 == s3 == s4

# Both index and name of the string element may be repeated
user = 'Anna'
s = 'Hello {0}! How do you do {0}?'.format(user)
assert s == 'Hello Anna! How do you do Anna?'


# Actual braces are produced by `'{{'` and `'}}'`:
s = r'{symbol} = m \times c^{{2}}'.format(symbol='E')

# ### `f` prefix

# `f` prefix is introduced in Python 3.6
# All code for this syntax is located in separate file `strings_f_prefix.py`
# because on Python prior 3.6 using of this prefix produces syntax error.
if version_info >= (3, 6):
    if __package__:
        from .strings_f_prefix import f_prefix
    else:
        from strings_f_prefix import f_prefix
    f_prefix()
