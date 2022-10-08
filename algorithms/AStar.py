from GreedyBFS import *


class AStar(GreedyBFS):
    def __int__(self, matrix, start, end):
        super().__init__(matrix, start, end)

    def find(self):
        queue = PriorityQueue()
        queue.put([0, self.start])
        trace, cost = {self.start: None}, {self.start: 0}
        while not queue.empty():
            dist, current = queue.get()
            if current == self.end:
                break
            for step in self.steps:
                neighbor = (current[0] + step[0], current[1] + step[1])
                if not self.inside_matrix(neighbor):
                    continue
                cost_new = cost[current] + heuristic(current, self.end)
                if (neighbor not in cost) or (cost_new < cost[neighbor]):
                    cost[neighbor] = cost_new
                    queue.put([cost_new, neighbor])
                    trace[neighbor] = current
        return self.trace_path(trace)
