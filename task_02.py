#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This is the week 10 warmup task 2 that references a dictionary."""

from data import BANDS

MEMBER = 'Nigel Tufnel'

NIGEL = [BANDS[bkey][MEMBER] for bkey in BANDS if MEMBER in BANDS[bkey]][0]

BAND_NAMES = BANDS.keys()
