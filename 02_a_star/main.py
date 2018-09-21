from board import *
from visualizer import *
from PIL import Image

def main():

    BOARD_PATH = "00_assets/boards/"
    BOARD_NAME = "board-1-1.txt"
    TILE_SIZE = 30
    LINE_SIZE = 1
    CIRCLE_COLOR = getColor('o')
    CIRCLE_RADIUS = 3
    EXPORT_FILE = "test.png"

    board = importBoard(BOARD_PATH, BOARD_NAME)
    boardIm = createBoardImage(board, TILE_SIZE, LINE_SIZE)
    boardPath = generateEmptyBoard(len(board[0]), len(board))

    boardPath[3][3] = 'o'
    boardPath[3][4] = 'o'
    boardPath[3][5] = 'o'
    boardPath[3][6] = 'o'
    boardPath[3][7] = 'o'
    boardPath[3][8] = 'o'
    boardPath[4][8] = 'o'
    boardPath[5][8] = 'o'
    boardPath[6][8] = 'o'

    printMatrix(boardPath)
    printMatrix(board)

    drawPath(boardIm, boardPath, TILE_SIZE, LINE_SIZE, CIRCLE_COLOR, CIRCLE_RADIUS)

    boardIm.show()

    return

if __name__ == "__main__":
    main()

