# -*- coding: utf-8 -*-
"""

Created on 2019-06-16 09:34

@author: liubo
"""


import logging
from pprint import pprint
from sys import stdout as STDOUT

# Example 1
class GameState(object):
    def __init__(self):
        self.level = 0
        self.lives = 4


# Example 2
state = GameState()
state.level += 1
state.lives -= 1


# Example 3

import pickle





























