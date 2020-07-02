# Using some opening book to randomize the games

import Arena

from MCTS import MCTS
from othello.OthelloGame import OthelloGame, display
from othello.OthelloPlayers import *
from othello.pytorch.NNet import NNetWrapper as NNet
from utils import *


class NeuralPlayer():
    def __init__(self, game,  nnet, args, reset=False):
        self.game = game
        self.mcts1 = MCTS(game, nnet, args)
        self.reset = reset
        self.nnet = nnet
        self.args = args
    
    def play(self, board, prevaction):
        if self.reset:
            self.mcts1 = MCTS(self.game, self.nnet, self.args)
        values, prob = self.mcts1.getActionProb(board, temp=-1)
        return values
        
    def force_play(self, board, move):
        return 
    
    def endgame(self):
        return
        

"""
use this script to play any two agents against each other, or play manually with
any agent.
"""
with open('othello/book/XOT/openingssmall.txt') as my_file:
    book_array = my_file.readlines()
    
    
g = OthelloGame(8)

# all players
rp = RandomPlayer(g)
gp = GreedyOthelloPlayer(g)
hp = HumanOthelloPlayer(g)

edax = EdaxPlayer(3, g)


# nnet players
n1 = NNet(g)
n1.load_checkpoint('./temp/','restart.pth.tar')
#n1.load_checkpoint('./pretrained_models/othello/pytorch','restart.pth.tar')
args1 = dotdict({'numMCTSSims': 600, 'cpuct':1.0})
n1p = NeuralPlayer(g, n1, args1)


n2 = NNet(g)
n2.load_checkpoint('./pretrained_models/othello/pytorch','8x8_100checkpoints_best.pth.tar')

args2 = dotdict({'numMCTSSims': 200, 'cpuct':1.0})
n2p = NeuralPlayer(g, n2, args2, False)

arena = Arena.Arena(n1p, edax, g,  display=display, book = book_array)
print(arena.playGames(10, verbose=True))
