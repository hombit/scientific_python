#!/usr/bin/env python3

from __future__ import division, print_function, unicode_literals

# Read simple_module.py first.

import simple_module as sm
# Print from simple_module is executed!
# First time import executes module, play with "import antigravity".

# imports only hello and default_name as described by `__all__`
from simple_module import * 
# Print isn't executed one more time.

from simple_module import goodbye as good_bye
# Print is silent again.

assert sm.hello(name='Joe') == 'Hello Joe'
assert good_bye(name='Mary') == 'Goodbye Mary'
assert default_name == 'Anonymous'
try:
    goodbye(name='Mike')
    assert False
except NameError as e:
    assert str(e) == "name 'goodbye' is not defined"
    
