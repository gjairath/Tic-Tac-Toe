# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 21:21:15 2020

@author: garvi
"""

from testing_env import Board

 
class QLearning:
    
    def __init__(self):
        self.q = {}
        self.alpha = 0.8
        self.discount = 0.9
        self.initVals = 0.5
        self.mdp = []
        
        self.computer_index = 2 
        
    
    def getQ(self, board):
        
        '''
        Input: board, class Board type encapsulating current state
        Returns: array, self.q[board] which has q value for each move opting for the best one.
        '''
        
        if board in self.q:
            return self.q[board]
        
        else:
            boardVals = [self.initVals] * 9
            self.q[board] = boardVals
            return self.q[board]
            
    def getOptimalMove(self, board):
        '''
        Input: state board
        Returns: max value in the q hash
        '''
        qVals = self.getQ(board)
        #print(optimalMove)
        print(board.get_legal_actions())
        while True:
            optimalMove = qVals.index(max(qVals))
            if optimalMove in board.get_legal_actions():
                return optimalMove
            else:
                qVals[optimalMove] = -1.0
            
    
    def makeMove(self, board):
        '''
        Inputs: board, state config
        Returns: board, after move made and appends it to our Markov Decision Policy
        '''
        #print(self.q)
        optimalMove = self.getOptimalMove(board)
        #print(optimalMove)
        #print(board)
        newBoard = board.makeMove(optimalMove, self.computer_index)
        self.mdp.append((board, optimalMove))
        return newBoard
    
    
    def UpdateQ(self, board):
        
        value = board.heuristic() # +10 if computer has won; -10 if computer has lost; 0 if we have drawn.
        value = value / 10 #Normalize values to single digit for convineice.
        if (value == 0): value = 0.5
        nextState = 0
        self.mdp.reverse()
        for tuples in self.mdp:
            #tuples[0] is the last board
            #tuples[1] is the move taken to get there
            arrayVals = self.getQ(tuples[0])
            if (nextState == 0): nextState = value
            arrayVals[tuples[1]] = (1 - self.alpha) * arrayVals[tuples[1]] + self.alpha * self.discount * nextState
            nextState = max(arrayVals)
        
        print(self.q)


qAgent = QLearning()
def train():
    b = Board()
    b.initBoard(9)
    for i in range(0,100000):
        while True:
            
            if (b.get_legal_actions() == []):
                qAgent.UpdateQ(b)
                break
            
            newBoard = b.computerRandomMove()
            
            if (b.isTerminal()): 
                qAgent.UpdateQ(b)
                break
               
            qAgent.makeMove(newBoard)
            newBoard.display()
                
            if (b.isTerminal()):
                qAgent.UpdateQ(b)
                break
        
def play():
        b = Board()
        b.initBoard(9)
        while True:
            i = input("Enter where to put Value: ")
            newBoard = b.makeMove(int(i) - 1, 1)
            newBoard.display()
        
            if (b.isTerminal()): 
                print ("Player wins")
                exit()
        
           
            if (b.optimalMove(b.board) == -1): 
                print ("Draw")
                exit()
                
            qAgent.makeMove(newBoard)
            newBoard.display()
                
            if (b.isTerminal()):
                qAgent.UpdateQ(b)
                break
            
train()
play()