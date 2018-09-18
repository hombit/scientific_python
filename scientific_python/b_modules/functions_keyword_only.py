#!/usr/bin/env python3


def keyword_only(*, key=None):
    """Does key open the lock"""
    return key is True


def pos_and_keyword_only(value, *, minimum=-1, maximum=1):
    """If value is between minimum and maximum"""
    return minimum <= value <= maximum
