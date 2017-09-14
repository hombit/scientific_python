#!/usr/bin/env python3


### Strings ###

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


## str ##

# str is a built-in type representing a sequences of Unicode characters (bytes
# in Python 2).

