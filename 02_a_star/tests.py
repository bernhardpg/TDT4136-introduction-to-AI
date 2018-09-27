"""
tests.py

Various tests

"""

import board as brd

def generateTestPath(width, height):
    testPath = brd.generateEmptyBoard(width, height)

    testPath[3][3] = 'o'
    testPath[3][4] = 'o'
    testPath[3][5] = 'o'
    testPath[3][6] = 'o'
    testPath[3][7] = 'o'
    testPath[3][8] = 'o'
    testPath[4][8] = 'o'
    testPath[5][8] = 'o'
    testPath[6][8] = 'o'

    return testPath
