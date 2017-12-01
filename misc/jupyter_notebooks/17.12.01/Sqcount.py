# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 21:58:38 2017

@author: Friend
"""
"""
Программа, вычисляющая квадрат числа.
Может выдавать сообщение с результатом 
разными способами по выбору.
Сообщение зависит не от ключа-цифры, а от
количества указаний опционального аргумента
"""
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("square", 
                    type=int,
                    help="display a square of a given number")
parser.add_argument("-v", "--verbosity",
                    #Работа программы определяется количеством указаний
                    #данного опционального аргумента
                    action="count", 
                    #Значение по умолчанию, будет присваиваться переменной
                    #verbosity, если его явно не указать при вызове
                    default=0,
                    help="increase output verbosity")
args = parser.parse_args()
answer = args.square**2
if args.verbosity >= 2:
    print("the square of {} equals {}".format(args.square, answer))
elif args.verbosity >= 1:
    print("{}^2 = {}".format(args.square, answer))
else:
    print(answer)
    
"""
Для демонстрации - запустить
python Sqcount.py 9 -v
python Sqcount.py 9 -vv
python Sqcount.py 9 -vvv
python Sqcount.py 9 - если не указали default=0, то выдаст ошибку, поскольку
                      операция сравнения не может быть перенесена на значение None
                      типа NoneType
"""