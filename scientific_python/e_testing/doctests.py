#!/usr/bin/env python3

# Try to start this module by `python3 doctests.py -v` to see verbose
# information about testing.

"""This is a module docstring. It should be first significant expression in the
module.

Docstrings (PEP 257) support special type of tests - doctests:
https://docs.python.org/3/library/doctest.html

Remember that docstrings can be used to produce beautiful HTML documentation,
for example compare help(numpy.array) and
https://docs.scipy.org/doc/numpy/reference/generated/numpy.array.html

Doctests are used to write examples and provide some simple tests. You
shouldn't use it to write a lot of various unit tests but to write some simple
regression tests.

Each doctest expression to be executed with `>>>`, `...` is used for indented
lines, lines that aren't started with these symbols are interpreted as desired
output of previous command.

>>> print('Hello!')
Hello!
>>> for i in range(3):
...     print(i)
0
1
2

Empty line returns us to normal docstring.
>>> print('{:.5f}'.format(sqrt_sin(1)))
0.91732

Special option flags inside comments help doctest to work correctly.
For example +ELLIPSIS allows usage of `...` to skip sub-string:
>>> print(list(range(100)))  # doctest: +ELLIPSIS
[0, 1, ..., 98, 99]

We can test any output, even exceptions
>>> 1.0/0.0  # doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
ZeroDivisionError: division by zero

You can combine several option flags:
>>> print(list(range(100)))  # doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
[0,  1,    2, ...,  98, 99]
"""


from __future__ import division, print_function, unicode_literals


import math


def sqrt_sin(x):
    """Returns square root from sinus

    Examples
    --------
    Zero input produces zero output:
    >>> print(sqrt_sin(0))
    0.0

    Some mystical values produces errors:
    >>> print(sqrt_sin(-1))  # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
    ValueError: math domain error
    """
    return math.sqrt(math.sin(x))


# This function can be used in `setup.py` as `test_suite` keyword argument
def test_suite():
    import doctest
    suite = doctest.DocTestSuite(__name__)
    return suite


if __name__ == '__main__':  # checks if this file is executed as script
    import doctest
    doctest.testmod(raise_on_error=True)
