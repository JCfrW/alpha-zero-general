
from subprocess import PIPE, STDOUT, Popen

# edax config
edax_level = 1
edax_path = "./edax/Edax"
edax_eval_path = "./edax/data/eval.dat"
edax_book_path = "./edax/data/book.dat"


def rl_2_othello(move):
    if move == 64:
        return "pass"
    ligne = move // 8
    col = move % 8
    return "abcdefgh"[col]+str(ligne+1)

def othello_2_rl(move):
    if move == "PS" : 
        return 64
    ligne = int(move[1]) -1
    col = ["A", "B", "C", "D", "E", "F", "G", "H"].index(move[0])
    return ligne * 8 + col
        
class Edax:


    def __init__(self):
        self.edax = Popen(edax_path + " -q -eval-file " + edax_eval_path  , shell=True, stdout=PIPE, stdin=PIPE, stderr=STDOUT)
        self.read_stdout()

    def set_level(self, level):
        self.write_stdin("l " + str(level))
        self.read_stdout()
        self.write_stdin("b randomness")
        self.read_stdout()

    def make_move(self, move):
        if move != -1 :
            self.write_stdin(rl_2_othello(move))
            self.read_stdout()

        self.write_stdin("go")
        edax_move_plane = self.read_stdout().split("plays ")[-1][:2]
        return othello_2_rl(edax_move_plane)

    def write_stdin(self, command):
        self.edax.stdin.write(str.encode(command + "\n"))
        self.edax.stdin.flush()

    def read_stdout(self):
        out = b''
        while True:
            next_b = self.edax.stdout.read(1)
            if next_b == b'>' and ((len(out) > 0 and out[-1] == 10) or len(out) == 0):
                break
            else:
                out += next_b
        return out.decode("utf-8")

    def close(self):
        self.edax.terminate()
