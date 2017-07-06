# This is a code for the first lesson. You can execute it by typing
# $ python intro.py
# Or if your prefer python3 (and you should prefer it)
# $ python3 intro.py

# As you see "#" is used for comments.


### Print ###

## Python 2 and 3 ##

# Unfortunately today there are two incompatible branches of Python language:
# version 2.7 and versions 3.*. The very first thing you find is print
# statement. In Python 2 print is literally a statement and should be used
# without parentheses:
# >>> print 1
# will print '1'. Nowadays you should use Python 3 where print is a function
# (for now just believe it has a reason to be so):
# >>> print(1)
# will print '1'. If you must use Python 2 or you write a library that should
# work on both 2 and 3 than you can use this "magic" line with __future__
# statement:

from __future__ import print_function, devision

# We will describe import system later. This line has no effect in Python 3 but
# in Python 2 it sets behaviour of print statement to the same as in Python 3.
# This line should be the first meaningful line in your file.

# Now we can really print something:
print(1)  # Will print '1' without quotes

# Let's test simple arithmetic operations:
print(1 + 2)
# >>> 3
print(3 - 4)
# >>> -1
print(3 * (-5))
# >>> -15
print(2 ** 10)
# >>> 1024


### Numbers ###

## Integers ##

# Python supports long integers
print(1024 ** 128)
# >>> 20815864389328798163850480654728171077230524494533409610638224700807216119346720596024478883464648369684843227908562015582767132496646929816279813211354641525848259018778440691546366699323167100945918841095379622423387354295096957733925002768876520583464697770622321657076833170056511209332449663781837603694136444406281042053396870977465916057756101739472373801429441421111406337458176

## Floats ##

# There is built-in floating numbers (float for short):
print(1.23)
# >>> 1.23
print(1e-3)
# >>> 0.001
# Floats unlike integers have limits.
print(1e200 * 1e200)
# >>> inf

## Division ##

# Division (operator "/") works different in Python 2 and 3. In Python 2
# division of two integers is always integer but in Python 3 it is always
# float. "Magic" statement "from __future__ import division" above works in the
# very same way as for print function described earlier and asks Python 2 to
# work as Python 3. Use it always if your code can run with Python 2
# interpretor.

# Let's look how division works
print(1 / 2)
# >> 0.5
print(4 / 2)
# >> 2.0
print(1.5 / 0.5)
# >> 3.0

# Operator "//" returns integer rounded to smaller value. It returns integer
# typed value for a pair of integers and float typed value if at least one of
# the value is float:
print(1 // 2)
# >> 0
print(4.0 // 2)
# >> 2.0
print(1.5 // 0.5)
# >> 3.0

## Complex numbers ##

# Python has a float complex type:
print(2 + 3j)
# >>> (2+3j)
# Where j is the imaginary unit modifier


### Variables and basic types ###

## Dynamic type checking ##

# Python is dynamic type checking language that means you don't need to declare
# variable before assignment. Also you can change type of variable after the
# first assignment
a = 10
print(a)
# >>> 10
a = 10.0
print(a)
# >>> 10.0

## Type conversions ##

# You can convert variable from one type to another
a = 7
b = complex(7)
print(b)
# >>> (7+0j)
a = 13.2
b = int(a)
print(b)
# >>> 13

## Attributes and methods ##

# Python is an object oriented language and each variable is represented by an
# object of some type (class). We will describe how to create our own classes
# later. Now the only thing that we should now that classes and therefore
# objects have attributes and methods (functions). Syntax of attribute access is
# the same as in a lot of other languages via "." separator.
a = (-1)**(-0.5)
print(a.imag)
# >>> -1.0
print(a.conjugate().imag)
# >>> 1.0

## Type of the variable ##

# Built-in function "type" returns object type
print(type(1))
# >>> <class 'int'>
# Full list of built-in functions can be found on
# https://docs.python.org/library/functions.html


