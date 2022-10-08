from collections import deque

from algorithms.Base import *


class BFS(Base):
    def __int__(self, matrix, start, end):
        super().__init__(matrix, start, end)

    def find(self):
        visited, queue = [], deque()
        queue.append(self.start)
        visited.append(self.start)

        trace = {self.start: None}

        while len(queue) > 0:
            current = queue.popleft()
            if current == self.end:
                break
            for step in self.steps:
                neighbor = (current[0] + step[0], current[1] + step[1])
                if self.inside_matrix(neighbor) and neighbor not in visited:
                    trace[neighbor] = current
                    visited.append(neighbor)
                    queue.append(neighbor)

        return self.trace_path(trace)
