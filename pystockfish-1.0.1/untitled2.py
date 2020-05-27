# -*- coding: utf-8 -*-
"""
Created on Wed May 27 03:05:42 2020

@author: user
"""


from pystockfish import Engine

deepthinker = Engine(depth=15)
deepthinker.setposition(['e2e4','e7e5'])
deepthinker.bestmove()