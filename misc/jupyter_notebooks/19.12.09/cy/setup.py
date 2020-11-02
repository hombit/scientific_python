#!/usr/bin/env python

import numpy as np
from Cython.Build import cythonize
from setuptools import setup, Extension


extensions = [
    Extension('cy_examples',
              ['autoreg.cpp', 'cy_examples.pyx'],
              extra_compile_args=['-std=c++11'],
              extra_link_args=['-std=c++11'],
              include_dirs=[np.get_include()],)
]

extensions = cythonize(extensions, annotate=True, force=True, language_level=3)


setup(
    name='cy_examples',
    ext_modules=extensions,
)