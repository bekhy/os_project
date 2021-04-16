class Color():
    Black = 0
    White = 1
    EMPTY = 2

class Empty():
    color = Color.EMPTY

    def get_moves(self, board, x, y):
        raise Exception("Error")

    def __str__(self):
        return "*"

class ChessColor():
    def __init__(self, color):
        self.color = color

class Board():
    def __init__(self):
        self.board = [[Empty()] * 8 for y in range(8)]
        xw = 1
        yw = 0
        xb = 6
        yb = 0
        for i in range(8):
            self.board[xw][yw] = Pawn(0)
            yw += 1

        for j in range(8):
            self.board[xb][yb] = Pawn(1)
            yb += 1
        # self.board[1][0] = Pawn(Color.Black)
        # self.board[1][1] = Pawn(Color.Black)
        # self.board[1][2] = Pawn(Color.Black)
        # self.board[1][3] = Pawn(Color.Black)
        # self.board[1][4] = Pawn(Color.Black)
        # self.board[1][5] = Pawn(Color.Black)
        # self.board[1][6] = Pawn(Color.Black)
        # self.board[1][7] = Pawn(Color.Black)
        # self.board[6][0] = Pawn(Color.White)
        # self.board[6][1] = Pawn(Color.White)
        # self.board[6][2] = Pawn(Color.White)
        # self.board[6][3] = Pawn(Color.White)
        # self.board[6][4] = Pawn(Color.White)
        # self.board[6][5] = Pawn(Color.White)
        # self.board[6][6] = Pawn(Color.White)
        # self.board[6][7] = Pawn(Color.White)
        self.board[0][3] = King(Color.Black)
        self.board[7][3] = King(Color.White)
        self.board[0][4] = Quenn(Color.Black)
        self.board[7][4] = Quenn(Color.White)
        self.board[0][5] = Bishop(Color.Black)
        self.board[0][2] = Bishop(Color.Black)
        self.board[7][5] = Bishop(Color.White)
        self.board[7][2] = Bishop(Color.White)
        self.board[0][6] = Knight(Color.Black)
        self.board[0][1] = Knight(Color.Black)
        self.board[7][6] = Knight(Color.White)
        self.board[7][1] = Knight(Color.White)
        self.board[0][7] = Castle(Color.Black)
        self.board[0][0] = Castle(Color.Black)
        self.board[7][7] = Castle(Color.White)
        self.board[7][0] = Castle(Color.White)




    def get_color(self, x, y):
        return self.board[y][x].color

    def get_moves(self, x, y):
        return self.board[y][x].get_moves(self, x, y)

    def move(self, xy_from, xy_to):
        self.board[xy_to[1]][xy_to[0]] = self.board[xy_from[1]][xy_from[0]]
        self.board[xy_from[1]][xy_from[0]] = Empty()

    def __str__(self):
        pro = ""
        for i in range(8):
            pro += "".join(map(str, self.board[i])) + "\n"
        return pro



class Pawn(ChessColor):
    def __str__(self):
        return ("♙", "♟")[self.color]

    def get_moves(self, board, x ,y):
        moves = []
        if self.color == Color.Black and y < 7 and board.get_color(x, y+1) == Color.EMPTY:
            moves.append([x, y+1])
        if self.color == Color.White and y < 0 and board.get_color(x, y-1) == Color.EMPTY:
            moves.append([x, y-1])
        return moves

class King(ChessColor):
    def __str__(self):
        return ("♔", "♚")[self.color]


class Quenn(ChessColor):
    def __str__(self):
        return ("♕", "♛")[self.color]

class Bishop(ChessColor):
    def __str__(self):
        return ("♗", "♝")[self.color]

class Knight(ChessColor):
    def __str__(self):
        return ("♘", "♞")[self.color]

class Castle(ChessColor):
    def __str__(self):
        return ("♖", "♜")[self.color]

b = Board()
print(b)

m = b.get_moves(1, 1)
b.move([1,1], m[0])
print(b)
#
# n = b.get_moves(6,6)
# b.move([6,6], m[0])
# print(b)