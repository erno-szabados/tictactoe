# Tic-tac-toe is a classic game that has been around for centuries. 
# The rules are simple: two players take turns placing either an X or an O on a 3x3 grid, 
# with the goal of getting three of their marks in a row (vertically, horizontally, or diagonally). 

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
