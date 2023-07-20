class Moves:

    @staticmethod
    def queen(pos):
        queenMoves = Moves.bishop(pos).union(Moves.rook(pos))

        return queenMoves

    @staticmethod
    def rook(pos):
        col, row = getMatrixPos(pos)

        rookMoves = set()
        j, i = col, row

        # UP
        while i < 8:
            rookMoves.add((j, i+1))
            i += 1

        j, i = col, row
        # Right
        while j < 8:
            rookMoves.add((j+1, i))
            j += 1

        j, i = col, row
        # Down
        while i > 1:
            rookMoves.add((j, i-1))
            i -= 1

        j, i = col, row
        # left
        while j > 1:
            rookMoves.add((j-1, i))
            j -= 1

        return rookMoves

    @staticmethod
    def knight(pos):
        col, row = getMatrixPos(pos)

        print(col, row)
        knightMoves = set()

        j, i = col, row

        # Left-Up
        j = j - 2
        i = i + 1
        if j > 0 and i < 9:
            knightMoves.add((j, i))

        j, i = col, row
        # Left-Down
        j = j - 2
        i = i - 1
        if j > 0 and i > 0:
            knightMoves.add((j, i))

        j, i = col, row
        # Down-Left
        j = j - 1
        i = i - 2
        if j > 0 and i > 0:
            knightMoves.add((j, i))

        j, i = col, row
        # Down-Right
        j = j + 1
        i = i - 2
        if j < 9 and i > 0:
            knightMoves.add((j, i))

        j, i = col, row
        # Right-Down
        j = j + 2
        i = i - 1
        if j < 9 and i > 0:
            knightMoves.add((j, i))

        j, i = col, row
        # Right- Up
        j = j + 2
        i = i + 1
        if j < 9 and i < 9:
            knightMoves.add((j, i))

        j, i = col, row
        # Up-Left
        j = j - 1
        i = i + 2
        if j > 0 and i < 9:
            knightMoves.add((j, i))

        j, i = col, row
        # Up-Right
        j = j + 1
        i = i + 2
        if j < 9 and i < 9:
            knightMoves.add((j, i))

        return knightMoves

    @staticmethod
    def bishop(pos):

        col, row = getMatrixPos(pos)

        bishopMoves = set()

        j, i = col, row
        while j > 1 and i > 1:
            bishopMoves.add((j - 1, i - 1))
            j -= 1
            i -= 1

        j, i = col, row

        while j < 8 and i > 1:
            bishopMoves.add((j + 1, i - 1))
            j += 1
            i -= 1

        j, i = col, row

        while j < 8 and i < 8:
            bishopMoves.add((j + 1, i + 1))

            j += 1
            i += 1

        j, i = col, row
        while j > 1 and i < 8:
            bishopMoves.add((j - 1, i + 1))

            j -= 1
            i += 1

        return bishopMoves


def getMatrixPos(data):

    validRows = {'1', '2', '3', '4', '5', '6', '7', '8'}
    vaildCols = {'A': '1', 'B': '2', 'C': '3', 'D': '4',
                 'E': ' 5', 'F': '6', 'G': '7', 'H': '8'}

    row, col = 0, 1
    for i in data:
        if i in vaildCols:
            col = 1
        if i in validRows:
            row = 1

    if row and col:
        r = int(data[1])

        c = int(vaildCols[data[0]])

        return [c, r]


def getMoves(moves):
    map = {"1": "A", "2": "B", "3": "C", "4": "D",
           "5": "E", "6": "F", "7": "G", "8": "H"}
    finalMoves = []
    for col, row in moves:
        move = str(map[str(col)]) + str(row)
        finalMoves.append(move)
    

    return finalMoves
