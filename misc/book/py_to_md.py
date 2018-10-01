# -*- coding: utf-8 -*-
"""
Created on Fri Sep  28 20:01:12 2018

@author: aleksandra
"""

import argparse
from converter import convert

parser = argparse.ArgumentParser()
parser.add_argument('filenames', help='''List of a python scripts names you
                    want to convert to Markdown. Example:
                    first_file.py second_file.py''', type=str, nargs='+')
filenames = parser.parse_args().filenames

for name in filenames:
    try:
        convert(name)
    except Exception:
        print('{} was not converted'.format(name))

