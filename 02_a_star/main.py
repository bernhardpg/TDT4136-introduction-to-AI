import sys
from PIL import Image

import board as brd
import visualizer as vis
import graph as grph
import tests
from datatypes import Queue
import agent

BOARD_PATH = "00_assets/boards/"
BOARD_NAME = "board-2-1.txt"
TILE_SIZE = 60
LINE_SIZE = 2
CIRCLE_COLOR = vis.getColor('o')
CIRCLE_RADIUS = 20
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

    boardMatrix = brd.importBoard(BOARD_PATH, BOARD_NAME)
    start, goal = brd.getStartAndGoal(boardMatrix)

    boardGraph = grph.SquareGrid(boardMatrix)
    path = agent.aStar(boardGraph, start, goal)
    boardPath = brd.constructPathMatrix(boardGraph, path)

    boardIm = vis.createBoardImage(boardMatrix, TILE_SIZE, LINE_SIZE)
    vis.drawPath(boardIm, boardPath, TILE_SIZE, LINE_SIZE, CIRCLE_COLOR, CIRCLE_RADIUS)
    boardIm.show()

    return

if __name__ == "__main__":
    main(sys.argv[1:])

