#!/usr/bin/env python3
# Usually module files shouldn't be called directly, but this one can acts as
# script so we keep it executable.

from __future__ import division, print_function, unicode_literals

# Every *.py is a module. You can import it from any python script in the same
# directory or from interpreter started in the directory.

# When module is imported it is executed.
# So uou will see this message on import:
print('File {} is executed'.format(__file__))

# Module imports only one time, other imports will only change current globals.
# See importlib from standard library for various import tools:
# https://docs.python.org/3/library/importlib.html

# Let's introduce some variables and functions.

default_name = 'Anonymous'


def hello(name=default_name):
    return 'Hello {}'.format(name)


def goodbye(name=default_name):
    return 'Goodbye {}'.format(name)


# Now we want to make some actions when the files used as executable script.
# How to understand that the file isn't imported? When module is imported some
# special attributes are set. One of them is `__name__`. It sets to the file
# name without .py extension. But when file is executed `__name__` has special
# value "__main__".

if __name__ == '__main__':  # False when module is imported
    # We can import in any place
    from sys import argv
    from time import sleep

    if len(argv) > 1:
        name = argv[1]
    else:
        name = default_name

    print(hello(name=name))
    sleep(1)
    print(goodbye(name=name))

# Variables (attributes, functions, classes ...) that are loaded by
# "from ... import *" can be specified by special `__all__` variable:
__all__ = ('hello', 'default_name')  # She said goodbye, I said hello
