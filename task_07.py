#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Separating key, value pairs."""

DATA = {
    3: 1,
    5: 5,
    13: 4,
    18: 6,
    24: 8,
    30: 9,
    36: 11,
    42: 12,
    48: 14,
    54: 15,
    60: 17,
    66: 18,
    72: 20,
    78: 21,
    84: 23,
}


def iter_dict_funky_sum(funkydict):
    """Returns a funky total.

    Args:
        funkydict (dict): Set of integer pairs.

    Returns:
        integer: The funky total.

    Examples:
        >>>iter_dict_funky_sum(DATA)
        -449

        >>>iter_dict_funky_sum({3: 1, 10: 5, 13: 4,})
        -16
    """
    ftotal = 0
    for key, value in funkydict.iteritems():
        ftotal = ftotal + (value - key)
    return ftotal
