import bottom_up
import matrix
import top_down
from utils import *
import sys


def get_type(arg):
    if arg == '-m':
        return 0
    if arg == '-u':
        return 1
    if arg == '-d':
        return 2
    return -1


def print_error():
    print('Correct call:')
    print('python analyze.py -t <grammar_filename> <graph_filename> (optional)<result_filename>')


def run(algo_type, grammar_filename, graph_filename, result_filename=''):
    res = []
    if algo_type == -1:
        print('Incorrect type of algorithm')
        print('Type:\n'
              '-m for matrix algorithm\n'
              '-u for bottom_up algorithm\n'
              '-d for top_down algorithm\n')
        print_error()
        sys.exit(1)
    elif algo_type == 0:
        res = matrix.run(grammar_filename, graph_filename)
    elif algo_type == 1:
        res = bottom_up.run(grammar_filename, graph_filename)
    elif algo_type == 2:
        res = top_down.run(grammar_filename, graph_filename)

    print("Printing...")

    res_str = res_to_str(res)
    if result_filename == '':
        print(res_str)
    else:
        with open(result_filename, 'w') as file:
            file.writelines(res_str)

    print('Printing: Done')


size = len(sys.argv)
if size == 4:
    algo_type = get_type(sys.argv[1])
    grammar_filename = sys.argv[2]
    graph_filename = sys.argv[3]
    run(algo_type, grammar_filename, graph_filename)
elif size == 5:
    algo_type = get_type(sys.argv[1])
    grammar_filename = sys.argv[2]
    graph_filename = sys.argv[3]
    result_filename = sys.argv[4]
    run(algo_type, grammar_filename, graph_filename, result_filename)
else:
    print('Incorrect number of arguments')
    print_error()
