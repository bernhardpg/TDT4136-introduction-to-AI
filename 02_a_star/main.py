import sys
from PIL import Image

import board as brd
import graph as grph
import tests
import agent

from visualizer import BoardImage
from visualizer import getColor

BOARD_PATH = "00_assets/boards/"
BOARD_NAME = "board-2-1.txt"
TILE_SIZE = 60
LINE_SIZE = 2
CIRCLE_COLOR = getColor('o')
CIRCLE_RADIUS = 10
EXPORT_FILE = "test.png"


def main(argv):
    """
    @param argv takes a board number as argument:
        i.e. 1-1, 1-2 etc.
    """
    global BOARD_NAME

    # Use command line argument if given
    if (len(argv)):
        BOARD_NAME = "board-" + argv[0] + ".txt"

    boards = 4
    levels = 2

    for level in range(1, levels + 1):
        for board in range(1, boards + 1):
            boardName = "board-" + str(level) + "-" + str(board) + ".txt"
            fileName = "01_solved_boards/board-" + str(level) + "-" + str(board) + ".png"

            solveBoard(BOARD_PATH, boardName, fileName)

    return


def solveBoard(BOARD_PATH, boardName, fileName):
    boardMatrix = brd.importBoardMatrix(BOARD_PATH, boardName)
    start, goal = brd.getStartAndGoal(boardMatrix)

    boardGraph = grph.SquareGrid(boardMatrix)
    path = agent.aStar(boardGraph, start, goal)

    boardIm = BoardImage(boardMatrix, TILE_SIZE, LINE_SIZE, CIRCLE_COLOR, CIRCLE_RADIUS)
    boardIm.drawPath(path)
    boardIm.save(fileName)

if __name__ == "__main__":
    main(sys.argv[1:])

