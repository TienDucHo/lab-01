class Base:
    def __init__(self, matrix, start, end):
        self.matrix = matrix
        self.start = start
        self.end = end
        self.wall_symbol = 'x'
        self.steps = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def inside_matrix(self, point):
        if point[0] >= len(self.matrix) or point[0] < 0:
            return False
        if point[1] >= len(self.matrix[0]) or point[1] < 0:
            return False
        if self.matrix[point[0]][point[1]] == self.wall_symbol:
            return False
        return True

    def trace_path(self, trace):
        current = self.end
        path = []

        while current != self.start:
            path.append(current)
            current = trace[current]

        path.append(self.start)
        path.reverse()

        return path

    def find(self):
        pass
