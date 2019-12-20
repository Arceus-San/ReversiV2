# -*- coding: utf-8 -*-

import time
import Reversi
from random import randint
from playerInterface import *

class myPlayer(PlayerInterface):

    def __init__(self):
        self._board = Reversi.Board(10)
        self._mycolor = None
        self._tour = 0

    def getPlayerName(self):
        return "MiniMax Player"

    def getPlayerMove(self):
        if self._board.is_game_over():
            print("Referee told me to play but the game is over!")
            return (-1,-1)
        move=self.bestMove()
        self._board.push(move)
        print("I am playing ", move)
        (c,x,y) = move
        assert(c==self._mycolor)
        print("My current board :")
        print(self._board)
        return (x,y) 

    def playOpponentMove(self, x,y):
        assert(self._board.is_valid_move(self._opponent, x, y))
        print("Opponent played ", (x,y))
        self._board.push([self._opponent, x, y])

    def newGame(self, color):
        self._mycolor = color
        self._opponent = 1 if color == 2 else 2

    def endGame(self, winner):
        if self._mycolor == winner:
            print("I won!!!")
        else:
            print("I lost :(!!")

    def heuristique(self):
        if self._mycolor==self._board._WHITE:    
            return self._board._nbWHITE - self._board._nbBLACK
        return self._board._nbBLACK - self._board._nbWHITE

    def minimax(self,depth,maximizingPlayer):
        if(depth==0):
            #print("Game over : ",self._board.is_game_over())
            #print("Legal Moves", self._board.legal_moves())
            #print("Points player 1 : ",self._board._nbBLACK)
            #print("Points player 2 : ",self._board._nbWHITE)  
            return self.heuristique()

        if maximizingPlayer:
            value=-float('infinity')
            for m in self._board.legal_moves():
                #print("Move : ",m)
                self._board.push(m)
                if(self._board.is_game_over()):
                    print("Game Over")
                    value=self.heuristique()
                    print("Score : ",value)
                    self._board.pop()
                    return value
                value=max(value,self.minimax(depth-1,False))
                self._board.pop()
            return value
        else:
            value=float('infinity')
            for m in self._board.legal_moves():
                #print("Move : ",m)
                self._board.push(m)
                if(self._board.is_game_over()):
                    print("Game Over")
                    value=self.heuristique()
                    print("Score : ",value)
                    self._board.pop()
                    return value
                value=min(value,self.minimax(depth-1,True))
                self._board.pop()
            return value

    def bestMove(self):
        self._tour+=1
        if(self._tour<4):
            moves = [m for m in self._board.legal_moves()]
            move = moves[randint(0,len(moves)-1)]
            return move
        #if(self._tour==3):
        #    time.sleep(3600)
        debut=time.time()
        for i in range(1,4):
            mx=-1
            my=-1
            maxpoints=-float('infinity')
            for m in self._board.legal_moves():
                #print("Move : ",m," Profondeur : ",i)
                self._board.push(m)
                points=self.minimax(i-1,False)
                self._board.pop()
                print("Move : ",m," Profondeur : ",i," Points : ",points," Maxpoints : ",maxpoints)

                if points>=maxpoints:
                    maxpoints=points
                    mx=m[1]
                    my=m[2]

                #print("")

        


        return [self._board._nextPlayer,mx,my]











