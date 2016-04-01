#!/usr/bin/env/python
# -*- coding: utf-8 -*-
"""task 03: creating new or removing entries in dicts"""


import data

CORRECTED = data.BANDS.copy()

CORRECTED['Dylan'] = {'Bob Dylan': ['vocals', 'guitar', 'harmonica']}

del CORRECTED['Van Halen']['David Lee Roth']

CORRECTED['Van Halen']['Sammy Hager'] = 'vocals'
