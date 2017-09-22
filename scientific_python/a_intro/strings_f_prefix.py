#!/usr/bin/env python3

# Requires Python 3.6 so no "import from __future__" statement

# "f" prefix works just like str.format() but with indicating of variable name

x = 1
name = 'x'

def f_prefix():
    s1 = '%s = %d' % ('x', x)
    s2 = '{} = {}'.format('x', x)
    s3 = f'{name} = {x}'
    s4 = f'{name:s} = {x:d}'
    assert s1 == s2 == s3 == s4
