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
# `Exception` (or its inheritor, see below). Such an object can be get using
# `except ... as` syntax:
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
        assert str(e) == 'not enough values to unpack (expected 2, got 1)'
    except TypeError as e:
        count_type_errors += 1
        assert str(e) == 'can only concatenate str (not "int") to str'
assert count_value_errors == 1
assert count_type_errors == 1

# ## Exception inheritance hierarchy
