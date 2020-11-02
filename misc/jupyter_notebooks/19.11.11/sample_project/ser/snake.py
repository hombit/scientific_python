# -*- coding: utf-8 -*-

from __future__ import unicode_literals


__all__ = ('is_snake',)


def is_snake(word):
    """Checks if an animal is a snake

    Parameters
    ----------
    word : str
        Animal name

    Returns
    -------
    bool

    Example
    -------
    Check if a bear is a snake

    >>> from ser.snake import is_snake
    >>>
    >>> if is_snake('bear'):
    ...     print('Shhhh')
    ... else:
    ...     print('Argh')
    Argh

    """
    if not word.isalpha():
        raise ValueError("String '{}' is not a word")
    if word.lower() == 'python':
        return True
    if word.lower() == 'питон':
        return True
    return False


def _parse_args(args=None):
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(description='Check if animal is snake')
    parser.add_argument('word', help='an animal to check')
    namespace = parser.parse_args()
    return namespace


def main():
    """Entry-point for ser module"""
    word = _parse_args().word
    if is_snake(word):
        print('{} is a snake'.format(word))
        return
    print('{} is not a snake'.format(word))


def plot():
    """Plot a snake"""
    import math
    import matplotlib.pyplot as plt

    x = [i / 10 for i in range(100)]
    plt.plot(x, [math.sin(a) for a in x])
    plt.show()
    plt.close()
