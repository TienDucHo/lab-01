import getopt
import sys

import utility


def main ():
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

    bonus, matrix = utility.read_from_file(inp_name)
    start, end = utility.getStartEnd(matrix)

    route = []
    if algo=="dfs":
        route=dfs()
    elif algo=="bfs":
        route=bfs()
    elif algo=="greedybfs":
        route=greedybfs()
    elif algo=="astar":
        route=astar()
    elif algo=="bonus":
        route=bonus()
    else:
        print("Please check all the algorithms you can use")
