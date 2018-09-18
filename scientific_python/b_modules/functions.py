#!/usr/bin/env python3

from __future__ import division, print_function, unicode_literals

import copy
import sys
from functools import reduce


# Functions are defined by `def` statement and located inside the block after
# the definition. A template of function is as follows:
# >>> def function_name(function_arguments, sepparated, by, commas):
# >>>     """Docstring, optional but better to have it"""
# >>>     Function_code_is_here
# >>>     Remember_indention
# >>>     return something, optional


# # `return` statement

# `return` exits the function and gives the value putted after it.

def one():
    """Prints "1" and returns integer 1"""
    print(1)
    return 1


assert one() == 1
# `1`


# Functions are variables, you can assign them and get their attributes:
f = one
assert f is one
assert f() == 1
# `hasattr` is a built-in function that object has an attribute:
assert hasattr(f, '__call__')
# `.__call__()` is what makes object callable, see details bellow
assert f() == f.__call__()
assert f.__doc__ is not None

# If no return value presented or a function doesn't have `return` statement
# `None` is returned. So every Python function returns something.


def none_function():
    """Returns None"""
    return


assert none_function() is None


def pass_function():
    pass  # special statement for empty blocks


assert pass_function() is None

# Multiple comma separated values after `return` are packed into the `tuple`


def one_two_tuple():
    """Returns a tuple of unity and two"""
    return 1, 2


a, b = one_two_tuple()
assert (a == 1) and (b == 2)
assert (1, 2) == one_two_tuple()
assert isinstance(one_two_tuple(), tuple)
# Use built-in function `isinstance()` to check if an object is an instance of
# some class. `isinstance()` is recommended way by PEP 8, do **not** use more
# complicated expressions like `type(one_two_tuple()) is tuple`


# # Arguments

# As you have seen, every function definition includes `()` after function
# name. If the function doesn't have any arguments, then these brackets are
# empty. Otherwise, brackets contain a list of arguments, which names are
# used as variable names inside the function.

# ## Positional arguments

# Arguments specified as a sequence of various variable names are named
# positional ones.


# Function with the only positional argument, it must by specified in call:


def plus_one(x):
    """Adds unity to any number"""
    return x + 1


x = 5
assert x + 1 == plus_one(x)


# Function with a pair of positional arguments, the order of arguments is
# significant:


def minus(x, y):
    """Returns a difference of two variables"""
    return x - y


x = 5
y = 3
assert x - y == minus(x, y)
# Do not be confused, `x` and `y` in the function and `x` and `y` above are
# different variables, the function has its local variables defined inside
# the round brackets:
assert y - x == minus(y, x)
# All positional arguments are required:
try:
    minus(x)
    assert False
except TypeError as e:
    assert str(e).startswith('minus()')


# ## Keyword arguments

# In Python, positional arguments of almost every function (see exceptions
# bellow) can be assigned by their names instead of assignment by position.
# In such a call these arguments can be called keyword arguments:

a, b = 2, 5
assert a - b == minus(x=a, y=b)
assert a - b == minus(y=b, x=a)

# Keyword arguments defined in function definition always have default value,
# often (not always, it is just useful in many cases) `None` is used as a such
# special default value. Examples are `dict.get(key, default=None)` or
# `sorted(iterable, key=None, reverse=False)` builtins.


def hello(name='Ira'):
    return '{} {}'.format('hello', name)


assert 'hello Ira' == hello()
assert 'hello Joe' == hello(name='Joe')

# Keyword argument can be called as positional one:
assert 'hello Julia' == hello('Julia')

# Import a simple function from neighbour module, we will learn more about
# import and modules later:
if __package__:
    from .utils import parallelogram_volume
else:
    from utils import parallelogram_volume
# See `parallelogram_volume` for an example of combining of positional and
# keyword arguments in function definition.

a, b, c = 1, 2, 3
assert a == parallelogram_volume(a)
assert a * b == parallelogram_volume(a=a, b=b)
assert a * b == parallelogram_volume(b=b, a=a)
assert a * b * c == parallelogram_volume(a, b, c)
assert a * b * c == parallelogram_volume(a, b, c=c)
# Remember that keyword arguments both in function definition and in function
# call must go after positional arguments. This is a **wrong** syntax:
# >>> parallelogram_volume(b=b, a)


# ### Default arguments

# You should never use mutable value as a default. The reason is
# straightforward: functions in Python are objects and their default values are
# just regular objects that are hold in the special function attribute
# `.__defaults__`.
assert parallelogram_volume.__defaults__ == (1, 1)

# When a function needs to use default value for its keyword argument it looks
# to this variable and takes (not copy) the value from it. So, if the default
# is mutable then it can be changed by function itself or returned to user and
# changed by her. This is an example of such behaviour:


def do_not_use_mutable_defaults(x=[]):
    x.append(1)
    return x


assert do_not_use_mutable_defaults() == [1]
assert do_not_use_mutable_defaults() == [1, 1]
assert do_not_use_mutable_defaults() == [1, 1, 1]
a = do_not_use_mutable_defaults()
assert a == [1, 1, 1, 1]
a[-1] = 500
assert do_not_use_mutable_defaults() == [1, 1, 1, 500, 1]

# If you really want this behaviour you should make it explicit. For example,
# write class with varying attribute (instead of varying default of keyword
# argument), implement `.__call__()` method (then an object of your class can
# be called as a function using operator `()`) and create an instance of your
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
a = callable_with_memory([3, 4, 5])
a[-1][-1] = -100  # object attribute hasn't changed!
assert callable_with_memory('hello') == [1, 2, [3, 4, 5], 'hello']


# ## Positional-only arguments

# In pure Python you cannot write a function with positional arguments and deny
# user to call it using keyword argument syntax. It is useless to force user to
# use positional arguments, because keyword arguments can improve readability
# of her code. But, for performance reasons, some of built-in CPython 3
# functions have special signatures that indicate some of arguments to be
# positional-only. Remember, that in interactive shell, you can see function
# signature using built-in `help()` function or typing `?` before object name
# in IPython. The basic example is `abs`:

assert 1 == abs(-1)
# Import standard library function `inspect.signature` that returns an object
# signature familiar to the first line of `help()` output:
if sys.version_info[0] >= 3:
    from inspect import signature
    assert '(x, /)' in str(signature(abs))
try:
    abs(x=-1)
except TypeError as e:
    assert str(e) == 'abs() takes no keyword arguments'
# Symbol `/` in a signature indicates that all arguments before it are
# positional-only.

# More complex example is `pow`:
assert 2**3 == pow(2, 3)
assert 2**3 % 5 == pow(2, 3, 5)
if sys.version_info[0] >= 3:
    assert '(x, y, z=None, /)' in str(signature(pow))
try:
    pow(2, 3, z=5)
except TypeError as e:
    assert str(e) == 'pow() takes no keyword arguments'
# So here `z` is positional but _optional_ argument. In Python, usually
# positional arguments are mandatory and keyword arguments are optional, but
# not in this case.


# ## Keyword-only arguments

# In Python 3 you can specify keyword-only arguments. This is useful when you
# would like to ovoid user to
if sys.version_info[0] >= 3:
    if __package__:
        from .functions_keyword_only import keyword_only, pos_and_keyword_only
    else:
        from functions_keyword_only import keyword_only, pos_and_keyword_only

    assert keyword_only(key=True)
    try:
        keyword_only(False)
    except TypeError as e:
        assert str(e).endswith('takes 0 positional arguments but 1 was given')

    assert pos_and_keyword_only(5, minimum=1, maximum=10)
    assert not pos_and_keyword_only(minimum=1, value=-3, maximum=10)


# Built-in functions also can have keyword-only arguments:
if sys.version_info[0] >= 3:
    assert ('(iterable, /, *, key=None, reverse=False)'
            in str(signature(sorted)))
    try:
        sorted([-5, -3, 0, 7], abs, True)  # sort by absolute value
    except TypeError as e:
        assert (str(e) == 'sorted expected 1 arguments, got 3'
                or str(e) == 'must use keyword argument for key function')


# ## Argument packing and unpacking

# A lot of these examples are Python 3 specific so they are located in separate
# module.
if sys.version_info[0] >= 3:
    if __package__:
        from .functions_packing_unpacking import packing, unpacking
    else:
        from functions_packing_unpacking import packing, unpacking
    packing()
    unpacking()


# # `lambda` statement

# Python has a special syntax for so called
# [anonymous functions](https://en.wikipedia.org/wiki/Anonymous_function).
# Anonymous functions are useful when you would like to write one-line function
# in place instead of writing separate `def`-block.
# We will use `reduce()` function from `functools` standard library module (in
# Python 2 `reduce()` is built-in function) as an example. This function takes
# three positional arguments: a function of two variables, iterable and an
# initial value (optional). The function of two variable will take a pair of
# currently reduced variable (at the first step it is the first value of the
# iterable or initial value if specified) and the next value of the iterable
# and produce new current reduced value.


def sum_of_squares(x, y):
    return x + y**2


assert reduce(sum_of_squares, range(5), 0) == 30
# And an example with anonymous function produced by `lambda` statement:
assert reduce(lambda x, y: x + y**2, range(5), 0) == 30
# So the syntax of `lambda` statement is as follows:
# >>> lambda [arg, arg, ...]: one-line expression which result is returned

# An object produced by `lambda` is similar to a one produced by `def`.
# However, it isn't recommended by PEP 8 to assign this object to some
# variable and use it after, because errors produced by anonymous functions
# are more difficult to debug.


# # Examples

# ## Bisection

# Avoid to implement such algorithms yourself! You should prefer to use
# implementations prepared by community (`bisect` module of standard library,
# `scipy.optimization` module
# https://docs.scipy.org/doc/scipy/reference/tutorial/optimize.html). This is
# a training example.

# TODO: write something
