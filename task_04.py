#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This is the week 10 warmup task 2 that references a dictionary."""

from data import BANDS

OLDNAME = 'Buckingham Nicks'
NEWNAME = 'Fleetwood Mac'

NEWBANDS = {
    OLDNAME: {
        'Lindsey Buckingham': ['guitar', 'vocals'],
        'Stevie Nicks': ['vocals', 'tambourine']
    }
}

NEWBANDS[NEWNAME] = BANDS[NEWNAME]

for (key, values) in NEWBANDS[OLDNAME].iteritems():

    NEWBANDS[NEWNAME][key] = values

BANDS.update(NEWBANDS)
