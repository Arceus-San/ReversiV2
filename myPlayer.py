# -*- coding: utf-8 -*-

import time
import Reversi
from random import randint
from playerInterface import *

class myPlayer(PlayerInterface):

    def __init__(self):
        self._board = Reversi.Board(10)
        self._mycolor = None

    def getPlayerName(self):
        return "Random Player"

    def getPlayerMove(self):
        if self._board.is_game_over():
            print("Referee told me to play but the game is over!")
            return (-1,-1)
        #moves = [m for m in self._board.legal_moves()]
        #move = moves[randint(0,len(moves)-1)]
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
        if self._mycolor is self._board._WHITE:
            return self._board._nbWHITE - self._board._nbBLACK
        return self._board._nbBLACK - self._board._nbWHITE

    def minimax(self,depth,maximizingPlayer):
        if(depth==0):
            return self.heuristique()

        if maximizingPlayer:
            value=-float('infinity')
            for m in self._board.legal_moves():
                self._board.push(m)
                value=max(value,self.minimax(depth-1,False))
                self._board.pop()
            return value
        else:
            value=float('infinity')
            for m in self._board.legal_moves():
                self._board.push(m)
                value=min(value,self.minimax(depth-1,True))
                self._board.pop()
            return value

    def bestMove(self):
        debut=time.time()
        maxpoints=-float('infinity')
        for i in range(1,2):
            for m in self._board.legal_moves():
                self._board.push(m)
                points=self.minimax(i-1,False)
                self._board.pop()
                print("Move : ",m," Profondeur : ",i," Points : ",points," Maxpoints : ",maxpoints)

                if points>=maxpoints:
                    maxpoints=points
                    mx=m[1]
                    my=m[2]

        time.sleep(6)


        return [self._board._nextPlayer,mx,my]











