from queue import PriorityQueue

from algorithms.Base import *


def heuristic(start, end):
    return abs(start[0] - end[0]) + abs(start[1] - end[1])


class GreedyBFS(Base):
    def __init__(self, matrix, start, end):
        super().__init__(matrix, start, end)

    def find(self):
        queue = PriorityQueue()
        queue.put([0, self.start])
        trace = {self.start: None}
        while not queue.empty():
            dis, current = queue.get()
            if current == self.end:
                break
            for step in self.steps:
                neighbor = (current[0] + step[0], current[1] + step[1])
                if not self.inside_matrix(neighbor):
                    continue
                if neighbor not in trace:
                    queue.put([heuristic(neighbor, self.end), neighbor])
                    trace[neighbor] = current
        return self.trace_path(trace)
