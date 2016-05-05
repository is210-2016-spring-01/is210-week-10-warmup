#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""task 04: updating/merging dict keys """


import data

data.BANDS['Buckingham Nicks'] = {'Lindsey Buckingham': ['guitar', 'vocals'],
                                  'Stevie Nicks': ['vocals', 'tambourine']}

data.BANDS['Fleetwood Mac'].update(data.BANDS['Buckingham Nicks'])
