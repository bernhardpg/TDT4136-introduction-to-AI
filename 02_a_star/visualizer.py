"""
visualizer.py

Functions needed to vizualise the board and the chosen path.

"""

from PIL import Image

def createBoardImage(board, TILE_SIZE, LINE_SIZE):
    """
    @param: board
    @param: TILE_SIZE
    @param: LINE_SIZE

    @return: Board with colors as an Image object

    """
    height = len(board)
    width = len(board[0])

    boardColors = getColorMatrix(board)

    imSize = (width* (TILE_SIZE + LINE_SIZE), height* (TILE_SIZE + LINE_SIZE))
    boardIm = Image.new('RGB', imSize)

    colorPixels(boardIm, boardColors, TILE_SIZE, LINE_SIZE)

    return boardIm

def colorPixels(im, colorMatrix, TILE_SIZE, LINE_SIZE):
    """
    @param im: Image object to be colored.
    @param colorMatrix: Matrix containing the color information
        for each pixel.
    @param TILE_SIZE
    @param LINE_SIZE

    """
    pixelMap = im.load()
    width, height = im.size

    for i in range(height):
        for j in range(width):
            if ((i % (TILE_SIZE + LINE_SIZE) < LINE_SIZE)
                or (j % (TILE_SIZE + LINE_SIZE)) < LINE_SIZE):
                pixelMap[j, i] = (0, 0,0) #Black
            else:
                pixelMap[j, i] = colorMatrix[int(i/(TILE_SIZE + LINE_SIZE))][int(j/(TILE_SIZE + LINE_SIZE))]

    return

def getColorMatrix(matrix):
    """
    @param boardMatrix: The board represented by a
        two-dimensional matrix with chars

    @return The corresponding matrix with each entry as
        a tupple containing the pixel color
    """
    boardColors = []
    row = []

    height = len(matrix)
    width = len(matrix[0])

    for i in range(height):
        for j in range(width):
            row.append(getColor(matrix[i][j]))
        boardColors.append(row)
        row = []

    return boardColors

def drawCircle(im, x, y, TILE_SIZE, LINE_SIZE, CIRCLE_COLOR, CIRCLE_RADIUS):
    """
    Draws a circle in the center of the desired tile

    @param im: Image object
    @param x, y: tile coordinates (NOT pixel coordinates)
    @TILE_SIZE, LINE_SIZE: constants
    @radius
    æcolor
    """
    pixelMap = im.load()
    offsetX = (TILE_SIZE + LINE_SIZE) * x + LINE_SIZE
    offsetY = (TILE_SIZE + LINE_SIZE) * y + LINE_SIZE

    for i in range(TILE_SIZE):
        for j in range(TILE_SIZE):
            # Circle equation: (x - centerX)**2 + (y - centerY)**2 == radius**2
            if ((j - ((TILE_SIZE - 1)/ 2))**2 + (i - ((TILE_SIZE - 1)/ 2))**2 < (CIRCLE_RADIUS**2)):
                pixelMap[i + offsetX, j + offsetY] = CIRCLE_COLOR

    return

def drawPath(boardIm, boardPath, TILE_SIZE, LINE_SIZE, CIRCLE_COLOR, CIRCLE_RADIUS):
    """
    Draws a given boardPath onto the boardIm object.
    @param boardIm: board as Image object
    @param boardPath: path to be drawn represented by a two dimensional matrix
        '.' represents an empty tile
        'o' represents a part of the path
    """
    height = len(boardPath)
    width = len(boardPath[0])

    for i in range(height):
        for j in range(width):
            if (boardPath[i][j] == 'o'):
                drawCircle(boardIm, j, i, TILE_SIZE, LINE_SIZE, CIRCLE_COLOR, CIRCLE_RADIUS)
    return

def getColor(char):
    """
    @param char: Char to be translated to color code

    @return: Tuple containing RGB information: (R, G, B)

    """
    ## STANDARD COLORS
    GREY = (100, 100, 100)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)

    ## TERRAIN COLORS
    WATER = (0, 204, 255)
    MOUNTAINS = (120, 120, 120)
    FORESTS = (0, 102, 0)
    GRASSLANDS = (153, 225, 153)
    ROADS = (153, 102, 51)

    ## PATH COLOR
    PATH = (0, 0, 0)

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
        "o": PATH,
    }

    return translations[char]

