# TODO Figure out how the agent will read the board, and change the functions accordingly
# TODO Consider adding black grid lines?
# TODO Create docstrings

from PIL import Image

def importBoard(BOARD_PATH, BOARD_FILE):
    f = open(BOARD_PATH + BOARD_FILE, 'r')
    boardString = f.read()
    f.close()

    board, width, height = getBoardFromString(boardString)
    return board, width, height

# Converts the string matrix to a two-dimensional
# matrix containing the color of each tile
def getBoardFromString(boardString):
    board = list()
    row = list()

    for char in boardString:
        if (char == '\n'):
            board.append(row)
            row = list()
        else:
            row.append(convertCharToColor(char))

    height = len(board)
    width = len(board[0])

    return board, width, height

# Creates a Image object of the board
def createBoardImage(board, width, height, TILE_SIZE, LINE_SIZE):
    imSize = (width* (TILE_SIZE + LINE_SIZE), height* (TILE_SIZE + LINE_SIZE))
    boardIm = Image.new('RGB', imSize)

    colorPixels(boardIm, board, TILE_SIZE, LINE_SIZE)

    return boardIm

# Color the pixels in im according to the pixels set in board, and with the tilesize given
def colorPixels(im, board, TILE_SIZE, LINE_SIZE):
    pixelMap = im.load()
    width, height = im.size

    for i in range(height):
        for j in range(width):
            if ((i % (TILE_SIZE + LINE_SIZE) < LINE_SIZE)
                or (j % (TILE_SIZE + LINE_SIZE)) < LINE_SIZE):
                pixelMap[j, i] = (0, 0, 0) #Black
            else:
                pixelMap[j, i] = board[int(i/(TILE_SIZE + LINE_SIZE))][int(j/(TILE_SIZE + LINE_SIZE))]

    return

# NOTE Currently not in use
# Breaks the sequence of pixels down to a two-dimensional matrix
def getPixelMatrix(im):

    pixels = list(im.getdata())
    width, height = im.size
    pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]

    return pixels

def convertCharToColor(char):
    ## STANDARD COLORS
    GREY = (100, 100, 100)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)

    ## TERRAIN COLORS
    WATER = (0, 204, 255)
    MOUNTAINS = (200, 200, 200)
    FORESTS = (0, 102, 0)
    GRASSLANDS = (153, 225, 153)
    ROADS = (153, 102, 51)

    translations = {
        ".": WHITE,
        "#": GREY,
        "A": GREEN,
        "B": RED,
        "w": WATER,
        "m": MOUNTAINS,
        "f": FORESTS,
        "g": GRASSLANDS,
        "r": ROADS,
    }

    return translations[char]

