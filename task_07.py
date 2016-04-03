#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A docstring that uses randon numbers to test the iteritems() function."""

DATA = {
    2: 25,
    25: 245,
    6: 771,
    95: 302,
    50: 190,
    65: 312,
    987: 25,
    605: 399,
    72: 419,
    394: 9
}


def iter_dict_funky_sum(mydata):
    """This function returns the sum of the numbers.

    Args:
    A dictionary: Keys and values that are integers. (required).

    Returns:
    returns a funky total.

    Example
    >>> import task_07
    >>> task_07.iter_dict_funky_sum(task_07.DATA)
    396
    """

    count = 0

    for key, value in mydata.iteritems():
        count = count + value - key
    return count
