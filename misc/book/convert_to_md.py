# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 22:41:58 2018

@author: aleksandra
"""

file_name = 'name.py'

my_file = open(file_name, 'r')
my_code = my_file.readlines()
my_file.close()


text = ''
code = False
notprint = True

if my_code[0][:2] == '#!':
    my_code = my_code[1:]

for string in (my_code):
    notprint = True
    if string[:5] == '# >>>':
        text = text + '\n' + '    ' + string[:2] + string[5:]
        notprint = False
        continue
    if string[:3] == '# `' and string[-2] == '`':
        if code:
            text = text + '\n ``` \n _' + string[3:-2] + '_ \n\n'
        else:
            text = text + '_' + string[3:-2] + '_ \n\n'
        code = False
        notprint = False
        continue
    if string[0] == '#':
        if code and notprint:
            while text[-1] == '\n':
                text = text[:-1]
            text = text + '\n ``` \n'
            code = False
        text = text + string[1:]
        continue
    if string == '\n' or code:
        text = text + string
        continue
    text = text + '\n ```python \n' + string
    code = True
            
if code:
    text =  text + ' \n ``` \n'      
    
result_name = file_name[:-2] + 'md'    
md = open(result_name,'w')
md.write(text)
md.close()


    
    