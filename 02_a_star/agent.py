"""
agent.py

The different algorithms making up the agent program.
"""

from datatypes import Queue


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
            if next not in parents:
                frontier.put(next)
                parents[next] = current

    return parents

