from collections import deque

from algorithms.Base import *


class BellmanFord(Base):
    def __init__(self, matrix, start, end, bonus):
        super().__init__(matrix, start, end)
        self.bonus = {}
        for x, y, reward in bonus:
            if (x, y) not in self.bonus:
                self.bonus[(x, y)] = reward

        self.min_bonus = self.bonus[min(self.bonus.keys(), key=(lambda kt: self.bonus[kt]))]

    def heuristic(self, end):
        if end in self.bonus:
            return self.bonus[end]
        return abs(self.min_bonus)

    def trace_path(self, trace):
        current = self.end
        path = []

        total_bonuses = 0
        total_cost = 0

        while current != self.start:
            path.append(current)
            total_cost += 1
            if current in self.bonus:
                total_bonuses += self.bonus[current]
                total_cost += self.bonus[current]
                print(current)
            current = trace[current]

        total_cost = 0 if total_cost < 0 else total_cost
        print('Total bonuses:', total_bonuses)
        print('Total cost:', total_cost)

        path.append(self.start)
        path.reverse()

        return path

    def find(self):
        queue = deque()
        queue.append(self.start)
        trace, cost = {self.start: None}, {self.start: 0}

        while len(queue) > 0:
            current = queue.popleft()
            for step in self.steps:
                neighbor = (current[0] + step[0], current[1] + step[1])
                if not self.inside_matrix(neighbor):
                    continue

                cost_new = cost[current] + self.heuristic(neighbor)
                if (neighbor not in cost) or (cost_new < cost[neighbor]):
                    cost[neighbor] = cost_new
                    queue.append(neighbor)
                    trace[neighbor] = current

        return self.trace_path(trace)
