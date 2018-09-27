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

    boardMatrix = brd.importBoardMatrix(BOARD_PATH, BOARD_NAME)
    start, goal = brd.getStartAndGoal(boardMatrix)

    boardGraph = grph.SquareGrid(boardMatrix)
    path = agent.aStar(boardGraph, start, goal)
    boardPath = brd.constructPathMatrix(boardGraph, path)

    boardIm = BoardImage(boardMatrix, TILE_SIZE, LINE_SIZE, CIRCLE_COLOR, CIRCLE_RADIUS)
    print(path)
    boardIm.drawPath(boardPath)
    boardIm.show()

    return

if __name__ == "__main__":
    main(sys.argv[1:])

