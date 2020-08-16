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
        
    
    def hashBoard(self, board):
            
        result = 0
        for i in range(9):
            result *= 3
            if (board.board[i] == '_'):
                result += 1
            elif (board.board[i] == 1):
                result += 2
            elif (board.board[i] == 2):
                result +=3
            #result += board.board[i]
            
        return result
    
        
    
    def getQ(self, hashValue):
        
        '''
        Input: board, class Board type encapsulating current state
        Returns: array, self.q[board] which has q value for each move opting for the best one.
        '''
     

        if hashValue in self.q:
            return self.q[hashValue]
        
        else:
            boardVals = [self.initVals] * 9
            self.q[hashValue] = boardVals
            return self.q[hashValue]
            
    def getOptimalMove(self, hashValue, board):
        '''
        Input: state board
        Returns: max value in the q hash
        '''
        qVals = self.getQ(hashValue)

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

        hashVal = self.hashBoard(board)
        
        optimalMove = self.getOptimalMove(hashVal, board)
        self.mdp.append((hashVal, optimalMove))
  
        return board.makeMove(optimalMove, self.computer_index)
        #return newBoard
    
    
    def UpdateQ(self, board):
        
        value = board.heuristic() 

        if (value == 10): value = -1.0
        if (value == 0): value = 0.5
        if (value == -10): value = +1.0
        nextState = -1.0
        self.mdp.reverse()
 
        for tuples in self.mdp:
#            shit = self.hashBoard(tuples[0])
            arrayVals = self.getQ(tuples[0])
            if nextState < 0:  # First time through the loop
                arrayVals[tuples[1]] = value
            else:
                arrayVals[tuples[1]] = arrayVals[tuples[1]] * (1.0 - self.alpha) + self.alpha * self.discount * nextState

            self.q[self.hashBoard(board)] = arrayVals            
            nextState = max(arrayVals)
        
        
    def newGame(self):
        self.mdp = []

qAgent = QLearning()


from copy import deepcopy
import random

def train_minimax():
    random2 = 0
    sexy = 0
    for i in range(0,10):
        b = Board()
        b.initBoard(9)
        qAgent.newGame()

        while True:
            
            if (b.get_legal_actions() == []):
                qAgent.UpdateQ(b)
                break
            
            choice = random.randint(-1, 1)
            if (choice <= 0.5 and choice >= -0.5):
                secondBoard = deepcopy(b.makeMove(b.optimalMove(b.board), 2))
            else:
                secondBoard = deepcopy(b.computerRandomMove())
            secondBoard.display()
            
            if (secondBoard.isTerminal()):
                sexy += 1
                qAgent.UpdateQ(secondBoard)
                break
                        
            if (b.get_legal_actions() == []): 
                break
            
            firstBoard = deepcopy(qAgent.makeMove(secondBoard))
            firstBoard.display()
            
            if (firstBoard.isTerminal()): 
                qAgent.UpdateQ(firstBoard)
                random2 += 1
                break
               
            b = firstBoard
    
    print (qAgent.q)
   
        
    print ("Q Agent has wins: ", end = ' ')
    print(random2)
    
    print ("Minimax has wins ", end = ' ')
    print(sexy)
        
def play():

        b = Board()
        b.initBoard(9)
        for i in range(9):
            
            b = Board()
            b.initBoard(9)
            qAgent.newGame()
            while True:
                print("\n Len of ")
                print(len(qAgent.q))
                i = input("Enter where to put Value: ")
                newBoard = b.makeMove(int(i) - 1, 2)
                newBoard.display()
            
                if (b.isTerminal()): 
                    print ("Player wins")
                    break
               
                if (b.optimalMove(b.board) == -1): 
                    print ("Draw")
                    break
                    
                qAgent.makeMove(newBoard)
                newBoard.display()
                    
                if (b.isTerminal()):
                    qAgent.UpdateQ(b)
                    break
            
train_minimax()

play()