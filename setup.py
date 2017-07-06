#!/usr/bin/env python3

from __future__ import division, print_function, unicode_literals

from setuptools import setup
# from pip.req import parse_requirements


setup(
    name='scientific_python',
    version='0.0.0',
    url='https://xray.sai.msu.ru/~malanchev/',
    license='MIT',
    author='Konstantin Malanchev',
    author_email='malanchev@physics.msu.ru',
    description='Package with materials for Scientific Python course for astronomers in Moscow University',
    packages=['scientific_python'],
#     install_reqs=parse_requirements('requirements.txt', session='hack'),
#     scripts=['bin/script'],
#     test_suite='scientific_python_sai.test.suite',
    classifiers=[
        'Intended Audience :: Education',
        'License :: OSI Approved :: MIT License',
        'Topic :: Education',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='sample education',
)
