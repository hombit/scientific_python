# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 20:16:06 2017

@author: Friend
"""

"""
Программа, выводящая степень exp числа base.
exp - опциональный аргумент,
base - позиционный аргумент
Если не указан exp, то base по умолчанию возводится в квадрат
Уже с отформатированным описанием
"""
import argparse
#импортируем функцию, помогающую выдавать текст со всеми переносами строки
#Она содержится в модуле работы с текстами textwrap
from textwrap import dedent
parser = argparse.ArgumentParser(
        #Описание программы
        description=dedent('''
        Calculates base to the power of exp.
        If base isn\'t mentioned, calculates square of base'''),
        #Нужный форматирующий класс - контролирует выдачу текста в описании
        formatter_class=argparse.RawDescriptionHelpFormatter
        )
#Добавляем позиционный аргумент типа int - основание степени
parser.add_argument("base", help="base of power, mandatory", type=int)
#Добавляем опциональный аргумент типа int - показатель степени,
#допускаем возможность указывать как короткое, так и полное имя
#опционального аргумента
parser.add_argument("-e","--exp", help="exponent of power, optional", type=int)   
args = parser.parse_args()

if (args.exp!=None):
    b = args.base
    e = args.exp
    print(b**e)
else:
    b = args.base
    print(b**2)