"""
board.py

Functions to import, create or manipulate a board matrix.

"""


def importBoardMatrix(BOARD_PATH, BOARD_NAME):
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

def getStartAndGoal(boardMatrix):
    width = len(boardMatrix[0])
    height = len(boardMatrix)

    for y in range(height):
        for x in range(width):
            if boardMatrix[y][x] == 'A':
                start = (x, y)
            elif boardMatrix[y][x] == 'B':
                goal = (x, y)

    return start, goal

def generateEmptyBoard(width, height):
    """
    Generates an empty board matrix filled with '.'

    """
    board = [['.' for x in range(width)] for y in range(height)]

    return board

def constructPathMatrix(graph, path):
    pathMatrix = generateEmptyBoard(graph.width, graph.height)

    for node in path:
        # has to be y, x when writing to a two-dimensional matrix!
        pathMatrix[node[1]][node[0]] = 'o'

    return pathMatrix

def printMatrix(matrix):
    height = len(matrix)
    width = len(matrix[0])
    rowString = "| "

    for y in range(height):
        for x in range(width):
            # has to be y, x when reading from a two-dimensional matrix!
            rowString += matrix[y][x]
            if (x - width ==  - 1):
                rowString += " |"
            else:
                rowString += " "
        print(rowString)
        rowString = "| "

    return

