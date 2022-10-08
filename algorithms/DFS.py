from Base import *


class DFS(Base):
    def __init__(self, matrix, start, end):
        super().__init__(matrix, start, end)

    def find(self):
        visited, stack = [], []
        trace = {self.start: None}
        visited.append(self.start)
        stack.append(self.start)

        while len(stack) > 0:
            current = stack.pop()
            visited.append(current)
            if current == self.end:
                break
            for step in self.steps:
                neighbor = (current[0] + step[0], current[1] + step[1])

                if self.inside_matrix(neighbor) and neighbor not in visited:
                    stack.append(neighbor)
                    trace[neighbor] = current

        return self.trace_path(trace)
