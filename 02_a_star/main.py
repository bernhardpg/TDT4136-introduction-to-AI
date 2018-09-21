import sys
from PIL import Image

from board import *
from visualizer import *
from tests import *


def main(argv):
    """
    @param argv takes a board number as argument:
        i.e. 1-1, 1-2 etc.
    """

    BOARD_PATH = "00_assets/boards/"
    BOARD_NAME = "board-2-1.txt"
    TILE_SIZE = 100
    LINE_SIZE = 3
    CIRCLE_COLOR = getColor('o')
    CIRCLE_RADIUS = 20
    EXPORT_FILE = "test.png"

    # Use command line argument if given
    if (len(argv)):
        BOARD_NAME = "board-" + argv[0] + ".txt"

    board = importBoard(BOARD_PATH, BOARD_NAME)
    boardIm = createBoardImage(board, TILE_SIZE, LINE_SIZE)
    boardPath = generateTestPath(len(board[0]), len(board))

    drawPath(boardIm, boardPath, TILE_SIZE, LINE_SIZE, CIRCLE_COLOR, CIRCLE_RADIUS)

    boardIm.show()

    return

if __name__ == "__main__":
    main(sys.argv[1:])

