# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import doctest
import unittest

import ser


class NameTestCase(unittest.TestCase):
    def test(self):
        name = 'serpens'
        self.assertEqual(ser.name, name,
                         msg='name should be {}'.format(name))


class IsSnakeTestCase(unittest.TestCase):
    def test_eng(self):
        self.assertTrue(ser.is_snake('python'),
                        msg='"python" should be identified as a snake')

    def test_ru(self):
        self.assertTrue(ser.is_snake('питон'),
                        msg='"питон" is a Russian name for python')

    def test_upper_case(self):
        self.assertTrue(ser.is_snake('Python'),
                        msg='Titled "Python" doesn\'t identified')

    def test_dog(self):
        self.assertFalse(ser.is_snake('dog'),
                         msg='"dog" shouldn\'t be identified as a snake')

    def test_string_with_spaces(self):
        msg = 'String with spaces should cause exception'
        with self.assertRaises(ValueError, msg=msg):
            ser.is_snake('Python is a snake')


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(ser.snake))
    return tests
