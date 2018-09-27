"""
agent.py

The different algorithms making up the agent program.
"""

from datatypes import Queue
from datatypes import PriorityQueue


def BFS(graph, start, goal):
    """ Implementation of breadth first search """

    # frontier = set of all leafnodes available
    # for expansion at any given point.
    frontier = Queue()
    frontier.put(start)

    # Hash table to keep track of which nodes are visited
    parents = {}
    parents[start] = None

    while not frontier.empty():
        current = frontier.get()

        if current == goal:
            break

        for next in graph.neighbors(current):
            # checks wheter next is a key in parent
            if next not in parents:
                frontier.put(next)
                parents[next] = current

    path = reconstructPath(parents, start, goal)

    return path


def dijkstra(graph, start, goal):
    """ Implementation of Dijstras algorithm. """

    frontier = PriorityQueue()
    frontier.put(start, 0)

    parents = {}
    costSoFar = {}

    parents[start] = None
    costSoFar[start] = 0

    while not frontier.empty():
        current = frontier.get()

        if current == goal:
            break;

        for next in graph.neighbors(current):
            newCost = costSoFar[current] + graph.cost(next)

            if next not in costSoFar or newCost < costSoFar[next]:
                costSoFar[next] = newCost
                priority = newCost
                frontier.put(next, priority)
                parents[next] = current

    path = reconstructPath(parents, start, goal)

    return path, costSoFar

def heuristic(a, b):
    """ Heuristic function used by A* """
    (x1, y1) = a
    (x2, y2) = b

    return abs(x1 - x2) + abs(y1 - y2)

def aStar(graph, start, goal):
    """ Implementation of A* """

    frontier = PriorityQueue()
    frontier.put(start, 0)

    parents = {}
    costSoFar = {}

    parents[start] = None
    costSoFar[start] = 0

    while not frontier.empty():
        current = frontier.get()

        if current == goal:
            break;

        for next in graph.neighbors(current):
            newCost = costSoFar[current] + graph.cost(next)
            if next not in costSoFar or newCost < costSoFar[next]:
                costSoFar[next] = newCost
                priority = newCost + heuristic(goal, next)
                frontier.put(next, priority)
                parents[next] = current

    path = reconstructPath(parents, start, goal)
 
    return path

def reconstructPath(parents, start, goal):
    """ Returns a list with the sequence of nodes in the path. """
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = parents[current]
    path.append(start)
    path.reverse()

    return path
