#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This is the week 10 warmup task 2 that references a dictionary."""

import data

CORRECTED = data.BANDS.copy()

CORRECTED['Dylan'] = {}
CORRECTED['Dylan']['Bob Dylan'] = ['vocals', 'guitar', 'harmonica']

del CORRECTED['Van Halen']['David Lee Roth']

CORRECTED['Van Halen']['Sammy Hagar'] = ['vocals']
