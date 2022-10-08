import getopt
import sys

from algorithms.AStar import *
from algorithms.BFS import *
from algorithms.DFS import *
from algorithms.GreedyBFS import *
from algorithms.UCS import *


def main():
    inp_name = ""
    out_name = ""
    algo = ""
    argv = sys.argv[1:]
    try:
        opts, args = getopt.getopt(argv, 'i:o:a', ["input=", "output=", "algorithm="])
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
        print("Missing elements")
        sys.exit(2)

    route = []
    if algo == "dfs":
        route = DFS.find()
    elif algo == "bfs":
        route = find()
    elif algo == "greedybfs":
        route = greedybfs()
    elif algo == "astar":
        route = astar()
    elif algo == "bonus":
        route = bonus()
    else:
        print("Please check all the algorithms you can use")
