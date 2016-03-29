#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This is the week 10 warmup task 7 that loops through a dictionary."""

DATA = {
    -200: 722474,
    -140: 47604800,
    -112: 333525,
    -60: 1251609,
    -42: 14142033,
    2: 326226,
    3: 4091979,
    4: 7493945,
    10: 1497448,
    21: 31331376,
    24: 8674458,
    45: 1137701,
    76: 9308640,
    165: 3629142,
    246: 1428844,
    268: 1293804,
    297: 965088,
    306: 24149568,
    360: 3649762,
    1332: 9275602,
    2848: 43613288,
    3368: 11716264,
    3552: 59270668,
    7000: 55040936,
    20600: 7087200,
    74336: 10559923
    }


def iter_dict_funky_sum(sumdict):
    """ Loops through the passed dictionary of numbers and geneates a sum of
        the values less the key

    ARGS:
        sumdict (dictionary): Dictionary with interger key and value

    RETURNS:
        interger: The total of all values less the keys

    EXAMPLE:
        >>> iter_dict_funky_sum(DATA)
        359481994
    """

    dsum = 0

    for dkey, dvalue in sumdict.iteritems():

        dsum += dvalue - dkey

    return dsum
