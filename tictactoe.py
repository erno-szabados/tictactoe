# Tic-tac-toe is a classic game that has been around for centuries. 
# The rules are simple: two players take turns placing either an X or an O on a 3x3 grid, 
# with the goal of getting three of their marks in a row (vertically, horizontally, or diagonally). 

# TODO
# decision tree representation
# minimax algorithm
# evaluation function:  
# Tic-tac-toe can be brute forced because the number of possible states is small.
# If we assume a deep tree, we can use a heuristic to evaluate the board state.
# Each board state must be evaluated to determine if it is a win, loss, or draw. these are endstates. 
# All rows, columns, and diagonals must be checked for a win. tree iteration can stop if a win is found.
# Each non-endstate must be evaluated to determine the best following move to make.
# Good board states when a heuristic is used examined using the following:
# all rows, columns, and diagonals must be checked for their potential. additionally, the board as a whole can be checked for its potential.
# if the player has two in a row, and there is a free space, and the player is about to move, it is a good board state. the heuristic value must be high.
# row, column, and diagonal values can be summed to determine the board state value.
# to determine a row value, we can use the following:
# if the row is empty, the value is 0.
# if the row has one opponent piece, the value is -1.
# if the row has one player piece, the value is 1.
# if the row has two opponent pieces, the value is -2.
# if the row has two player pieces, the value is 2.
# if the row has three opponent pieces, the value is -3, and it is a loss.
# if the row has three player pieces, the value is 3, and it is a win.
# Determining positional value
# the center is the most valuable position, followed by the corners, and then the edges.
# this is because the center eliminates 4 possible winning positions, the corners eliminate 3, and the edges eliminate 2.
# to represent this, we can use a 3x3 matrix with the following values:
# 3 2 3
# 2 4 2
# 3 2 3


print("tic-tac-toe")

board = list(range(9))

class tictactoe:
    def __init__(self):
        self.board = [0] * 9
        self.symbols = [' ','x', 'o']
        self.EMPTY = 0

        # chosen for summing in win detection
        self.HUMAN = 1
        self.COMPUTER = -1

        # precalculated board indices to check on win condition
        self.WIN = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

    
    def same_sign(self, n1, n2):
        return (n1 * n2) > 0

    def haswon(self, player_id):
        return any(abs(t) == 3 and self.same_sign(t, player_id) for t in [sum([self.board[i] for i in w]) for w in self.WIN])

    def move(self, player_id, x, y):
        ''' 
        player_index - 1 or -1
        update the table state with the player move, if the move is valid.
        return if the move is valid.
        '''
        if x < 3 and y < 3:
            offset = 3 * y + x
            if self.board[offset] == self.EMPTY:
                self.board[offset] = player_id
                return True
        return False

    def print_board(self):
        for i in range(3):
            row_start = 3 * i
            row_end = 3 * i + 3
            print(" | ".join([self.symbols[x] for x in self.board[row_start:row_end]]))
            if i < 2:
                print('--+---+--')


game = tictactoe()
game.print_board()
for i in range(3):
    print(game.move(game.HUMAN, i,i))
    game.print_board()
print(game.haswon(game.HUMAN))
