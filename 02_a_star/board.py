"""
board.py

Functions to import, create or manipulate a board matrix.

"""


def importBoard(BOARD_PATH, BOARD_NAME):
    """
    Imports the board from a 'txt' file and returns the corresponding
    board matrix.

    """
    f = open(BOARD_PATH + BOARD_NAME, 'r')
    boardString = f.read()
    f.close()

    board = getBoardFromString(boardString)
    return board

def getBoardFromString(boardString):
    """
    @param boardString: a string sequence containing
        the entire board data

    @return: the board represented by a two-dimensional matrix
    """
    board = []
    row = []

    for char in boardString:
        if (char == '\n'):
            board.append(row)
            row = []
        else:
            row.append(char)

    return board

def generateEmptyBoard(width, height):
    """
    Generates an empty board matrix filled with '.'

    """
    board = []
    row = []

    for i in range(height):
        for j in range(width):
            row.append('.')
        board.append(row)
        row = []

    return board

def printMatrix(matrix):
    height = len(matrix)
    width = len(matrix[0])
    rowString = "| "

    for i in range(height):
        for j in range(width):
            rowString += matrix[i][j]
            if (j == width - 1):
                rowString += " |"
            else:
                rowString += " "
        print(rowString)
        rowString = "| "

    return
