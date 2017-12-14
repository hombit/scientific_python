#!/usr/bin/env python3

# Read packaging and distributing tutorial:
# https://packaging.python.org/tutorials/distributing-packages/

from setuptools import find_packages, setup, Extension
import os
import glob

packagename='scientific_python'

# Cython related
try:
    from Cython.Build import cythonize
    import numpy as np
    ext_modules = cythonize([
        Extension(
            'scientific_python.f_speed.cy_contfrac',
            ['src/cy_contfrac.pyx'],
            include_dirs=[np.get_include()]),
        Extension(
            'scientific_python.f_speed.erf',
            ['src/erf.pyx'],
            include_dirs=[np.get_include()]),
    ])
except ImportError:
    ext_modules = []

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'requirements.txt')) as f:
    install_requires=f.read().splitlines()

setup(
    name=packagename,
    version='0.2.0',
    url='http://homb.it/sci_py/',
    license='MIT',
    author='Konstantin Malanchev',
    author_email='malanchev@physics.msu.ru',
    description='Package with materials for Scientific Python course for astronomers in Moscow University',
    packages=find_packages(),
    # If you have only one Python module use `py_modules` instead of `packages`:
    # py_module = ['mymodule'],
    scripts=['bin/sci_py_example', 'bin/sci_py_import_all'],
    ext_modules=ext_modules,
    data_files=[
        ('doc',  ['doc/course_abstract.docx']),
    ],
    install_requires=install_requires,
    test_suite='scientific_python.e_testing.test_suite',
    classifiers=[
        'Intended Audience :: Education',
        'License :: OSI Approved :: MIT License',
        'Topic :: Education',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='sample education',
)
