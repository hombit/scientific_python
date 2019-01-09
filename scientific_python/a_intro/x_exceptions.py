#!/usr/bin/env python3

from __future__ import print_function


# # Catch exceptions

# An exception is an error that throws from some point of the code. You can
# catch exception in `try`-`except` block:
try:
    1 / 0
except ZeroDivisionError:
    print('ZeroDivisionError was caught')
# `ZeroDivisionError was caught`

# An exception is represented as a special object of built-in class
# `Exception` (or its inheritor, see details below). Such an object can be
# get using `except ... as` syntax:
try:
    1 + '0'
except TypeError as e:
    assert str(e).startswith('unsupported operand type(s) for +:')

# ## `assert`

# By the way, the only thing that `assert` does is throwing `AssertionError`
# exception:
try:
    assert False, 'Always fails'  # the second argument is an error message
except AssertionError as e:
    assert str(e) == 'Always fails'

# If exception isn't caught the entire Python program fails. That's why
# `assert` is used in the code examples of this book, the code is tested to
# not fail, so while reading you can always assume that statement after
# `assert` is true or `AssertionError` is caught as shown above.


# ## Catch exceptions of different types

# You can enumerate different exceptions in one `except` block

d = {'zero': 0}
exceptions = set()
for key in ['zero', 'unity']:
    try:
        d[key] = 1 / d[key]
    except (ZeroDivisionError, KeyError) as e:
        exceptions.add(type(e))
# Exceptions of both types were caught:
assert not exceptions.difference((ZeroDivisionError, KeyError))
# NB bool(set()) is False

# Multiple `except` blocks can be used if different behaviour should be
# implemented for different exceptions.

a = [[1], ['x', 3]]
count_value_errors = 0
count_type_errors = 0
for pair in a:
    try:
        x, y = pair  # ValueError if pair is not a two-element collection
        z = x + y  # TypeError if variables cannot be added
    except ValueError as e:
        count_value_errors += 1
    except TypeError as e:
        count_type_errors += 1
assert count_value_errors == 1
assert count_type_errors == 1

# ## Exception inheritance hierarchy

# As it was mentioned above all exception classes inherit `BaseException`
# built-in class. The main inheritor of this class is `Exception`, which is
# the base of almost all built-in exceptions and should be used to create
# user-defined exceptions. See the full hierarchy of built-in exceptions on
# https://docs.python.org/3/library/exceptions.html#exception-hierarchy

assert issubclass(Exception, BaseException)
assert issubclass(ValueError, Exception)

# Multiple `except` statements work like `if` with one or more `elif`
# statements: only first matched exception is used, not all of them.
# In the next example `LookupError` and its inheritors `IndexError` and
# `KeyError` will be used.

assert issubclass(IndexError, LookupError)

a = []
try:
    x = a[0]
except LookupError as e:
    count_lookup_error = 1
except IndexError as e:
    assert False  # we cannot be here
assert count_lookup_error == 1

try:
    x = a[0]
except KeyError as e:
    assert False  # not a KeyError
except IndexError as e:
    count_index_error = 1
except LookupError as e:
    assert False
assert count_index_error == 1

# ## Catch them all

# It could be desired to catch all types of exceptions at once. It is
# possible, but be aware to use it all the time.
