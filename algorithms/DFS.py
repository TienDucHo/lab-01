from Base import *


class DFS(Base):
    def __init__(self, matrix, start, end):
        super().__init__(matrix, start, end)

    def find(self):
        visited, queue = [], []
        trace = {self.start: None}
        visited.append(self.start)
        queue.append(self.start)

        while len(queue) > 0:
            current = queue.pop()
            visited.append(current)
            if current == self.end:
                break
            for step in self.steps:
                neighbor = (current[0] + step[0], current[1] + step[1])

                if self.inside_matrix(neighbor):
                    if neighbor not in visited:
                        queue.append(neighbor)
                        trace[neighbor] = current

        return self.trace_path(trace)
