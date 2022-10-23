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
    try:
        opts, args = getopt.getopt(argv, 'i:o:a:', ["input=", "output=", "algorithm="])
    except getopt.GetoptError:
        print("Command error")
        sys.exit(2)
    for com, val in opts:
        if com in ['-i', '--input']:
            inp_name = val
        elif com in ['-o', '--output']:
            out_name = val
        elif com in ['-a', '--algorithm']:
            algo = val
    if inp_name == "" or out_name == "" or algo == "":
        sys.exit(2)

    bonus, matrix = utility.read_from_file(inp_name)
    start, end = utility.get_start_end(matrix)

    route = []
    route1 = []
    if algo == "dfs":
        route = DFS(matrix, start, end).find()
    elif algo == "bfs":
        route = BFS(matrix, start, end).find()
    elif algo == "ucs":
        route = UCS(matrix, start, end).find()
    elif algo == "gbfs":
        route = GreedyBFS(matrix, start, end).find(heuristic=0)
        route1 = GreedyBFS(matrix, start, end).find(heuristic=1)
    elif algo == "astar":
        route = AStar(matrix, start, end).find(heuristic=0)
        route1 = AStar(matrix, start, end).find(heuristic=1)
    elif algo == "bonus":
        route = BellmanFord(matrix, start, end, bonus).find()
    else:
        print("Please check all the algorithms you can use")

    plt = utility.visualize_maze(matrix, bonus, start, end, route)
    plt.savefig(out_name)

    if len(route1) > 0:
        plt2 = utility.visualize_maze(matrix, bonus, start, end, route1)
        plt2.savefig("{}-euclid.png".format(out_name))


if __name__ == '__main__':
    main()
