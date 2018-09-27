import sys
from PIL import Image

import board as brd
import visualizer as vis
import graph as grph
import tests

BOARD_PATH = "00_assets/boards/"
BOARD_NAME = "board-1-1.txt"
TILE_SIZE = 100
LINE_SIZE = 3
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
    print("Board matrix:")
    brd.printMatrix(boardMatrix)

    allNodes = grph.getNodes(boardMatrix)
    print("\nNodes:")
    print(allNodes)
    print(grph.neighbors(allNodes[0], allNodes))

    return

if __name__ == "__main__":
    main(sys.argv[1:])

