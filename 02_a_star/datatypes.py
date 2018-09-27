import collections

class Queue:
    """ Simple Queue class """
    def __init__(self):
        self.elements = collections.deque()
    def empty(self):
        return len(self.elements) == 0
    def put(self, item):
        self.elements.append(item)
    def get(self):
        return self.elements.popleft()
