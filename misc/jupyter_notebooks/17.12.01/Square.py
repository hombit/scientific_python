# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 18:01:59 2017

@author: Friend
"""

"""
Программа, выводящая квадрат числа, вводимого с клавиатуры
"""
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("square", 
                    help="number, which square is given",
                    type=int)   #Обязательно указывать тип вводимой переменной,
                                 #потому что по умолчанию он считает,
                                 #что этот тип - строка
args = parser.parse_args()
print(args.square**2)