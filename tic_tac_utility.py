# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 23:28:33 2020

@author: garvi
"""

import error_class as e
import random

class Board:
    
    def __init__(self):
        
        self.max_tiles = 9
        self.board = self.initBoard(self.max_tiles)
        
        # 0 = Computer; 1 = Player
        self.computer_index = 0
        
        
    
    def get_legal_actions(self):
        
        actions = []
        
        for i in range(len(self.board)):
            if (self.board[i] == '_'): 
                actions.append(i)
            else:
                pass
            
        return actions
    
    def make_move(self, action, playerID):
        
        '''
        Returns a new board instance updated with made move
        Inputs: action, what action to take. (An integer, no GUI as of now)
                playerID, what is the player ID
        
        Returns: Updated board object, not modified but updated.
        '''
        
        if (self.board == []):
            raise e.empty_board("\nBoard is not initialized")
        
        legalActions = self.get_legal_actions()
        
        print(legalActions)
        print(self.board)
        
        if not action in legalActions:
            raise e.fatal_error("Something went wrong. Please Restart.")
            exit()
        
        newBoard = Board()
        newBoard.board = self.board
        
        if action in legalActions:
            
            if playerID == self.computer_index:
                newBoard.board[action] = 2
            
            else:
                newBoard.board[action] = 1
    
        
        return newBoard
        
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
    
    
    def computer_move(self):
        
        legalActions = self.get_legal_actions()
    
            
        action = random.choice(legalActions)

        
        newBoard = self.make_move(action, self.computer_index)
        
        newBoard.display()
        
    
    
    
    def display(self):
        ''' 
        ideally prints tictac format
        '''
        print('\n\n')
        
        if (self.board == []):
            raise e.empty_board("\n\nBoard not initiliazed")
            
        rows = int(self.max_tiles / 3)
        cols = int(self.max_tiles / 3)
        
        index = 0
        
        for i in range(0, rows):
            for j in range(0, cols):
                if (j == (cols - 1)):
                    print ('\t', end = ' ')
                    print (self.board[index], end =' ')
                    index += 1
                else:
                    print ('\t', end = ' ')
                    print (self.board[index], end = ' \t| ')
                    index += 1
                
            print()
            
        print('\n\n')
        
    
        
b = Board()
b.initBoard(9)

while True:
    i = input("enter where to put shit")

    c = b.make_move(int(i), 1)
    c.display()

    d = c.computer_move()


