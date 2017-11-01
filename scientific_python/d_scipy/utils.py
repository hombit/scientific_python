#!/usr/bin/env python3

from __future__ import division

import numpy as np

def ssd(a, b):
    """Sum of square differences of two arrays"""
    return np.sum(np.square(a-b))

