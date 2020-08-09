# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 23:28:33 2020

@author: garvi
"""

import error_class as e

class Board:
    
    def __init__(self):
        
        self.max_tiles = 9
        self.board = self.initBoard(self.max_tiles)
        
        # 0 = Computer; 1 = Player
        self.player_index = 0
        self.player_choice = 'X'
        
    
    def make_move(self, action, playerID):
        
        if (self.board == []):
            raise e.empty_board("\nBoard is not initialized")
            
        
        
    def initBoard(self, max_tiles):
        
        ''' 
        A function to initilize a board.
        Initially, the board is empty, hence we have 0's.
        
        I envisioned it being better to have an array instead of a dictionary.
        Later when creating the MDP it can be useful for even Q-learning for data passing
        
        Input: max number of tiles
        Returns: board array
        '''
        
        if (max_tiles < 9):
            raise e.wrong_tiles("\n\nAtleast enter a positive number")
        
            
        board = []
        
        for i in range(0, self.max_tiles):
            board.append('_') 
        
        return board
    
    
    def display(self):
        ''' 
        ideally prints tictac format
        '''
        
        print('\n\n')
        
        if (self.board == []):
            raise e.empty_board("\n\nBoard not initiliazed")
            
        rows = int(self.max_tiles / 3)
        cols = int(self.max_tiles / 3)
        
        for i in range(0, rows):
            for j in range(0, cols):
                if (j == (cols - 1)):
                    print ('\t', end = ' ')
                    print (self.board[i], end =' ')
                else:
                    print ('\t', end = ' ')
                    print (self.board[i], end = ' \t| ')
                
            print()
            
        print('\n\n')
        
    
        
b = Board()
b.initBoard(9)
b.display()