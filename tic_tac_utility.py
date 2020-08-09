# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 23:28:33 2020

@author: garvi
"""

import error_class as e

class Board:
    
    def __init__(self):
        
        self.board = []
        self.max_tiles = 9
    
        
    def initBoard(self, max_tiles):
        
        ''' 
        A function to initilize a board.
        Initially, the board is empty, hence we have 0's.
        
        I envisioned it being better to have an array instead of a dictionary.
        Later when creating the MDP it can be useful for even Q-learning for data passing
        
        Input: max number of tiles
        Returns: board array
        '''
        
        if (max_tiles <= 0):
            raise e.wrong_tiles("\n\nAtleast enter a positive number")
        
            
        board = []
        
        for i in range(0, self.max_tiles):
            board.append(0) 
        
        return board
    
    
    def __str__(self):
        ''' 
        Overloading representation of boards, ideally prints tictac format
        '''
        
        pass
        
b = Board()
#b.initBoard(0)

print(b)