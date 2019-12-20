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
        #print("Next Player : ",self._board._nextPlayer)
        if self._board._nextPlayer==1:
            return self._board._nbWHITE - self._board._nbBLACK
        return self._board._nbBLACK - self._board._nbWHITE

    def negascout(self,depth,alpha,beta):
        if(depth==0 or len(self._board.legal_moves())<=1):
            return self.heuristique()
        cpt=0
        for m in self._board.legal_moves():
            cpt+=1
            if(cpt==1):
                self._board.push(m)
                score=-self.negascout(depth-1,-beta,-alpha)
                self._board.pop()
            else:
                self._board.push(m)
                score=-self.negascout(depth-1,-alpha-1,-alpha)
                self._board.pop()
                if(alpha<score<beta):
                    self._board.push(m)
                    score=-self.negascout(depth-1,-beta,-score)
                    self._board.pop()
            alpha=max(alpha,score)
            if alpha>=beta:
                break
        return alpha

    def bestMove(self):
        debut=time.time()
        maxpoints=-float('infinity')
        for i in range(1,5):
            for m in self._board.legal_moves():
                self._board.push(m)
                points=self.negascout(i-1,-float('infinity'),float('infinity'))
                self._board.pop()
                print("Move : ",m," Profondeur : ",i," Points : ",points," Maxpoints : ",maxpoints)

                if points>=maxpoints:
                    maxpoints=points
                    mx=m[1]
                    my=m[2]

        #time.sleep(3)



        return [self._board._nextPlayer,mx,my]












