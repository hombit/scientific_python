#!/usr/bin/env python3

# No __future__ imports, this is Python 3 only code

if __package__:
    from .utils import parallelogram_volume
else:
    from utils import parallelogram_volume

## Argument packing ##

def packing():
# "*" symbol before argument name (usually it is named args) means that
# function takes any number of positional arguments and all of them are packed
# into one tuple.
    def packed_args(*args):
        return args
    assert packed_args(1) == (1,)
    assert isinstance(packed_args(1), tuple)
    assert len(packed_args(1)) == 1
    assert packed_args() == tuple()
    assert isinstance(packed_args(1, 2, 3), tuple)
    assert len(packed_args(1, 2, 3)) == 3
    assert (1, 2, 3) == packed_args(1, 2, 3)

# "**" before argument name (usually it is named kwargs - keyword arguments)
# means that function takes any number of keyword arguments and all of them are
# packed into one dict.
    def packed_kwargs(**kwargs):
        return kwargs
    x = packed_kwargs(key='value', one=1)
    assert isinstance(x, dict)
    assert len(x) == 2
    assert ('key' in x) and ('one' in x)
    assert ('value' in x.values()) and (1 in x.values())
    try:
        packed_kwargs('hello')
        assert False
    except TypeError as e:
        assert str(e) == "packed_kwargs() takes 0 positional arguments but 1 was given"

# And all together now!
    def packed_args_kwargs(*args, **kwargs):
        return len(args), len(kwargs)
    assert packed_args_kwargs(1, 2, 3, four=4, five=5) == (3, 2)

    def packed_and_non_packed(x, *args, key=None, **kwargs):
        return len(args), len(kwargs)
    assert packed_and_non_packed(1) == (0, 0)
    assert packed_and_non_packed(1, 2, 3, four=4, five=5) == (2, 2)
    assert packed_and_non_packed(1, 2, 3, four=4, five=5, key='value') == (2, 2)

## Arguments unpacking ##

def unpacking():
# In the same way positional and keyword arguments can be passed in as a parts
# of iterable ordered variables and unpacked them inside the function.
    a, b, c = 2, 3, 4
    l = [a, b, c]
    t = (a, b, c)
    d = {'a': a, 'b': b, 'c': c}
    volume = a * b * c
    assert volume ==  parallelogram_volume(*l)
    assert volume ==  parallelogram_volume(*t)
    assert volume ==  parallelogram_volume(**d)
    assert volume ==  parallelogram_volume(a, *(b, c))
    assert volume ==  parallelogram_volume(a, **{'b': b, 'c': c})
    assert volume ==  parallelogram_volume(*[a], c=c, **{'b': b})
    assert volume ==  parallelogram_volume(a, *[b], c=c)


__all__ = ('packing', 'unpacking')
