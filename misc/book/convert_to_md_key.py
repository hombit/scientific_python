# -*- coding: utf-8 -*-
"""
Created on Fri Sep  28 20:01:12 2018

@author: aleksandra
"""
import argparse
from convert_to_md_function import convert

parser = argparse.ArgumentParser()
parser.add_argument('file_name', help = 'Name of a python script you want to convert to Markdown. Example: my_file.py', type=str)
file_name = parser.parse_args().file_name

convert(file_name)
