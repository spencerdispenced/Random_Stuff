
from collections import deque


class Stack:

    def __init__(self) -> None:
        self.container = deque()

    def push(self, item):
        self.container.append(item)

    def pop(self, item):
        self.container.pop()

    def peek(self):
        return self.container[-1]

    def size(self):
        return len(self.container)

    def empty(self):
        self.container.clear()
