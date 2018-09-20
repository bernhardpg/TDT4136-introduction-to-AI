from board import *
from PIL import Image

def main():

    BOARD_PATH = "00_assets/boards/"
    BOARD_NAME = "board-2-4.txt"
    TILE_SIZE = 30
    LINE_SIZE = 1
    EXPORT_FILE = "test.png"

    board = importBoard(BOARD_PATH, BOARD_NAME)
    boardIm = createBoardImage(board, TILE_SIZE, LINE_SIZE)
    boardIm.show()
    printMatrix(board)

    return

if __name__ == "__main__":
    main()

