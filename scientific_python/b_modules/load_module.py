#!/usr/bin/env python3

from __future__ import division, print_function, unicode_literals

# If this file is used as stand-alone module or script its __package__ variable
# is `None` or empty string then import can be produced as usual. If the file is
# used as package module, then we should use relative import.

# Read simple_module.py first.
if __package__:
    from . import simple_module as sm
else:
    import simple_module as sm
# Print from simple_module is executed!
# First time import executes module, play with `import antigravity`.

# imports only hello and default_name as described by `__all__`
if __package__:
    from .simple_module import *
else:
    from simple_module import *
# Print isn't executed one more time.

if __package__:
    from .simple_module import goodbye as good_bye
else:
    from simple_module import goodbye as good_bye
# Print is silent again.

assert sm.hello(name='Joe') == 'Hello Joe'
assert good_bye(name='Mary') == 'Goodbye Mary'
assert default_name == 'Anonymous'

assert 'goodbye' not in sm.__all__
try:
    goodbye(name='Mike')
    assert False
except NameError as e:
    assert str(e) == "name 'goodbye' is not defined"
