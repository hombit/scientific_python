# coding: utf-8
from __future__ import unicode_literals
s = 'abcd1213-=*&^тавдыжжфщушм'
s
s[0]
s[-1]
s[5:10]
'abc' + 'def'
str(1)
str([1, 2, 3, 'hello', (5, 6, 7), {'d', 'e', 'd'}])
s[0] = 'r'
del s[]0
del s[0]
b'abc'
type(b'abc')
b = b'abc'
b + 'abc'
b + b'abc'
b.decode()
get_ipython().run_line_magic('pinfo', 'b.decode')
s
get_ipython().run_line_magic('pinfo', 's.encode')
s.encode()
s = 'Hello'
s2 = "Hello"
s == s2
s
s2
s = 'Hello "World"'
s
s = "Hello 'World'"
s
s = '\''
s
'\'"'
'\'\"'
s = 
s = 'Hello\nWorld'
s
print(s)
s = """Hello world"""
s = '''Hellow world'''
s
s = "Hello
s = """Hello
world
"""
s
print(s)
s.__doc__
sorted.__doc__
R''
s = r'\n'
print(s)
r'\n' != 
r'\n' != '\n'
type(r'\n')
'\\n' == r'\n'
x = 10
print('x =', x)
'x = ' + str(x)
'x = {}'.format(x)
'x = {} {}'.format(x, x**2)
'x = {1} {0} {1}'.format(x, x**2)
'x = {1:f} {0} {1}'.format(x, x**2)
'x = {1:f} {0} {1}'.format(x, 3.1415)
'x = {1:f} {0} {1} {{}}'.format(x, 3.1415)
'x = {1:f} {0} {key} {{}}'.format(x, 3.1415, key='default')
'x = {1:f} {0} {key} {{}}'.format(x, 3.1415)
'x = {1:f} {0} {key} {{}}'.format(x, 3.1415, key='default')
'x = {x}, pi = {pi:f}, l = {length}'.format(x=x, pi=3.14, length=2*3.14*x)
'x = {x}, pi = {pi:f}, l = {length:.2f}'.format(x=x, pi=3.14, length=2*3.14*x)
'pyformat.info'
f'x = {x}'
def unity():
    x = 1
    return x
one = unity()
print(one)
f = unity
f is unity
unity.__class__
a = [unity, 1, 2, 3]
a
def unity():
    """Returns one"""
    return 1
get_ipython().run_line_magic('pinfo', 'unity')
unity.__doc__
def unity():
    """Returns one
    
    This function ...
    is very fine
    """
    return 1
get_ipython().run_line_magic('pinfo', 'unity')
unity.__doc__
def none_function():
    return
none_function() is None
def hello_name(name):
    print('hello {}'.format(name))
    
hello_name('Masha')
hello_name('Vasya')
result = hello_name('Vasya')
result is None
def minus(x, y):
    return x - y
x = 5
y = 3
minus(x, y)
minus(y, x)
minus(x=x, y=y)
get_ipython().run_line_magic('pinfo', 'minus')
minus(x=10, y=33)
minus(y=33, x=10)
get_ipython().run_line_magic('pinfo', 'sorted')
get_ipython().run_line_magic('pinfo', 'pow')
pow(2, 3, 4)
pow(2, 3)
pow(x=2, y=3)
pow(2, 3, z=4)
def hello_user(user='%username%'):
    return 'hello {}'.format(user)
hello_user()
hello_user(user='Masha')
hello_user('Masha')
minus()
minus(x=1, 2)
def check_between(value, minimum=-1, maximum=1):
    return minumum <= value <= maximum
check_between(10)
def check_between(value, minimum=-1, maximum=1):
    return minimum <= value <= maximum
check_between(10)
check_between(10, minimum=-100, maximum=500)
check_between(10, -100, 500)
def check_between(value, *, minimum=-1, maximum=1):
    return minimum <= value <= maximum
def check_between(value=0, *, minimum=-1, maximum=1):
    return minimum <= value <= maximum
check_between()
check_between(0.5)
check_between(value=0.5)
check_between(0.5, -1, 1)
check_between(0.5, minimum=-10, maximum=100)
get_ipython().run_line_magic('pinfo', 'sorted')
check_between(maximum=100, value=0, minimum=33)
def f(a=1):
    pass
f()
f.__defaults__
f.__defaults__[0]
import inspect
def f(a=[1]):
    pass
f.__defaults__
def f(a=[1]):
    a.append(a[-1] + 1)
    
def f(a=[1]):
    a.append(a[-1] + 1)
    return a
f()
f()
f()
f()
f().append(-100)
f()
class FunctionWithMemory:
    __used_arguments = []
    
class FunctionWithMemory:
    __used_arguments = []
    
class FunctionWithMemory:
    __used_arguments = []
    def __call__(self, arg):
        import copy
        
        self.__used_arguments.append(arg)
        return copy.deepcopy(self.__used_arguments)
    
f = FunctionWithMemory()
f()
f(1)
f(3.14)
f(5.5)
def pair():
    return 1, 2
pair()
type(pair())
def pair():
    return 1,
pair()
def pair():
    return (1 + 3)
pair()
def pair():
    return 1, 2, 3
pair()
x, y, z = pair()
def f(a, b, c, x='x', y='y', z='z'):
    pass
f(1, 2, 3, y=100, z=500)
t = (1, 2, 3)
def f(a, b, c, x='x', y='y', z='z'):
    print(a, b, c, x, y, z)
    
f(t[0], t[1], t[2])
f(*t)
f(*[1, 2, 3])
d = {x: 1, y: 2, z: 3}
f(*t, **d)
d = {'x': 1, 'y': 2, 'z': 3}
f(*t, **d)
d = {'x': -100}
f(*t, **d)
f(*[1, 2, 3, 4])
f(**{'a': -1, 'b': -2, 'c': -3, 'x': 100})
def f(*args):
    print(args)
    
f(1, 2, 3, 4, 5)
def f(x, *args):
    print(x)
    print(args)
    
f('x', 1, 2, 3,)
f('x')
def f(**kwargs):
    print(kwargs)
    
f(a=1, b=2)
f(*args, **kwargs):
def f(*args, **kwargs):
    kwargs['x'] = 50
    f1(*args, **kwargs)
    
def f(x, *args, key='key', **kwargs):
    kwargs['x'] = 50
    f1(*args, **kwargs)
    
get_ipython().run_line_magic('pinfo', 'str.format')
s = '{}'
s
s.format(3.14)
sum(range(10))
def value_at_zero(f):
    return f(0)
value_at_zero(abs)
import math
value_at_zero(math.cos)
def f(x):
    return x**2 + 1
value_at_zero(f)
value_at_zero(lambda x: x**2 + 1)
from scipy.optimize import root
get_ipython().run_line_magic('pinfo', 'root')
root(lambda: 2*x + 1, 0.)
root(lambda x: 2*x + 1, 0.)
root(lambda x: 2*x + 1, 0.)
root(math.cos, 0.5)
root(lambda x: math.cos(2*x), 0.5)
root(lambda x: math.pow(3.14, x) - 5, 0.)
from functools import partial
