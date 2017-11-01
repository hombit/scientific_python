#!/usr/bin/env python3

from setuptools import find_packages, setup

with open('requirements.txt') as f:
    reqs = f.read().splitlines()

setup(
    name='scientific_python',
    version='0.0.1',
    url='https://xray.sai.msu.ru/~malanchev/',
    license='MIT',
    author='Konstantin Malanchev',
    author_email='malanchev@physics.msu.ru',
    description='Package with materials for Scientific Python course for astronomers in Moscow University',
    packages=find_packages(),
    scripts=['bin/sci_py_example', 'bin/sci_py_import_all'],
    package_data={
        'scientific_python': ['misc', 'doc'],
    },
#     test_suite='scientific_python.test.suite',
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
