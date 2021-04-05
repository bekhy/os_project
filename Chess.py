class Board:
    def __init__(self):
        self.board = [["*"] * 8 for i in range(8)]
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

        self.board[0][3] = King(0)
        self.board[7][3] = King(1)
        self.board[0][4] = Quenn(0)
        self.board[7][4] = Quenn(1)
        self.board[0][5] = Bishop(0)
        self.board[0][2] = Bishop(0)
        self.board[7][5] = Bishop(1)
        self.board[7][2] = Bishop(1)
        self.board[0][6] = Knight(0)
        self.board[0][1] = Knight(0)
        self.board[7][6] = Knight(1)
        self.board[7][1] = Knight(1)
        self.board[0][7] = Castle(0)
        self.board[0][0] = Castle(0)
        self.board[7][7] = Castle(1)
        self.board[7][0] = Castle(1)


    def __str__(self):
        pro = ""
        for i in range(8):
            pro += "".join(map(str, self.board[i])) + "\n"
        return pro


class Pawn(Board):
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return ("♙", "♟")[self.color]


class King(Board):
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return ("♔", "♚")[self.color]


class Quenn(Board):
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return ("♕", "♛")[self.color]

class Bishop(Board):
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return ("♗", "♝")[self.color]

class Knight(Board):
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return ("♘", "♞")[self.color]

class Castle(Board):
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return ("♖", "♜")[self.color]

print(Board())
