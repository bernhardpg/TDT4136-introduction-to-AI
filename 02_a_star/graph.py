"""
graph.py
Toolkit for creating and modifying a graph representation of a two dimensional matrix.

"""

class SquareGrid:
    """ General Graph object """
    def __init__(self, matrix):
        self.width = len(matrix[0])
        self.height = len(matrix)
        self.nodes  = getNodesFromMatrix(matrix, self.width, self.height)

    def neighbors(self, node):
        return getNeighbors(node, self.nodes)


def getNodesFromMatrix(matrix, width, height):
    """ Creates a list of nodes from a two dimensional matrix. """
    nodes = []

    for x in range(width):
        for y in range(height):
            nodes.append((x, y))

    return nodes

def getNeighbors(node, allNodes):
    """
    @param node
    Returns all the neighbors for a node

    """
    # Up, down, left, right
    dirs = [[0, 1], [0, -1], [-1, 0], [1, 0]]
    result = []

    for dir in dirs:
        neighbor = (node[0] + dir[0], node[1] + dir[1])
        # Make sure the node is not out of bounds
        if neighbor in allNodes:
            result.append(neighbor)

    return result

#TODO implement cost function
