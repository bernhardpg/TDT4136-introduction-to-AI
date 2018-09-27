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

    # It might be useful to return costSoFar
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
