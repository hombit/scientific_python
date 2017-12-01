# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 22:13:56 2017

@author: Friend
"""
"""
Как реализовать сосуществование конфликтующих опциональных аргументов,
которые выполняют противоположные действия
"""
import argparse

parser = argparse.ArgumentParser(description="calculate X to the power of Y")
#Создаём группу опциональных аргументов с помощью ещё одного метода 
#класса ArgumentParser. В ней возможно хранить опциональные аргументы,
#выполняющие противоположные действия
group = parser.add_mutually_exclusive_group()
#action="store_true" означает, что при указании данного опционального аргумента
#при вызове ему будет присвоено значение True.
#Если его не указать, то будет по умолчанию значение None
group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-q", "--quiet", action="store_true")
parser.add_argument("x", type=int, help="the base")
parser.add_argument("y", type=int, help="the exponent")
args = parser.parse_args()
answer = args.x**args.y

if args.quiet:
    print(answer)
elif args.verbose:
    print("{} to the power of {} equals {}".format(args.x, args.y, answer))
else:
    print("{}^{} = {}".format(args.x, args.y, answer))
    
"""
Для демонстрации - запустить
python Powconfl.py 5 7
python Powconfl.py 5 7 -q
python Powconfl.py 5 7 -v
python Powconfl.py 5 7-qv
python Powconfl.py 5 7 -h
"""