import numpy as np

import othello.edax_api



class RandomPlayer():
    def __init__(self, game):
        self.game = game

    def play(self, board, prevaction):
        a = np.random.randint(self.game.getActionSize())
        valids = self.game.getValidMoves(board, 1)
        while valids[a]!=1:
            a = np.random.randint(self.game.getActionSize())
        return a

    def force_play(self, game, move ):
        return 
    
    def endgame(self):
        return

class HumanOthelloPlayer():
    def __init__(self, game):
        self.game = game
        
        
    def force_play(self, game, move ):
        return 

    def play(self, board, prevaction):
        # display(board)
        valid = self.game.getValidMoves(board, 1)
        for i in range(len(valid)):
            if valid[i]:
                print(int(i/self.game.n), int(i%self.game.n))
        while True:
            a = input()
            x,y = [int(x) for x in a.split(' ')]
            a = self.game.n * x + y if x!= -1 else self.game.n ** 2
            if valid[a]:
                break
            else:
                print('Invalid')
        return a

    def endgame(self):
        return

class EdaxPlayer():
    def __init__(self, level, game):
        self.edax = othello.edax_api.Edax()
        self.edax.set_level(level)
        self.game = game

    def force_play(self, game, move ):
        self.edax.force_move(move)
        return 

    def play(self, board, move):
        answer = self.edax.make_move(move)
        return answer

    def endgame(self):
        self.edax.write_stdin("new")
        self.edax.read_stdout()


        

class GreedyOthelloPlayer():
    def __init__(self, game):
        self.game = game

    def force_play(self, game, move):
        return 
    
    def play(self, board, prevaction):
        valids = self.game.getValidMoves(board, 1)
        candidates = []
        for a in range(self.game.getActionSize()):
            if valids[a]==0:
                continue
            nextBoard, _ = self.game.getNextState(board, 1, a)
            score = self.game.getScore(nextBoard, 1)
            candidates += [(-score, a)]
        candidates.sort()
        return candidates[0][1]

    def endgame(self):
        return

