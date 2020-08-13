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
        self.computer_index = 2
        self.rows = [self.board[x:x+3] for x in range(0,len(self.board),3)]

        
    
    def get_legal_actions(self):
        
        actions = []
        
        for i in range(len(self.board)):
            if (self.board[i] == '_'): 
                actions.append(i)
            else:
                pass
            
        return actions
    
    def makeMove(self, action, playerID):
        
        '''
        Returns a new board instance updated with made move
        Inputs: action, what action to take. (An integer, no GUI as of now)
                playerID, what is the player ID
        
        Returns: Updated board object, not modified but updated.
        '''
        
        if (self.board == []):
            raise e.empty_board("\nBoard is not initialized")
        
        legalActions = self.get_legal_actions()
        
        
        if not action in legalActions:
            raise e.fatal_error("Something went wrong. Please Restart.")
            exit()
        
        newBoard = Board()
        newBoard.board = self.board
        
        self.display()
        
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
    
    
    def computerRandomMove(self):
        
        legalActions = self.get_legal_actions()

        action = random.choice(legalActions)
        
        newBoard = self.makeMove(action, self.computer_index)
        
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

    def rowUtility(self):
        
        '''
        If all the rows are one value, game has ended.
        '''
    
        subList = [self.board[x:x+3] for x in range(0,len(self.board), 3)]
        
        for rows in subList:
            if (all(element == rows[0] for element in rows) and rows[0] != '_'):
                return True, rows[0]
            else:
                pass
            
        return False, -69
            
            
    def colUtility(self):
        subList = []
        
        # First reorganize it row format
        for i in range(0, 3):
            for x in range(i,9,3):
                subList.append(self.board[x])
        
        # Reuse previse snippet to sublist it. Genius.
        subList = [subList[x:x+3] for x in range(0,len(self.board), 3)]

        for cols in subList:
            if (all(element == cols[0] for element in cols) and cols[0] != '_'):
                return True, cols[0]
            else:
                pass
            
        return False, -69
      
    def diagUtility(self):
        
        # I simply did the above stuff for fun, I dont think I needed to do this, I could just do basic
        # Partioning. Here, it seems crazily overkill sooo
        # I simply did the above stuff for fun, I dont think I needed to do this, I could just do basic
        # Partioning. Here, it seems crazily overkill sooo
        
        if (self.board[0] == self.board[4] and self.board[0] == self.board[8] and self.board[0] != '_'):
            return True, self.board[0]
        
        if (self.board[2] == self.board[4] and self.board[2] == self.board[6] and self.board[2] != '_'):
            return True, self.board[2]
        
        return False, -69
    


    def miniMax(self, depth, player, board):

        if (depth == 0 or self.isTerminal()[0]):
            _, heurestic = self.isTerminal()
            return heurestic
        
        if (player == True):
            value = -10000
            for action in self.get_legal_actions():

                board[action] = 2
                value = max(value, self.miniMax(depth - 1 , ~player, board))  
                board[action] = '_'
            return value - depth
        else:
            value = 100000
            for action in self.get_legal_actions():
                
                board[action] = 1
                value = min(value, self.miniMax(depth - 1 , ~player, board))
                board[action] = '_'
            return value + depth
        
    def optimalMove(self, board):
        
        inf = -100
        
        if (self.get_legal_actions() == []):
            print("Draw!")
            exit()
            
        bestAction = self.get_legal_actions()[0]
 
        for action in self.get_legal_actions():
            board[action] = 2
            value = self.miniMax(9, 2, board)
            board[action] = '_'
            print(value)
            if value > inf:
                inf = value
                bestAction = action
        
        
        return bestAction
        
    
    def isTerminal(self):
        
        isRows, _ = self.rowUtility()
        isCols, _ = self.colUtility()
        isDiag, _ = self.diagUtility()
        
        
        
        if (isRows): 
            if (self.rowUtility()[1] == 2):
                return True, +10
            else:
                return True, -10

        if (isCols): 
            if (self.colUtility()[1] == 2):
                return True, +10
            else:
                return True, -10

        if (isDiag): 
            if (self.diagUtility()[1] == 2):
                return True, +10
            else:
                return True, -10
    

        return False, 0
        
b = Board()
b.initBoard(9)


while True:
    i = input("Enter where to put Value: ")
    b.makeMove(int(i) - 1, 1)
    b.display()

    if (b.isTerminal()[0]): 
        print ("Player wins")
        exit()

    if (b.board == []):
        print("Draw!")
        exit()
            
    b.makeMove(b.optimalMove(b.board), 2)
    b.display()
    
    if (b.isTerminal()[0]):
        print("Computer Wins")
        exit()

