#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 20:54:51 2017

@author: Friend
"""

"""
Программа, выводящая степень exp числа base.
exp - опциональный аргумент,
base - позиционный аргумент
Если не указан exp, то base по умолчанию возводится в квадрат
"""
import argparse

parser = argparse.ArgumentParser()
#Добавляем позиционный аргумент типа int - основание степени
parser.add_argument("base", help="base of power, mandatory", type=int)
#Добавляем опциональный аргумент типа int - показатель степени,
#допускаем возможность указывать как короткое, так и полное имя
#опционального аргумента
parser.add_argument("-e","--exp", help="exponent of power, optional", type=int)   
args = parser.parse_args()

if (args.exp is not None):
    b = args.base
    e = args.exp
    print(b**e)
else:
    b = args.base
    print(b**2)
    
"""
Для демонстрации - запустить
python Power.py 2 -e 6
python Power.py 2 --ex 5
python Power.py 7
"""