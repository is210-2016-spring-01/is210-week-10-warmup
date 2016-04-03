#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Remove dictionary keys exercise."""

import data

CORRECTED = data.BANDS.copy()

CORRECTED['Dylan'] = {'Bob Dylan': ['vocals', 'guitar', 'harmonica']}

del CORRECTED['Van Halen']['David Lee Roth']

CORRECTED['Van Halen'].update({'Sammy Hagar': ['vocals']})
