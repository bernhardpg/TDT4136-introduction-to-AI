from board import *
from PIL import Image

def main():

    BOARD_PATH = "00_assets/boards/"
    BOARD_FILE = "board-2-4.txt"
    TILE_SIZE = 30
    LINE_SIZE = 1
    EXPORT_FILE = "test.png"

    board, width, height = importBoard(BOARD_PATH, BOARD_FILE)
    boardImage = createBoardImage(board, width, height, TILE_SIZE, LINE_SIZE)

    boardImage.show()
    boardImage.save(EXPORT_FILE)

    return

if __name__ == "__main__":
    main()

