def read_from_file(filename):
    bonus, matrix = [], []
    with open(filename) as f:
        lines = f.readlines()
        n = int(lines[0])
        for i in range(n):
            x, y, reward = map(int, lines[i + 1].split(' '))
            bonus.append((x, y, reward))

        matrix = [list(line.strip()) for line in lines[n + 1:]]
    return bonus, matrix
