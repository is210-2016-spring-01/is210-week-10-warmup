#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 07 Module"""

DATA = {
    42: 43257,
    85: 23563,
    23: 45325,
    98: 12345,
    24: 23546,
    49: 23506,
    30: 63592,
    80: 24964,
    15: 25046,
    86: 24503,
    58: 24345
}


def iter_dict_funky_sum(dictarg):
    """Calculates a running total of the sum of the values minus the key.

    Args:
        dictarg (dictionary): Dictionary data containing key and value integers

    Returns:
        total: running total of the sum of the values minus the key

    Examples:
        >>> iter_dict_funky_sum(DATA)
        333402
    """
    total = 0

    for key, val in dictarg.iteritems():
        total += val - key

    return total
