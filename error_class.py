# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 00:12:17 2020

@author: garvi
"""


class Error(Exception):
    pass


class wrong_tiles(Exception):
    ''' Idiot entered wrong number of tiles '''
    pass


class empty_board(Exception):
    ''' Board is not initilized '''
    pass


class not_implemented(Exception):
    ''' Function not implemented '''
    pass

class fatal_error(Exception):
    ''' If something really really goes wrong... '''
    pass