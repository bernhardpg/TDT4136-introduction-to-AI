"""
graph.py
Toolkit for creating and modifying a graph representation of a two dimensional matrix.

"""


def getNodes(matrix):

    nodes = []
    width = len(matrix[0])
    height = len(matrix)

    for x in range(width):
        for y in range(height):
            nodes.append([x, y])

    return nodes

def neighbors(node, allNodes):
    """
    @param node
    Returns all the neighbors for a node

    """
    # Up, down, left, right
    dirs = [[0, 1], [0, -1], [-1, 0], [1, 0]]
    result = []

    for dir in dirs:
        neighbor = [node[0] + dir[0], node[1] + dir[1]]
        # Make sure the node is not out of bounds
        if neighbor in allNodes:
            result.append(neighbor)

    return result
