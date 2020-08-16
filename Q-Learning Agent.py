# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 21:21:15 2020

@author: garvi
"""

from testing_env import Board
import numpy as np
win = 1.0
draw = 0.5
loss = 0.0
 
class QLearning:
    
    def __init__(self):
        self.q = {}
        self.alpha = 0.8
        self.discount = 0.9
        self.initVals = 0.5
        self.mdp = []
        
        self.computer_index = 1
        
    
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
        #print(board.get_legal_actions())
        while True:
            
            optimalMove = np.argmax(qVals)
            if optimalMove in board.get_legal_actions():
                return optimalMove
            else:
                qVals[optimalMove] = -1.0
            
    
    def makeMove(self, board):
        '''
        Inputs: board, state config
        Returns: board, after move made and appends it to our Markov Decision Policy
        '''
        optimalMove = self.getOptimalMove(board)
        self.mdp.append((board, optimalMove))
  
        newBoard = board.makeMove(optimalMove, self.computer_index)
        return newBoard
    
    
    def UpdateQ(self, board):
        
        value = board.heuristic() 

        if (value == 10): value = -1.0
        if (value == 0): value = 0.5
        if (value == -10): value = +1.0
        nextState = -1.0
        self.mdp.reverse()
 
        #print(self.mdp)
        for tuples in self.mdp:
            
            arrayVals = self.getQ(tuples[0])
            if nextState < 0:  # First time through the loop
                arrayVals[tuples[1]] = value
            else:
                arrayVals[tuples[1]] = arrayVals[tuples[1]] * (1.0 - self.alpha) + self.alpha * self.discount * nextState

            self.q[board] = arrayVals            
            nextState = max(arrayVals)
        
        i = 0
        for key in self.q:
            print (i)
            print (self.q[key], end = '\t')
            key.display()
            i += 1
        print (self.q)
       
    def newGame(self):
        self.mdp = []

qAgent = QLearning()


from copy import deepcopy

def train_random():
    random = 0
    sexy = 0
    for i in range(0,100000):
        b = Board()
        b.initBoard(9)

        while True:
            
            if (b.get_legal_actions() == []):
                qAgent.UpdateQ(b)
                break
            
            newBoard = deepcopy(b.computerRandomMove())
            #newBoard = deepcopy(b.makeMove(b.optimalMove(b.board), 2))

            if (b.isTerminal()): 
                qAgent.UpdateQ(b)
                random += 1
                break
               
            #newBoard.display()
            if (newBoard.get_legal_actions() == []): 
                break
            newBoard2 = deepcopy(qAgent.makeMove(newBoard))

            b = newBoard2
            
            if (b.isTerminal()):
                sexy += 1
                qAgent.UpdateQ(b)
                break
    print ("Random has wins: ", end = ' ')
    print(random)
    
    print ("Q Agent has wins ", end = ' ')
    print(sexy)

def train_minimax():
    random = 0
    sexy = 0
    for i in range(0,10):
        b = Board()
        b.initBoard(9)
        qAgent.newGame()

        while True:
            
            if (b.get_legal_actions() == []):
                qAgent.UpdateQ(b)
                break
            
            b.display()
            qAgent.makeMove(b)
            b.display()
            
            if (b.isTerminal()): 
                qAgent.UpdateQ(b)
                random += 1
                break
               
            #newBoard.display()
            if (b.get_legal_actions() == []): 
                break
            
            b.makeMove(b.optimalMove(b.board), 2)

            b.display()
            
            if (b.isTerminal()):
                sexy += 1
                qAgent.UpdateQ(b)
                break
            
    print ("Q Agent has wins: ", end = ' ')
    print(random)
    
    print ("Minimax has wins ", end = ' ')
    print(sexy)
        
def play():

        b = Board()
        b.initBoard(9)
        while True:
            print("\n Len of ")
            print(len(qAgent.q))
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
            
train_minimax()
#play()