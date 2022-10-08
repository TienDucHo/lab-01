import getopt
import sys

import utility
from algorithms.AStar import *
from algorithms.BFS import *
from algorithms.BellmanFord import *
from algorithms.DFS import *
from algorithms.UCS import *


def main():
    inp_name = ""
    out_name = ""
    algo = ""
    argv = sys.argv[1:]
    print(argv)
    try:
        opts, args = getopt.getopt(argv, 'i:o:a:', ["input=", "output=", "algorithm="])
    except getopt.GetoptError:
        print("Command error")
        sys.exit(2)
    print(opts)
    for com, val in opts:
        if com in ['-i', '--input']:
            inp_name = val
        elif com in ['-o', '--output']:
            out_name = val
        elif com in ['-a', '--algorithm']:
            algo = val
    if inp_name == "" or out_name == "" or algo == "":
        print("Missing elements")
        print(inp_name)
        print(out_name)
        print(algo)
        sys.exit(2)

    bonus, matrix = utility.read_from_file(inp_name)
    start, end = utility.get_start_end(matrix)

    route = []
    if algo == "dfs":
        route = DFS(matrix, start, end).find()
    elif algo == "bfs":
        route = BFS(matrix, start, end).find()
    elif algo == "ucs":
        route = UCS(matrix, start, end).find()
    elif algo == "greedy":
        route = GreedyBFS(matrix, start, end).find()
    elif algo == "astar":
        route = AStar(matrix, start, end).find()
    elif algo == "bonus":
        route = BellmanFord(matrix, start, end, bonus).find()
    else:
        print("Please check all the algorithms you can use")

    plt = utility.visualize_maze(matrix, bonus, start, end, route)
    plt.savefig(out_name)


if __name__ == '__main__':
    main()
